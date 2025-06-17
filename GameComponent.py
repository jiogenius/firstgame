import pygame
import os

mainFolderPath = os.path.dirname(os.path.abspath(__file__))
assetPath=os.path.join(mainFolderPath,"asset")

class GameObject:
    def __init__(self,Pos):
        self.Pos = Pos
        self.default_image = pygame.image.load(os.path.join(assetPath, "test.png"))
        self.speed = [0,0]

    def setPos(self,Pos):
        self.Pos = Pos

    def move(self,Pos):
        self.Pos = [self.Pos[0]+Pos[0],self.Pos[1]+Pos[1]]


class Entity(GameObject):
    pass

class Block(GameObject):
    pass