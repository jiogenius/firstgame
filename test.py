import setting
import os

mainFolderPath = os.path.dirname(os.path.abspath(__file__))

a = setting.Setting(mainFolderPath)
print(a.get("playerSetting")["a"])