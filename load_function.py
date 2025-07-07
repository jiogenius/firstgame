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
    imageManager.imagemanager.preload_general_image("test.png", "test")
    imageManager.imagemanager.preload_animation_image("test2.png", 128,"test2")
    imageManager.imagemanager.preload_animation_image("image.png", 128, "image")
    print(f'images loaded in {time.time() - image_loading_start:.2f} seconds')