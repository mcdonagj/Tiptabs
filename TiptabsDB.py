import mysql.connector


class TiptabsDB:

    def __init__(self):

        self.TiptabsDBConnector = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="root"
        )

        self.db_cursor = self.TiptabsDBConnector.cursor()

        self._initDB()

    def _initDB(self):
        commands = ["DROP DATABASE IF EXISTS tiptabs_db;", "CREATE DATABASE IF NOT EXISTS tiptabs_db;",
                    "USE tiptabs_db;",
                    "CREATE TABLE users (username VARCHAR(20), password VARCHAR(20), favorite_conversions VARCHAR(35));"]

        for command in commands:
            self._get_cursor().execute(command)

    def _get_cursor(self):
        return self.db_cursor

    def _get_connector(self):
        return self.TiptabsDBConnector

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
        self._get_cursor().execute(sql_insert)
        self._get_connector().commit()
        add_entry_result = [True, "Item was added successfully to the Database."]

        return add_entry_result

    def remove_entry(self, entry):
        remove_entry_result = [True, "Item was removed successfully from the Database."]
        return remove_entry_result

    def retrieve_user_favorites(self, entry):

        valid_entry_checks = self.check_inputs(entry)

        if not valid_entry_checks:
            return valid_entry_checks

        query = "SELECT favorite_conversions FROM {!s} WHERE username='{!s}';".format(entry[0], entry[1])

        self._get_cursor().execute(query)
        rows = self._get_cursor().fetchall()

        retrieve_entry_result = [True, rows]
        return retrieve_entry_result

    def get_all_users(self):

        query = "SELECT username FROM users;"
        self._get_cursor().execute(query)

        # Returns a list of all users.
        rows = self._get_cursor().fetchall()

        all_users_result = [True, rows]

        return all_users_result

