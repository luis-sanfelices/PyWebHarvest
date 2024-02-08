import os
import json

class JsonLoader:
    """
    A class for loading data into a JSON file.
    """

    def __init__(self, path, file_name, load_mode="w", **load_options):
        """
        Initialize JsonLoader.

        :param path: path where file will be stored 
        :param file_name: The file where data will be loaded.
        :param load_mode: The mode for opening the file. Default is 'w' (open for writing, truncating the file first).
        :param file_options: Additional options for opening the file.
        :param json_options: Additional options for JSON serialization.
        """
        self.path = path
        self.file_name = file_name
        self.load_mode = load_mode
        self.file_options = load_options.get("file_options", {})
        self.json_options = load_options.get("json_options", {})

    def load(self, data: dict):
        """
        Load data into the JSON file.

        :param data: The data to be loaded into the JSON file.
        :raises Exception: If an error occurs during loading.
        """
        try:
            file_path = os.path.join(self.path,self.file_name)
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            with open(file_path, self.load_mode, **self.file_options) as outfile:
                json.dump(data, outfile, **self.json_options)
            return file_path
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File '{self.file_name}' not found.") from e
        except PermissionError as e:
            raise PermissionError(f"No permission to write to file '{self.file_name}'.") from e
        except Exception as e:
            raise Exception(f"Something went wrong when loading data into JSON file {self.file_name}") from e
