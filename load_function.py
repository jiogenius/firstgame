import imageManager
import time

def load():
    image_loading_start = time.time()
    print("loading images...")
    imageManager.imagemanager.preload_general_image("test.png", "test")
    imageManager.imagemanager.preload_animation_image("test2.png", 128,"test2")
    imageManager.imagemanager.preload_animation_image("image.png", 128, "image")
    print(f'images loaded in {time.time() - image_loading_start:.2f} seconds')