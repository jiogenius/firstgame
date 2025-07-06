import json
import os
import utility_functions

class Setting:
    def __init__(self, mainFolderPath):
        self.setting_path = os.path.join(mainFolderPath, "setting/")
        self.settings = {}
        file_json = utility_functions.easy_jsonLoad(os.path.join(self.setting_path, "file.json"))
        for i in file_json:
            self.settings[i["name"]] = utility_functions.easy_jsonLoad(i["path"])

    def save(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save()