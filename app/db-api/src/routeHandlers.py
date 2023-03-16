from contextlib import closing


class UserRoutes:
    def __init__(self, db):
        self.db = db

    def users(self):
        with closing(self.db.readConnection()) as cnx:
            with closing(cnx.cursor()) as cursor:
                cursor.execute("SELECT id, username FROM users")
                return [
                    {"id": int(id), "username": username} for (id, username) in cursor
                ]


class ProductRoutes:
    def __init__(self, db):
        self.db = db

    def products(self):
        with closing(self.db.readConnection()) as cnx:
            with closing(cnx.cursor()) as cursor:
                cursor.execute(
                    "SELECT id, name, price, quantity, imageurl FROM products"
                )
                return [
                    {
                        "id": int(id),
                        "name": name,
                        "price": float(price),
                        "quantity": quantity,
                        "imageurl": imageurl,
                    }
                    for (id, name, price, quantity, imageurl) in cursor
                ]
