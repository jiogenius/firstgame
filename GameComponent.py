import pygame
import os
import animation
import imageManager

mainFolderPath = os.path.dirname(os.path.abspath(__file__))
assetPath=os.path.join(mainFolderPath,"asset")

class GameObject:
    def __init__(self,Pos: list | tuple):
        self.Pos = Pos
        self.defaultImage = pygame.image.load(os.path.join(assetPath, "test.png"))

    def setPos(self,Pos: list | tuple):
        self.Pos = Pos

    def move(self,Pos: list | tuple):
        self.Pos = [self.Pos[0]+Pos[0],self.Pos[1]+Pos[1]]

    def frame(self):
        pass

class Entity(GameObject):
    def __init__(self, Pos:list | tuple):
        super().__init__(Pos)
        self.speed = []
        self.assets = [] #animation and image
        self.status = {} #{}<-other property
        self.assetNumber = 0
    def frame(self):
        friction = 0
        self.move(self.speed)
        if self.speed[0] < 0:
            self.speed[0]+=friction
        if self.speed[0] > 0:
            self.speed[0]-=friction
        if self.speed[1] < 0:
            self.speed[1]+=friction
        if self.speed[1] > 0:
            self.speed[1]-=friction
        if abs(self.speed[0]) < friction:
            self.speed[0] = 0
        if abs(self.speed[1]) < friction:
            self.speed[1] = 0
        if type(self.assets[self.assetNumber]) == animation.Animation:
            self.assets[self.assetNumber].frame()
        self.AI()
        
    def AI(self):
        pass
    
    def set_current_animation(self, assetNumber: int):
        self.assetNumber = assetNumber

    def get_current_image(self):
        if type(imageManager.imagemanager.get_image(self.assets[self.assetNumber])) == animation.Animation:
            return imageManager.imagemanager.get_image(self.assets[self.assetNumber]).get_current_image()
        else:
            return imageManager.imagemanager.get_image(self.assets[self.assetNumber])
class Block(GameObject):
    pass

