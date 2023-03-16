from routeHandlers import UserRoutes, ProductRoutes
from flask import Flask
from db import DB

app = Flask(__name__)

userRoutes = UserRoutes(DB())
productRoutes = ProductRoutes(DB())


@app.route("/users")
def users():
    return userRoutes.users()


@app.route("/products")
def products():
    return productRoutes.products()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
