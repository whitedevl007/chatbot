
from flask import Flask, request, render_template, jsonify
from chatbot.chatbot_logic import chatbot_response, initialize_shopping_cart
from pymongo import MongoClient

app = Flask(__name__)

# Replace the following connection string with your MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://your_username:your_password@cluster0.t6dii5m.mongodb.net/"

# Function to connect to MongoDB and return the product collection
def get_product_collection():
    # Replace 'MONGO_URI' with your actual MongoDB Atlas connection string
    MONGO_URI = "mongodb+srv://your_username:your_password@cluster0.t6dii5m.mongodb.net/"
    client = MongoClient(MONGO_URI)
    db = client["ecommerce"]
    collection = db["products"]  # Assuming the collection name is 'products'
    return collection

users = {}  # Initialize the users dictionary

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')  # Render the HTML page

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    user_id = "default_user"  # You can change this as per your logic
    product_collection = get_product_collection()  # Make sure get_product_collection function is defined correctly
    response = chatbot_response(user_id, user_message, product_collection, users)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)