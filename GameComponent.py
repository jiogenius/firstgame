import pygame
import os
import animation
import imageManager

mainFolderPath = os.path.dirname(os.path.abspath(__file__))
assetPath=os.path.join(mainFolderPath,"asset")

class GameObject:
    def __init__(self,Pos: list | tuple):
        self.Pos = Pos # Position of the object
        self.defaultImage = "test" # Default image of the object

    def setPos(self,Pos: list | tuple):
        self.Pos = Pos # Reposition the object

    def move(self,Pos: list | tuple):
        self.Pos = [self.Pos[0]+Pos[0],self.Pos[1]+Pos[1]] # Move the object by a certain amount

    def frame(self):
        pass

class Entity(GameObject):
    def __init__(self, Pos:list | tuple):
        super().__init__(Pos)
        self.speed = [0,0]# Speed of the entity
        self.assets = [] #animation and image
        self.status = {} #{}<-other property
        self.assetNumber = 0# Current asset number
        self.friction = 0#  # Friction applied to the entity's speed
    def frame(self):
        self.AI()# AI function to control the entity's behavior
        #print(f"speed {self.speed}")
        # Apply friction to the entity's speed
        if self.speed[0] < 0:
            self.speed[0]+=self.friction
        if self.speed[0] > 0:
            self.speed[0]-=self.friction
        if self.speed[1] < 0:
            self.speed[1]+=self.friction
        if self.speed[1] > 0:
            self.speed[1]-=self.friction
        if abs(self.speed[0]) < self.friction:
            self.speed[0] = 0
        if abs(self.speed[1]) < self.friction:
            self.speed[1] = 0
        if type(self.assets[self.assetNumber]) == animation.Animation:
            self.assets[self.assetNumber].next()
        # Move the entity by its speed
        self.move(self.speed)
        #print(f"Pos {self.Pos} speed {self.speed}")
        
    def AI(self):
        pass
    
    def set_current_animation(self, assetNumber: int):
        self.assetNumber = assetNumber

    def get_current_image(self):
        if type(self.assets[self.assetNumber]) == animation.Animation:
            return self.assets[self.assetNumber].get_current_image()
        else:
            return imageManager.imagemanager.get_image(self.assets[self.assetNumber])

    def push(self, speed: list | tuple):
        self.speed = [self.speed[0] + speed[0] + self.friction, self.speed[1] + speed[1] + self.friction]
        print(f"push speed {self.speed} Pos {self.Pos} friction {self.friction}")
class Block(GameObject):
    pass

