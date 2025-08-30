# Visual Product Matcher

An AI-powered image similarity search system that leverages a hybrid approach to find visually and semantically similar products. Upload an image or provide a URL, and let our system find matching products based on a combination of visual and textual features.

---

## Features

- **Image Upload:** Supports both file uploads and image URLs for flexible searching.  
- **Hybrid Search:** Combines a visual search (comparing images) with a textual search (comparing product names) for highly accurate results.  
- **Dynamic Interface:** Displays the uploaded query image and a list of similar products with their similarity scores.  
- **User-Friendly Controls:** Allows users to filter results by a minimum similarity score and limit the number of products shown.  
- **Responsive Design:** The application's interface is mobile-friendly and accessible on any device.  
- **Robust Backend:** Includes basic error handling and a simple data model for easy maintenance.  

---

## Technical Approach

The core of this project is its **hybrid search model**, which combines two different methodologies for superior results.

### Visual Similarity
- Uses a **lightweight perceptual hashing approach** instead of heavy deep learning models.  
- Creates a unique "fingerprint" for each image by analyzing structure and texture.  
- Combines multiple hashes (`phash`, `dhash`, `whash`) with image pre-processing (grayscaling, resizing) to ensure accuracy.  

### Textual Similarity
- Uses **fuzzy string matching** to compare user text queries with product names.  
- Adds a semantic layer to correct for visual mismatches and find conceptually similar products.  

### Combined Scoring
- Final similarity score is calculated using a **weighted average of visual and textual scores**.  
- Ensures results are both visually and contextually relevant.  

This approach balances **performance and accuracy**, providing a scalable solution suitable for practical use.

---

## Setup and Installation

### Prerequisites
- Python 3.8+  

### Steps

1. **Clone the Repository:**
```bash
git clone https://github.com/meharshsri11/Visual_Product_Matcher.git
cd Visual_Product_Matcher
Create a Virtual Environment:

bash
Copy code
python -m venv .venv
Activate the Virtual Environment:

Windows:

bash
Copy code
.\.venv\Scripts\activate
macOS/Linux:

bash
Copy code
source .venv/bin/activate
Install Required Libraries:

bash
Copy code
pip install -r requirements.txt
Run the Flask Application:

bash
Copy code
flask run
The application will be accessible at: http://127.0.0.1:5000

Usage
Open your web browser and navigate to the local host URL.

Upload a product image file or paste an image URL.

Optionally, enter a text query (e.g., "blue jeans").

Click "Find Similar Products" to see the results.

Notes
Make sure your static/uploads/ folder exists for uploaded files.

Sensitive files like .env and virtual environment folders are excluded via .gitignore.

For large-scale use, consider integrating cloud storage for uploads.
