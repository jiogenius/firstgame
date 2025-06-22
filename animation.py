import pygame
class animation:
    def __init__(self,image,width,interval):
        self.interval=interval
        self.cin=0 #cin:current image number
        self.curser=0
        self.images =[]
        self.width=width
        print(range(0,image.get_width(),width))
        for i in range(0,image.get_width(),width):
            print(float(i), 0.0, float(width),float(image.get_height()))
            tmp_image=image.subsurface(pygame.Rect(float(i), 0.0, float(width),float(image.get_height())))
            self.images.append(tmp_image)
    def next(self):
        self.curser+=1
        self.cin=self.curser//self.interval
        if self.cin>=len(self.images):
            self.cin=0
            self.curser=0
    def get_current_image(self):
        return self.images[self.cin]


