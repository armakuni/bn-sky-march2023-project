from routeHandlers import UserRoutes
from flask import Flask
from db import DB

app = Flask(__name__)

userRoutes = UserRoutes(DB())


@app.route("/users")
def users():
    return userRoutes.users()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
