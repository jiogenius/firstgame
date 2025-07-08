import imageManager
import time
import setting

def load():
    image_loading_start = time.time()
    print("loading images...")
    print(setting.setting.get("ImageLoad"))
    for i in setting.setting.get("ImageLoad"):
        print(i)
        print(f'preloading image:', i["name"])
        if i["type"] == 1:  # 일반 이미지
            imageManager.imagemanager.preload_general_image(i["path"], i["name"])
        elif i["type"] == 2:  # 애니메이션 이미지
            imageManager.imagemanager.preload_animation_image(i["path"], i["height"], i["name"])
    print(f'images loaded in {time.time() - image_loading_start:.2f} seconds')