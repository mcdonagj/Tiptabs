import mysql.connector


class TiptabsDB:

    def __init__(self):

        self.TiptabsDBConnector = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="root"
        )

        self.db_cursor = self.TiptabsDBConnector.cursor()

        commands = ["DROP DATABASE IF EXISTS tiptabs_db;", "CREATE DATABASE IF NOT EXISTS tiptabs_db;",
                    "USE tiptabs_db;",
                    "CREATE TABLE users (username VARCHAR(20), password VARCHAR(20), favorite_conversions VARCHAR(35));"]

        for command in commands:
            self.db_cursor.execute(command)

    def check_inputs(self, entry):
        valid_input = True

        if len(entry) != 4:
            valid_input = False
            invalid_entry_array = [valid_input, "Invalid number of entry items entered."]
            return invalid_entry_array

        for item in entry:
            if not len(item) > 0:
                valid_input = False

        if not valid_input:
            add_invalid_item_res = "Invalid item was attempted to be added."
            return [valid_input, add_invalid_item_res]

        check_inputs_result = [valid_input, "Valid input entered."]
        return check_inputs_result

    def add_entry(self, entry):

        valid_entry_checks = self.check_inputs(entry)

        if not valid_entry_checks:
            return valid_entry_checks

        sql_insert = "INSERT INTO {!s} VALUES ('{!s}', '{!s}', '{!s}');".format(entry[0], entry[1], entry[2], entry[3])
        self.db_cursor.execute(sql_insert)
        self.TiptabsDBConnector.commit()
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

        query = "SELECT username FROM users;"
        self.db_cursor.execute(query)
        for username in self.db_cursor:
            print("Current User: " + str(username))

        users = username
        all_users_result = [True, users]

        return all_users_result

