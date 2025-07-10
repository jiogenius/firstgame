import GameComponent
import animation

class testEntity(GameComponent.Entity):
    def __init__(self, Pos: list | tuple):
        super().__init__(Pos)
        self.assets = [animation.Animation("test2", 10)]  # 애니메이션 객체를 assets에 추가

