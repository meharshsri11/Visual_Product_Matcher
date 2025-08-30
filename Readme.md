**Visual Product Matcher**

This project is a web application that helps users find visually and semantically similar products. Built as a technical assessment, it demonstrates a solution for building a robust and efficient product search engine using a hybrid approach. The application allows users to upload an image or provide a URL, as well as an optional text query, to find the most relevant products from a database.

**Key Features**

Image Upload: Supports both file uploads and image URLs for flexible searching.

Hybrid Search: Combines a visual search (comparing images) with a textual search (comparing product names) for highly accurate results.

Dynamic Interface: Displays the uploaded query image and a list of similar products with their similarity scores.

User-Friendly Controls: Allows users to filter results by a minimum similarity score and limit the number of products shown.

Responsive Design: The application's interface is designed to be mobile-friendly and accessible on any device.

Robust Backend: Includes basic error handling and a simple data model for easy maintenance.

**Technical Approach**

The core of this project is its hybrid search model, which combines two different search methodologies to deliver superior results.

Visual Similarity: Instead of a complex, resource-intensive deep learning model, a lightweight perceptual hashing approach was chosen. This method creates a unique "fingerprint" for each image by analyzing its structure and texture. The application uses a combination of multiple hashes (phash, dhash, and whash) and image pre-processing (grayscaling, resizing) to ensure a high degree of accuracy without heavy computational requirements.

Textual Similarity: A fuzzy string matching algorithm is used to compare a user's text query with product names in the database. This adds a semantic layer to the search, helping to correct for visual mismatches and find products that are conceptually similar.

Combined Scoring: A final similarity score is calculated by combining the visual and textual scores using a weighted average. This ensures the search results are both visually and contextually relevant.

This approach demonstrates an understanding of the trade-off between complexity and performance, providing a scalable and efficient solution that meets the project's constraints.

**Setup and Installation**

To run this project, you will need Python 3.8+.

Clone the Repository:

Bash

git clone https://github.com/meharshsri11/Visual-Product-Matcher-Unthinkable-4-.git
cd Visual-Product-Matcher-Unthinkable-4-
Create a Virtual Environment:

Bash

python -m venv .venv
Activate the Virtual Environment:

On Windows:

Bash

.\.venv\Scripts\activate
On macOS/Linux:

Bash

source .venv/bin/activate
Install Required Libraries:

Bash

pip install -r requirements.txt
Run the Flask Application:

Bash

flask run
The application will be accessible at http://127.0.0.1:5000.

**Usage**

To use the application, open your web browser and navigate to the local host URL.

Upload a product image file or paste an image URL.

Optionally, enter a text query (e.g., "blue jeans").

Click "Find Similar Products" to see the results.
