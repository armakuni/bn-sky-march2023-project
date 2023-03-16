from contextlib import closing
from flask import Flask
import os

app = Flask(__name__)
import mysql.connector


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


readDatabaseHost = (
    "ecommercedb-cluster.cluster-ro-crhc8869crtd.us-east-2.rds.amazonaws.com"
)
writeDatabaseHost = (
    "ecommercedb-cluster.cluster-crhc8869crtd.us-east-2.rds.amazonaws.com"
)

user = os.environ.get("ec_USERNAME")
password = os.environ.get("ec_PASSWORD")
database = os.environ.get("ec_DATABASE")

print(user, password, database)


@app.route("/users")
def users():
    with closing(readDatabaseConnection()) as cnx:
        with closing(cnx.cursor()) as cursor:
            cursor.execute("SELECT id, username FROM users")
            return [{id: username} for (id, username) in cursor]


def readDatabaseConnection():
    return mysql.connector.connect(
        user=user,
        password=password,
        host=readDatabaseHost,
        database=database,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
