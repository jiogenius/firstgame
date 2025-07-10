import pygame

import GameComponent
import animation

class testEntity(GameComponent.Entity):
    def __init__(self, Pos: list | tuple):
        super().__init__(Pos)
        self.assets = [animation.Animation("test2", 10), "test"]  # 애니메이션 객체를 assets에 추가
        self.friction = 10

    def AI(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.push([0, -10])
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.push([0, 10])
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.push([10, 0])
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.push([-10, 0])

    def frame(self):
        super().frame()

