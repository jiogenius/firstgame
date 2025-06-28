import pygame
class animation:
    def __init__(self,image,height,interval):
        self.interval=interval
        self.cin=0 #cin:current image number
        self.curser=0
        self.images =[]
        self.height=height
        print(range(0,image.get_width(),height))
        for i in range(0,image.get_height(),height):
            print(0.0, float(i), float(image.get_width()),float(height))
            tmp_image=image.subsurface(pygame.Rect(0.0, float(i), float(image.get_width()),float(height)))
            self.images.append(tmp_image)
    def next(self):
        self.curser+=1
        self.cin=self.curser//self.interval
        if self.cin>=len(self.images):
            self.cin=0
            self.curser=0
    def get_current_image(self):
        return self.images[self.cin]
