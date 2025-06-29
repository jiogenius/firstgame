import pygame
import os
mainFolderPath = os.path.dirname(os.path.abspath(__file__))
assetPath=os.path.join(mainFolderPath,"asset")
class ImageManager:
    def __init__(self, assetPath):
        self.assetPath = assetPath
        self.imageCache = {"animation":{}, "image":{}}

    def preload_general_image(self, filename, name=None):
        if name is None:
            name = filename
        self.imageCache["image"][name] = pygame.image.load(os.path.join(self.assetPath, filename))
    def preload_animation_image(self, filename, height, name=None):
        images = []
        image= pygame.image.load(os.path.join(self.assetPath, filename))
        print(range(0, image.get_width(), height))
        for i in range(0, image.get_height(), height):
            print(0.0, float(i), float(image.get_width()), float(height))
            tmp_image = image.subsurface(pygame.Rect(0.0, float(i), float(image.get_width()), float(height)))
            images.append(tmp_image)
        if name is None:
            name = filename
        self.imageCache["animation"][name] = images
    def get_image(self, name, type=1):
        if type == 1:
            return self.imageCache["image"].get(name, None)
        elif type == 2:
            return self.imageCache["animation"].get(name, None)
        else:
            raise ValueError("Unknown type: {}".format(type))

imagemanager = ImageManager(assetPath)
