import json
import os
import utility_functions

class Setting:
    def __init__(self, mainFolderPath):
        self.setting_path = os.path.join(mainFolderPath, "setting/")
        self.settings = {}
        file_json = utility_functions.easy_jsonLoad(os.path.join(self.setting_path, "file.json"))
        print("Loading settings from:", self.setting_path, "file.json:" , type(file_json))
        for item in file_json:
            print("Loading setting item:", item)
            item_path = os.path.join(self.setting_path, item.get("path", ""))
            self.settings[item["name"]] = utility_functions.easy_jsonLoad(item_path)

    def save(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save()

setting = Setting(os.path.dirname(os.path.abspath(__file__)))