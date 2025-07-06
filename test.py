import random
seedlist = ['apple','Sugar_apple','Sunflower','Ember_lily']
class garden:
    def __init__(self, seed):
        self.stock = seed
    def restock(self):
        print(self.stock)
    def power_of_robux(self):
        
ike = garden(seedlist[random.randint(0,3)])
ike.restock()