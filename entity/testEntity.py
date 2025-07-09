import GameComponent

class testEntity(GameComponent.Entity):
    def __init__(self, Pos: list | tuple):
        super().__init__(Pos)
        self.assets = ["test2"]

