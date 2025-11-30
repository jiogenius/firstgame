import GameComponent
import setting
import animation
import pygame

class Player(GameComponent.Entity):
    def __init__(self, Pos: list | tuple):
        super().__init__(Pos)
        self.assets = [animation.Animation("entity/player/walkingDown", 10)]  # Animation and idle image
        self.friction = setting.setting.get("playerSetting")["friction"]
        self.maxSpeed = setting.setting.get("playerSetting")["maxSpeed"]
        self.acceleration = setting.setting.get("playerSetting")["acceleration"]

    def AI(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.push([0, -self.acceleration])
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.push([0, self.acceleration])
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.push([self.acceleration, 0])
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.push([-self.acceleration, 0])
    def frame(self):
        super().frame()
        print(self.speed)