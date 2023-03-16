import os
import requests

from typing import List
from flask import Flask, request, jsonify, make_response

from util import ShopItem, calculate_cart_total


db_api_url = os.environ.get("DB_URL")


app = Flask(__name__)


user_cart: List[ShopItem] = []


@app.route("/checkout", methods=["POST"])
def post_checkout():
    try:
        subtotal = calculate_cart_total(cart=user_cart)
        # Handle some Payment hold
        # EG: Strike.make_payment_intent("card details", subtotal)
        # If success, continue:
        # Check items in Cart and retreive
        for item in user_cart:
            requests.delete(f"{db_api_url}/product", params={id: item.id})
        
        response_data = {'message': 'SUCCESS', "data": {"cart": user_cart, "subtotal": subtotal}}

        return make_response(jsonify(response_data), 200)
    
    except:
        response_data = {'message': 'FAILED'}

        return make_response(jsonify(response_data), 404)


@app.route("/cart", methods=["GET"])
def get_cart():
    try: 

        response_data = {'message': 'SUCCESS', "data": {"cart": user_cart, "subtotal": calculate_cart_total()}}

        return make_response(jsonify(response_data), 200)
    
    except:
        response_data = {'message': 'FAILED'}

        return make_response(jsonify(response_data), 404)



@app.route("/cart", methods=["POST"])
def post_cart():
    try: 
        shop_item_id = request.get_json().get("item_id")

        product_from_db = requests.get(f"{db_api_url}/<product>", params={id: shop_item_id})

        # Potentially reserve item
        shop_item = ShopItem(product_from_db.id, product_from_db.name, product_from_db.unit_price)

        user_cart.append(ShopItem(shop_item))

        response_data = {'message': 'SUCCESS', "data": {"cart": user_cart, "subtotal": calculate_cart_total()}}

        return make_response(jsonify(response_data), 200)
    
    except:
        response_data = {'message': 'FAILED'}

        return make_response(jsonify(response_data), 404)


@app.route("/", methods=["GET"])
def get_index():
    return f"<h1> Hello World </h1><br/><p>Your Database URL is: {db_api_url}</p>"


if __name__ == "__main__":
    print("APP IS WORKING...")
    app.run(host="0.0.0.0", port=8000)
