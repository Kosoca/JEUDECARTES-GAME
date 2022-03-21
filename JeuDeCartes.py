# Coeur 3
# Carreau 2
# Trèfle 1
# Pique 0
# 13
import random


class JeuDeCartes():

    def __init__(self):
        self.colorCard = 0
        self.cardsGame = []
        self.colorCards = ("de Coeur", "de Carreau", "de Trèfle", "de Pique")
        self.nameCards = ("Valet", "Dame", "Roi", "As")

        for index in range(1, 53):
            if index <= 13:
                colorCard = 0
                self.cardsGame.append((index+1, colorCard))
            elif index <= 26:
                colorCard = 1
                self.cardsGame.append(((index+1)-13, colorCard))
            elif index <= 39:
                colorCard = 2
                self.cardsGame.append(((index+1)-26, colorCard))
            elif index <= 52:
                colorCard = 3
                self.cardsGame.append(((index+1)-39, colorCard))

    def getCardsGame(self):
        return self.cardsGame

    def nom_carte(self, card):
        result = ""
        for cardValue in self.cardsGame:
            if cardValue == card:
                continue
            else:
                break
            pass
        pass

        if card[0] == 14:
            result = result + self.nameCards[3]
            pass
        elif card[0] == 13:
            result = result + self.nameCards[2]
            pass
        elif card[0] == 12:
            result = result + self.nameCards[1]
            pass
        elif card[0] == 11:
            result = result + self.nameCards[0]
            pass
        else:
            result = result + str(card[0])
            pass

        if card[1] == 0:
            result = result + " " + self.colorCards[0]
            pass
        elif card[1] == 1:
            result = result + " " + self.colorCards[1]
            pass
        elif card[1] == 2:
            result = result + " " + self.colorCards[2]
            pass
        elif card[1] == 3:
            result = result + " " + self.colorCards[3]
            pass

        return result

    def battre(self):
        random.shuffle(self.cardsGame)
        return self.cardsGame

    def tirer(self):
        if len(self.cardsGame) == 0:
            return None
        else:
            return self.cardsGame.pop(0)
