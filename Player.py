class Player(object):
    def __init__(self):
        self.lumber = 0
        self.grain = 0
        self.ore = 0
        self.wool = 0
        self.brick = 0
        self.victoryPoints = 0
        self.devCards = 0
    
    def resources(self, dice):
        if dice == 2:
            self.brick += 1 
        elif dice == 3:
            self.brick += 1
            self.grain += 1
        elif dice == 4:
            self.lumber += 1
            self.brick += 1
        elif dice == 5:
            self.grain += 1
            self.ore += 1
        elif dice == 6:
            self.lumber += 1
            self.grain += 1
        elif dice == 8:
            self.ore += 1
            self.grain += 1
        elif dice == 9:
            self.wool += 2
        elif dice == 10:
            self.ore += 1
            self.wool += 1
        elif dice == 11:
            self.lumber +=1
            self.wool += 1
        elif dice == 12:
            self.lumber += 1
