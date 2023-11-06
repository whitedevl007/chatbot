# import random

# # Sample product data
# products = [
#     {"name": "Smartphone A", "description": "The latest smartphone from Samsung with amazing features.", "price": 800.0, "available": True, "brand": "Samsung"},
#     {"name": "Smartphone B", "description": "An Apple smartphone known for its sleek design.", "price": 600.0, "available": True, "brand": "Apple"},
#     {"name": "Laptop C", "description": "High-performance Dell laptop for your computing needs.", "price": 1200.0, "available": True, "brand": "Dell"},
#     {"name": "Smart TV D", "description": "Samsung Smart TV with a stunning display.", "price": 900.0, "available": True, "brand": "Samsung"},
#     {"name": "Smart Speaker E", "description": "Google Smart Speaker for voice-activated assistance.", "price": 100.0, "available": True, "brand": "Google"},
#     # Additional sample product entries
# ]

# users = {}  # Initialize the users dictionary

# # Initialize the shopping cart for a user
# def initialize_shopping_cart(user_id):
#     if user_id not in users:
#         users[user_id] = {"cart": []}

# # Function to provide user-friendly and engaging responses
# def chatbot_response(user_id, user_message, product_collection, users):
#     user_message = user_message.lower()
#     initialize_shopping_cart(user_id)

#     # Retrieve product data from MongoDB (assuming product_collection is a valid MongoDB collection)
#     products = list(product_collection.find({}))

#     # Add logic for discounts and sales
#     def apply_discounts(cart):
#         discounted_cart = cart.copy()
#         # Apply a 10% discount to the cart items
#         for item in discounted_cart:
#             item['price'] *= 0.9  # Applying a 10% discount
#         return discounted_cart

#     if "apply discounts" in user_message:
#         cart_items = users[user_id]["cart"]
#         if cart_items:
#             discounted_cart = apply_discounts(cart_items)
#             return "Great news! A 10% discount has been applied to your cart. You can complete the purchase now or continue exploring our products."
#         else:
#             return "Your cart is empty. Please add items to apply discounts."

#     # Function to simulate a purchase with discount
#     def simulate_purchase_with_discount():
#         cart_items = users[user_id]["cart"]
#         if cart_items:
#             total_price = sum(item['price'] for item in cart_items)
#             discounted_total = sum(item['price'] for item in apply_discounts(cart_items))
#             users[user_id]["cart"] = []  # Clear the cart
#             return f"Your purchase is confirmed! 🎉 Total Price: ${total_price:.2f}. After 10% discount: ${discounted_total:.2f}. Thank you for shopping with us!"
#         else:
#             return "Your cart is empty. Please add items to make a purchase."

#     if "complete purchase" in user_message or "finish buying" in user_message or "finalize purchase" in user_message:
#         return simulate_purchase_with_discount()

#     # Function to recommend items
#     def recommend_product():
#         available_products = [product for product in products if product["available"]]
#         if available_products:
#             recommended_product = random.choice(available_products)
#             return f"I recommend {recommended_product['name']} 🌟. It is available for ${recommended_product['price']}. Would you like to add it to your cart?"
#         else:
#             return "I'm sorry, but there are no products available for recommendations at the moment. How about exploring our product list?"

#     if "recommend" in user_message:
#         return recommend_product()

#     # Incorporate engaging responses based on user queries
#     if "hello" in user_message or "hi" in user_message:
#         return "Hello! 😊 Welcome to our store. How can I assist you today? You can ask about available products, discounts, or request recommendations."

#     if "products" in user_message or "show available products" in user_message:
#         product_list = [f"{product['name']} - ${product['price']}" for product in products if product["available"]]
#         response = "Here are the products we have available:\n"
#         response += "\n".join(product_list)
#         response += "\nWould you like to add any of these to your cart or need a recommendation?"
#         return response

#     if "help" in user_message or "assistance" in user_message:
#         return "Sure, I'm here to assist you. You can ask about available products, request recommendations, add items to your cart, apply discounts, or complete your purchase."

#     # Add logic to handle adding items to the cart
#     if "add to cart" in user_message:
#         product_name = user_message.replace("add to cart", "").strip()
#         product = next((p for p in products if p["name"].lower() == product_name and p["available"]), None)
#         if product:
#             users[user_id]["cart"].append(product)
#             return f"{product['name']} has been added to your cart! 🛒 Would you like to explore more or proceed to checkout?"

#     # Handle showing the cart
#     if "show my cart" in user_message or "display cart" in user_message:
#         cart_items = users[user_id]["cart"]
#         if cart_items:
#             cart_list = [f"{item['name']} - ${item['price']}" for item in cart_items]
#             response = "Your cart contains the following items:\n"
#             response += "\n".join(cart_list)
#             response += "\nWould you like to proceed with the purchase, apply discounts, or get a recommendation?"
#             return response
#         else:
#             return "Your cart is empty. Would you like to add some products?"

#     # For unknown commands or messages
#     return "I'm sorry, I couldn't quite understand that. 😔 Please feel free to ask another question or type 'help' for assistance."

# # Testing the chatbot logic
# user_id = 123  # Simulating a user ID
# user_message = "Hello, can you recommend something for me?"

# response = chatbot_response(user_id, user_message, products, users)
# print(response)




import random
from pymongo import MongoClient


# Sample product data
products = [
    {"name": "Smartphone A", "description": "The latest smartphone from Samsung with amazing features.", "price": 800.0, "available": True, "brand": "Samsung"},
    {"name": "Smartphone B", "description": "An Apple smartphone known for its sleek design.", "price": 600.0, "available": True, "brand": "Apple"},
    {"name": "Laptop C", "description": "High-performance Dell laptop for your computing needs.", "price": 1200.0, "available": True, "brand": "Dell"},
    {"name": "Smart TV D", "description": "Samsung Smart TV with a stunning display.", "price": 900.0, "available": True, "brand": "Samsung"},
    {"name": "Smart Speaker E", "description": "Google Smart Speaker for voice-activated assistance.", "price": 100.0, "available": True, "brand": "Google"},
    # Additional sample product entries
]

users = {}

def get_product_collection():
    # Replace 'MONGO_URI' with your actual MongoDB Atlas connection string
    MONGO_URI = "mongodb+srv://your_username:your_password@cluster0.t6dii5m.mongodb.net/"
    client = MongoClient(MONGO_URI)
    db = client["ecommerce"]
    collection = db["products"]  # Assuming the collection name is 'products'
    return collection# Initialize the users dictionary

def initialize_shopping_cart(user_id):
    if user_id not in users:
        users[user_id] = {"cart": []}
#     # Access the cart items separately after initialization
 
 
 # Function to add products to the cart
def add_to_cart(user_id, user_message):
    product_name = user_message.split("add to cart,")[-1].strip()

    product = next((p for p in products if p["name"].lower() == product_name.lower() and p["available"]), None)
    if product:
        if user_id not in users:
            users[user_id] = {"cart": []}
        users[user_id]["cart"].append(product)
        return f"{product['name']} has been added to your cart! 🛒"
    else:
        return "The product is not available or does not exist. Please try a different product."

def show_my_cart(user_id):
    if user_id in users and "cart" in users[user_id] and users[user_id]["cart"]:
        cart_items = users[user_id]["cart"]
        cart_list = [f"{item['name']} - ${item['price']}" for item in cart_items]
        response = "Your cart contains the following items:\n"
        response += "\n".join(cart_list)
        response += "\nWould you like to proceed with the purchase, apply discounts, or get a recommendation?"
        return response
    else:
        return "Your cart is empty. Would you like to add some products?"

# Function to display available products
def display_available_products():
    available_product_list = [f"{product['name']} - ${product['price']}" for product in products if product["available"]]
    response = "Here are the available products:\n"
    response += "\n".join(available_product_list)
    response += "\nYou can add a product to your cart or ask for recommendations."
    return response
def apply_discounts(cart):
    for item in cart:
        item['price'] *= 0.9  # Applying a 10% discount
    return cart

def simulate_purchase_with_discount(user_id):
    cart_items = users.get(user_id, {}).get("cart", [])
    if cart_items:
        total_price = sum(item['price'] for item in cart_items)
        discounted_total = sum(item['price'] for item in apply_discounts(cart_items))
        return f"Your purchase is confirmed! 🎉 Total Price: ${total_price:.2f}. After 10% discount: ${discounted_total:.2f}. Thank you for shopping with us!"
    else:
        return "Your cart is empty. Please add items to make a purchase."

       
# Function to provide user-friendly and engaging responses
def chatbot_response(user_id, user_message, product_collection, users):
    user_message = user_message.lower()
    initialize_shopping_cart(user_id)

    cart_items = users.get(user_id, {}).get("cart", [])
    # Add logic for discounts and sales
    def apply_discounts(cart):
        discounted_cart = cart.copy()
        # Apply a 10% discount to the cart items
        for item in discounted_cart:
            item['price'] *= 0.9  # Applying a 10% discount
        return discounted_cart

    # Function to recommend items
    def recommend_product():
        available_products = [product for product in products if product["available"]]
        if available_products:
            recommended_product = random.choice(available_products)
            return f"I recommend {recommended_product['name']} 🌟. It is available for ${recommended_product['price']}. Would you like to add it to your cart?"
        else:
            return "I'm sorry, but there are no products available for recommendations at the moment. How about exploring our product list?"

    # Logic for adding items to the cart
    if user_message.startswith("add to cart"):
        return add_to_cart(user_id, user_message)
    
    # Greeting messages and initial interaction
    if "hello" in user_message or "hi" in user_message:
        return "Hello! 😊 Welcome to our store. How can I assist you today? You can ask about available products, discounts, or request recommendations."

    # Display available products
    if "available products" in user_message or "show available products" in user_message:
        return display_available_products()

    # Help message presenting commands in bullet points
    if "help" in user_message:
        response = """Sure, I'm here to assist you. You can use the following commands:
        • 'Add to cart, [Product Name]' to add a product to your cart.
        • 'Show my cart' to view your cart items.
        • 'Complete purchase' to finish your shopping and apply discounts.
        • 'Recommend something for me' to get product recommendations.
        • 'Available products' to see the list of available products."""
        return response

    
    # Logic for adding items to the cart
    if user_message.startswith("add to cart"):
        return add_to_cart(user_id, user_message)

    # Display the contents of the cart
    if "show my cart" in user_message or "display cart" in user_message:
        return show_my_cart(user_id)

    # Complete purchase or checkout
    if "complete purchase" in user_message or "finish buying" in user_message or "finalize purchase" in user_message:
        return simulate_purchase_with_discount(user_id)

    # Request for product recommendations
    if "recommend" in user_message:
        return recommend_product()

    # For unknown commands or messages
    return "I'm sorry, I couldn't quite understand that. 😔 Please feel free to ask another question or type 'help' for assistance."

user_id = "123"
user_message = "Hello, can you recommend something for me?"
product_collection = get_product_collection()
users = {}  # Initialize the users dictionary

response = chatbot_response(user_id, user_message, product_collection, users)
print(response)
