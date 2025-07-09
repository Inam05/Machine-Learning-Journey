import json
import os

class DataBase:
    def add_data(self, name, email, password):
        """Adds user data while ensuring db.json exists and is properly formatted."""
        # Ensure the file exists and is not empty
        if not os.path.exists("db.json") or os.stat("db.json").st_size == 0:
            with open("db.json", "w") as wf:
                json.dump({}, wf)  # Initialize an empty JSON object

        try:
            with open("db.json", "r") as rf:
                database = json.load(rf)  # Load existing data
        except json.JSONDecodeError:
            database = {}  # Reset if file is corrupted

        if email in database:
            return 0  # Email already registered
        else:
            database[email] = [name, password]
            with open("db.json", "w") as wf:
                json.dump(database, wf)  # Save updated data
            return 1  # Signup successful

    def search(self,email,password):

        with open('db.json','r') as rf:
            database = json.load(rf)
            if email in database:
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0
