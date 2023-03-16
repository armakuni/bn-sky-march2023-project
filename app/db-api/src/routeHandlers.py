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
