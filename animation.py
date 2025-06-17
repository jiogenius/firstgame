import pygame
class animation:
    def __init__(self,image,width,interval):
        self.interval=interval
        self.cin=0
        self.curser=0
        self.images =[]
        for i in range(0,image.get_width()+width,width):
            tmp_image=image.subsurface(pygame.Rect(i, 0, width, image.get_height))
            self.images.append(tmp_image)
    def next(self):
        self.curser+=1
        self.cin=self.curser//self.interval
    def get_curren_image(self):
        return self.images[self.cin]


