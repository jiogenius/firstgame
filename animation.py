import pygame
class animation:
    def __init__(self,image,width):
        self.images =[]
        for i in range(0,image.get_width()+width,width):
            tmp_image=image.subsurface(pygame.Rect(i, 0, width, image.get_height))
            self.images.append(tmp_image)


