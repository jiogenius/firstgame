import json
import os
import utility_functions

class Setting:
    def __init__(self, main_folder_path):
        self.setting_path = os.path.join(main_folder_path, "setting/")
        self.settings = {}
        self.load()
        self.main_file_path = os.path.join(self.setting_path, "settings.json")

    def load(self):
        file_names_json = utility_functions.easy_jsonLoad(os.path.join(self.setting_path, "file_names.json"))
        for i in file_names_json:
            self.settings[i] = utility_functions.easy_jsonLoad(i)
        try:
            with open(self.file_path, 'r') as file:
                self.settings = json.load(file)
        except FileNotFoundError:
            self.settings = {}
        except json.JSONDecodeError:
            print("Error decoding JSON from the settings file.")
            self.settings = {}

    def save(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save()