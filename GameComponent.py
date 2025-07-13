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
        self.mexSpeed = 1000 # Maximum speed of the entity
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
        # AI logic for the entity (used when subclassed)
        pass
    
    def set_current_animation(self, assetNumber: int):
        self.assetNumber = assetNumber # Set the current asset number to the specified one

    def get_current_image(self):
        # Return the current image of the entity based on the asset number
        if type(self.assets[self.assetNumber]) == animation.Animation:
            return self.assets[self.assetNumber].get_current_image()
        else:
            return imageManager.imagemanager.get_image(self.assets[self.assetNumber])

    def push(self, speed: list | tuple):
        # Push the entity with a certain speed
        if speed[0] > 0:
            self.speed[0] = self.speed[0] + speed[0] + self.friction
        elif speed[0] < 0:
            self.speed[0] = self.speed[0] + speed[0] - self.friction
        if speed[1] > 0:
            self.speed[1] = self.speed[1] + speed[1] + self.friction
        elif speed[1] < 0:
            self.speed[1] = self.speed[1] + speed[1] - self.friction
        # Limit the speed to the maximum speed
        self.speed[0] = max(-self.mexSpeed, min(self.mexSpeed, self.speed[0]))
        self.speed[1] = max(-self.mexSpeed, min(self.mexSpeed, self.speed[1]))
        #print(f"push speed {self.speed} Pos {self.Pos} friction {self.friction}")
class Block(GameObject):
    pass

class Item:
    def __init__(self, asset: str|animation.Animation, amount: int):
        self.asset = asset
        self.amount = amount

    def get_current_image(self):
        if type(self.asset) == animation.Animation:
            return self.asset.get_current_image()
        else:
            return imageManager.imagemanager.get_image(self.asset)

    def frame(self):
        if type(self.asset) == str:
            pass
        else:
            self.asset.next()

        #add any additional logic for the item here when subclassed


