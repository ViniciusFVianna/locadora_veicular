import json
import os
from .json_datasource import JsonDataSource

class JsonDataSourceImpl(JsonDataSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save_data(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)