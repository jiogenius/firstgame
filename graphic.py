import GameComponent
import animation
import pygame
import os
class cam:
    def __init__(self, Pos, name):
        self.Pos = Pos
        self.name = name

    def setPos(self, Pos):
        self.Pos = Pos

    def move(self, Pos):
        self.Pos = [self.Pos[0] + Pos[0], self.Pos[1] + Pos[1]]

    def draw_image(self, screen, toDraw, Pos):
        DrawPos = [self.Pos[0] - Pos[0], self.Pos[1] - Pos[1]]
        screen.blit(toDraw, (DrawPos[0],DrawPos[1]))

    def draw(self, screen, object):
        if type(object)==animation.animation:
            self.draw_image(screen, object.get_current_image(), [0,0])
        #if type(object)==GameComponent.Entity:
            #TODO:Entity클레스 만들기
        #    self.draw_image(screen,object.get_current_image(), self.Pos)
        #elif type(object)==GameComponent.Block:
            #TODO:Block클레스 만들기
        #    self.draw_image(screen,object.get_current_image(), self.Pos)
        #else:
        #    raise TypeError

    def ScreenClickPos_to_WorldClickPos(self, ScreenClickPos):
        WorldClickPos = [ScreenClickPos[0] + self.Pos[0], ScreenClickPos[1] + self.Pos[1]]
        return WorldClickPos
class imageManager:
    def __init__(self, assetPath):
        self.assetPath = assetPath
        self.imageCache = {"animation":{}, "image":{}}

    def preload_general_image(self, filename, name=None):
        if name is None:
            name = filename
        self.imageCache["image"][name] = pygame.image.load(os.path.join(self.assetPath, filename))
    def preload_animation_image(self, filename, name=None):
        if name is None:
            name = filename
        self.imageCache["animation"][name] = pygame.image.load(os.path.join(self.assetPath, filename))
    def get_image(self, name, type=1):
        if type == 1:
            return self.imageCache["image"].get(name, None)
        elif type == 2:
            return self.imageCache["animation"].get(name, None)
        else:
            raise ValueError("Unknown type: {}".format(type))
