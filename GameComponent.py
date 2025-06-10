class GameObject:
    def __init__(self,Pos,image):
        self.Pos = Pos
        self.image = image
        self.speed = [0,0]

    def setPos(self,Pos):
        self.Pos = Pos

    def move(self,Pos):
        self.Pos = [self.Pos[0]+Pos[0],self.Pos[1]+Pos[1]]

    def Acceleration(self,speed):
        speed