import pygame
import imageManager
class Animation:
    def __init__(self,image,interval):
        self.interval=interval
        self.cin=0 #cin:current image number
        self.curser=0
        self.image=image
    def next(self):
        self.curser+=1
        self.cin=self.curser//self.interval
        if self.cin>=len(imageManager.imagemanager.get_image(self.image,2)):
            self.cin=0
            self.curser=0

    def get_current_image(self):
        return imageManager.imagemanager.get_image(self.image,2)[self.cin]
