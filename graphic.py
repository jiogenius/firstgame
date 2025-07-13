import GameComponent
import animation
import pygame
import setting

import os
class cam:
    def __init__(self, Pos :list | tuple):
        # Initialize camera position and settings
        self.Rect = pygame.Rect(4200, 4550, 1600, 900)
        self.min_zoom = setting.setting.get("cameraSetting")["minZoom"] # Minimum zoom level
        self.max_zoom = setting.setting.get("cameraSetting")["maxZoom"] # Maximum zoom level
        self.base_width = 1600 #Default base size of the camera view
        self.base_height = 900
        self.surface = pygame.Surface((10000, 10000))  # Assuming a large surface for the camera view
        self.surfacePos = Pos # Camera position in the world
        self.zoom = 1.0  # Default zoom level
    def setPos(self, Pos: list | tuple):
        self.surfacePos = Pos

    def move(self, Pos: list | tuple):
        self.surfacePos[0] += Pos[0]
        self.surfacePos[1] += Pos[1]

    def draw_image(self, toDraw, Pos: list | tuple):
        DrawPos = [Pos[0] - self.surfacePos[0],Pos[1] - self.surfacePos[1]]
        #print(f"Calculated DrawPos: {DrawPos}x:{self.Rect.x} y:{self.Rect.y} zoom:{self.zoom} width:{self.Rect.width} height:{self.Rect.height}Drawing image at {Pos} with surface position {self.surfacePos}")

        if DrawPos[0] > 10000 or DrawPos[1] > 10000 or DrawPos[0] < 0 or DrawPos[1] < 0:
            return
        else:
            self.surface.blit(toDraw, DrawPos)
    def draw(self, object):
        if issubclass(type(object), animation.Animation):
            self.draw_image(object.get_current_image(), [0,0])
        elif issubclass(type(object), GameComponent.Entity):
            self.draw_image(object.get_current_image(), object.Pos)
        else:
            raise TypeError

    def Zoom(self, zoomDelta: float| int):

        self.zoom += zoomDelta
        self.zoom = max(self.min_zoom, min(self.max_zoom, self.zoom))
        self.Rect.width = int(self.base_width / self.zoom)
        self.Rect.height = int(self.base_height / self.zoom)
        self.Rect.x = int((10000-self.Rect.width) // 2)
        self.Rect.y = int((10000-self.Rect.height) // 2)

    def drawToScreen(self,screen):
        cuttedSurface = self.surface.subsurface(self.Rect)
        scaledSurface = pygame.transform.scale(cuttedSurface, screen.get_size())
        screen.blit(scaledSurface, (0, 0))


   #def ScreenClickPos_to_WorldClickPos(self, ScreenClickPos):
   #     WorldClickPos = [ScreenClickPos[0] + self.Pos[0], ScreenClickPos[1] + self.Pos[1]]
   #     return WorldClickPos

