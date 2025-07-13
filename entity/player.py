import GameComponent
import setting
import animation
import pygame

class Player(GameComponent.Entity):
    def __init__(self, Pos: list | tuple):
        super().__init__(Pos)
        self.assets = [animation.Animation("entity/player/walkingDown", 10)]  # Animation and idle image
        self.friction = setting.setting.get("playerSetting")["friction"]
        self.mexSpeed = setting.setting.get("playerSetting")["maxSpeed"]

    def AI(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.push([0, -self.mexSpeed])
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.push([0, self.mexSpeed])
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.push([self.mexSpeed, 0])
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.push([-self.mexSpeed, 0])