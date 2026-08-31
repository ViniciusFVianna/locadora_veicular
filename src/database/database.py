import json
import os

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.data = self.load_data()

    @staticmethod
    def load_data(self):
        path = f"src/database/{self.db_file}.json"
        if os.path.exists(path):
            with open(path, 'r') as f:
                return json.load(f)
        else:
            return {}

    @staticmethod
    def save_data(self):
        path = f"src/database/{self.db_file}.json"
        with open(path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value
        self.save_data()

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save_data()