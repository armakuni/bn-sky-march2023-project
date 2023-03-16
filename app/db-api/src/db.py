import mysql.connector
import os

readDatabaseHost = (
    "ecommercedb-cluster.cluster-ro-crhc8869crtd.us-east-2.rds.amazonaws.com"
)
writeDatabaseHost = (
    "ecommercedb-cluster.cluster-crhc8869crtd.us-east-2.rds.amazonaws.com"
)

user = os.environ.get("ec_USERNAME")
password = os.environ.get("ec_PASSWORD")
database = os.environ.get("ec_DATABASE")


class DB:
    def readConnection(self):
        return mysql.connector.connect(
            user=user,
            password=password,
            host=readDatabaseHost,
            database=database,
        )
