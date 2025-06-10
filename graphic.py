class cam:
    def __init__(self, Pos, name):
        self.Pos = Pos
        self.name = name

    def setPos(self, Pos):
        self.Pos = Pos

    def move(self, Pos):
        self.Pos = [self.Pos[0] + Pos[0], self.Pos[1] + Pos[1]]

    def draw(self, screen, toDraw, Pos):
        DrawPos = [self.Pos[0] - Pos[0], self.Pos[1] - Pos[1]]
        screen.draw(toDraw, DrawPos)

    def ScreenClickPos_to_WorldClickPos(self, ScreenClickPos):
        WorldClickPos = [ScreenClickPos[0] + self.Pos[0], ScreenClickPos[1] + self.Pos[1]]
        return WorldClickPos
