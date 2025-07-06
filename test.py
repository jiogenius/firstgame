import random
seedlist = ['apple','Sugar_apple','Sunflower','Ember_lily']
class garden:
    def __init__(self, seed):
        self.stock = seed
    def restock(self):
        print(self.stock)

ike = garden(seedlist[random.randint(0,3)])
ike.restock()