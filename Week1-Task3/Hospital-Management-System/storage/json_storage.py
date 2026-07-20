import json
import os


class JsonStorage:

    @staticmethod
    def save(filename, data):

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    @staticmethod
    def load(filename):

        if not os.path.exists(filename):
            return []

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)