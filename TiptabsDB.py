import mysql.connector


class TiptabsDB:

    def __init__(self):

        self.TiptabsDBConnector = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="root"
        )

        self.TiptabsDBConnector.cursor().execute("DROP DATABASE tiptabs_db;")
        self.TiptabsDBConnector.cursor().execute("CREATE DATABASE tiptabs_db;")
        self.TiptabsDBConnector.cursor().execute("USE tiptabs_db;")
        self.TiptabsDBConnector.cursor().execute("CREATE TABLE users (username VARCHAR(20), password VARCHAR(20), favorite_conversions VARCHAR(35));")

    def add_entry(self, entry):
        self.TiptabsDBConnector.cursor().execute("INSERT INTO users (username, password, favorite_conversions) " +
                                       "VALUES ('garym', 'gary', 'EURtoUSD');")
        add_entry_result = [True, "Item was added successfully to the Database."]
        return add_entry_result

    def remove_entry(self, entry):
        remove_entry_result = [True, "Item was removed successfully from the Database."]
        return remove_entry_result

    def retrieve_entry(self, entry):
        item_collection = "Item placeholder."
        retrieve_entry_result = [True, item_collection]
        return retrieve_entry_result

    def get_all_users(self):
        users = self.TiptabsDBConnector.cursor().execute("SELECT username FROM users;")
        all_users_result = [True, users]
        return all_users_result
