import json
from pathlib import Path


class KnowledgeBase:
    def __init__(self, data_files):
        self.data = {}

        for file_path in data_files:
            self._load_file(file_path)

    def _load_file(self, file_path):
        path = Path(file_path)

        with open(path, "r", encoding="utf-8") as file:
            self.data[path.stem] = json.load(file)

    def search(self, keyword):
        keyword = keyword.lower()
        results = []

        def contains_keyword(value):
            if isinstance(value, dict):
                return any(contains_keyword(v) for v in value.values())

            if isinstance(value, list):
                return any(contains_keyword(v) for v in value)

            return keyword in str(value).lower()

        def search_value(value, source=""):
            if isinstance(value, dict):
                # If this whole record matches, return the complete record
                if contains_keyword(value):
                    if "name" in value or "role" in value or "department" in value:
                        results.append({
                            "source": source,
                            "record": value
                        })
                        return

                for key, item in value.items():
                    search_value(item, source)

            elif isinstance(value, list):
                for item in value:
                    search_value(item, source)

        search_value(self.data)

        return results