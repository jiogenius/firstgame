import pygame
import os

mainFolderPath = os.path.dirname(os.path.abspath(__file__))
assetPath=os.path.join(mainFolderPath,"asset")

class GameObject:
    def __init__(self,Pos):
        self.Pos = Pos
        self.default_image = pygame.image.load(os.path.join(assetPath, "test.png"))

    def setPos(self,Pos):
        self.Pos = Pos

    def move(self,Pos):
        self.Pos = [self.Pos[0]+Pos[0],self.Pos[1]+Pos[1]]

    def frame(self):
        pass

class Entity(GameObject):
    def __init__(self, Pos):
        super().__init__(Pos)
        self.speed = []
        self.animations = []
        self.status = [0,{}] #[0<--health,{}<-other property]
    def frame(self):
        self.move


class Block(GameObject):
    pass