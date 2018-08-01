import mysql.connector


class TiptabsDB:

    def __init__(self):

        TiptabsDB = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="root"
        )

        tiptabs_db_cursor = TiptabsDB.cursor()
        tiptabs_db_cursor.execute("DROP DATABASE tiptabs_db;")
        tiptabs_db_cursor.execute("CREATE DATABASE tiptabs_db;")

    def add_entry(self, entry):
        add_entry_result = [True, "Item was added successfully to the Database."]
        return add_entry_result

    def remove_entry(self, entry):
        remove_entry_result = [True, "Item was removed successfully from the Database."]
        return remove_entry_result

    def retrieve_entry(self, entry):
        item_collection = "Item placeholder."
        retrieve_entry_result = [True, item_collection]
        return retrieve_entry_result
