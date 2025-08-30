import os
import json
import base64
import requests
import imagehash
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from PIL import Image
import io
import uuid

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# --- Pre-process and hash the product database (one-time task) ---
def create_product_hashes():
    """
    This function generates and saves perceptual hashes for the product database.
    It should only be run once to initialize the database with hashes.
    """
    try:
        with open('data/products.json', 'r') as f:
            products_db = json.load(f)
    except FileNotFoundError:
        print("Error: products.json file not found.")
        return []

    updated_products_db = []
    print("Generating perceptual hashes for product images...")
    for product in products_db:
        # Construct the full filesystem path to the image
        img_path = os.path.join("static", product.get("image_path", ""))
        
        # This is the corrected way to store the path for the frontend
        product['image_path_web'] = f"/{img_path.replace(os.path.sep, '/')}"
        
        if os.path.exists(img_path):
            try:
                img = Image.open(img_path)
                product_hash = str(imagehash.phash(img))
                product['hash'] = product_hash
                updated_products_db.append(product)
            except Exception as e:
                print(f"Warning: Could not hash image {img_path}. Error: {e}")
                updated_products_db.append(product)
        else:
            print(f"Warning: Image file not found for product: {product.get('name', 'Unnamed')}")
            updated_products_db.append(product)

    print("Product hashes created successfully.")
    return updated_products_db

products_db = create_product_hashes()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_products():
    try:
        image_data = None
        if 'image_file' in request.files and request.files['image_file'].filename != '':
            image = request.files['image_file']
            image_data = image.read()
        elif 'image_url' in request.form and request.form['image_url'] != '':
            image_url = request.form['image_url']
            response = requests.get(image_url)
            response.raise_for_status()
            image_data = response.content
        else:
            return jsonify({'error': 'No image file or URL provided'}), 400

        results_limit = int(request.form.get('limit', 5))
        
        query_image = Image.open(io.BytesIO(image_data))

        unique_filename = f"query_{uuid.uuid4().hex}.jpg"
        upload_path = os.path.join("static/uploads", unique_filename)
        os.makedirs(os.path.dirname(upload_path), exist_ok=True)
        query_image.save(upload_path)
        query_image_path = "/" + upload_path.replace("\\", "/")

        query_hash = imagehash.phash(query_image)

        scored_products = []
        for product in products_db:
            if 'hash' in product:
                product_hash = imagehash.hex_to_hash(product['hash'])
                distance = query_hash - product_hash
                score = 100 - (distance / 64) * 100
                product['score'] = score
                scored_products.append(product)
        
        scored_products.sort(key=lambda p: p['score'], reverse=True)
        
        top_results = scored_products[:results_limit]
        
        final_results = []
        for product in top_results:
            final_results.append({
                "name": product.get("name", "Unnamed"),
                "category": product.get("category", "N/A"),
                "image_path": product.get("image_path_web", ""),
                "score": product.get('score', 0)
            })

        query_result = {
            "name": "Query Image",
            "category": "N/A",
            "image_path": query_image_path
        }

        return jsonify({
            "query_image": query_result,
            "similar_products": final_results
        })
    
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'An error occurred while fetching the image URL: {e}'}), 500
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)