import GameComponent
import animation
import pygame
import setting

import os
class cam:
    def __init__(self, Pos, name):
        self.Rect = pygame.Rect(Pos[0], Pos[1], 1000, 800)
        self.name = name
        self.min_zoom = setting.setting.get("cameraSetting")["minZoom"]
        self.max_zoom = setting.setting.get("cameraSetting")["maxZoom"]
        self.base_width = 1000
        self.base_height = 800
        self.surface = pygame.Surface((2000, 1600))  # Assuming a large surface for the camera view
        self.zoom = 1.0  # Default zoom level
    def setPos(self, Pos):
        self.Rect.x = Pos[0]
        self.Rect.y = Pos[1]

    def move(self, Pos):
        self.Rect.x = self.Rect.x + Pos[0]
        self.Rect.y = self.Rect.y + Pos[1]

    def draw_image(self, toDraw, Pos):
        DrawPos = [Pos[0] - self.Rect.x,Pos[1] - self.Rect.y]

        if DrawPos[0] > 2000 or DrawPos[1] > 1600 or DrawPos[0] < 0 or DrawPos[1] < 0:
            return
        else:
            self.surface.blit(toDraw, DrawPos)
    def draw(self, object):
        if type(object)==animation.Animation:
            self.draw_image(object.get_current_image(), [0,0])
        elif type(object)==GameComponent.Entity:
            self.draw_image(object.get_current_image(), object.Pos)
        else:
            raise TypeError

    def Zoom(self, zoomDelta):
        prev_center = self.Rect.center  # 줌 전에 중심 기억

        # 줌 비율 조정
        self.zoom += zoomDelta
        self.zoom = max(self.min_zoom, min(self.max_zoom, self.zoom))

        # ✅ 원본 크기에 비례한 새로운 크기 계산
        new_width = int(self.base_width / self.zoom)
        new_height = int(self.base_height / self.zoom)

        # ✅ 중심을 기준으로 크기 재설정
        self.Rect.width = new_width
        self.Rect.height = new_height
        self.Rect.center = prev_center
    def drawToScreen(self,screen):
        surface_rect = self.surface.get_rect()
        cuttingRect = pygame.Rect(self.Rect.x, self.Rect.y, self.Rect.width, self.Rect.height)
        cuttingRect = cuttingRect.clip(surface_rect)  # 안전하게 클립

        if cuttingRect.width == 0 or cuttingRect.height == 0:
            return  # 화면에 보일 것이 없음

        visible_surface = self.surface.subsurface(cuttingRect)
        resized_surface = pygame.transform.scale(visible_surface, screen.get_size())
        screen.blit(resized_surface, (0, 0))

   #def ScreenClickPos_to_WorldClickPos(self, ScreenClickPos):
   #     WorldClickPos = [ScreenClickPos[0] + self.Pos[0], ScreenClickPos[1] + self.Pos[1]]
   #     return WorldClickPos

