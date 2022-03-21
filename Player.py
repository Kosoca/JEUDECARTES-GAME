class Player():

    def __init__(self, JeuDeCartes):
        self.playerPoint = 0
        self.playerDeck = JeuDeCartes

    def getDeck(self):
        return self.playerDeck

    def getPoints(self):
        return self.playerPoint

    def addPoint(self):
        self.playerPoint = self.playerPoint + 1
        return self.getPoints()

    def removePoint(self):
        self.playerPoint = self.playerPoint - 1
        return self.getPoints()
