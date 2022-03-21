from JeuDeCartes import JeuDeCartes
from Player import Player

player2 = Player(JeuDeCartes())
player1 = Player(JeuDeCartes())

player2.getDeck().battre()
player1.getDeck().battre()

print(player1.getDeck().getCardsGame())
print("=-----------------=")
print(player2.getDeck().getCardsGame())

nbEgalite = 0
print("=-----------------=")
for count in range(0, 52):
    tirageP1 = player1.getDeck().tirer()[0]
    tirageP2 = player2.getDeck().tirer()[0]
    if (tirageP1 == tirageP2):
        nbEgalite = nbEgalite + 1
        pass

    if (tirageP1 < tirageP2):
        player2.addPoint()
        print(tirageP1, tirageP2)
        pass
    else:
        player1.addPoint()
        print(tirageP1, tirageP2)
        pass
    pass

print(f"Joueur 1 : {player1.getPoints()} point(s)")
print(f"Joueur 2 : {player2.getPoints()} point(s)")
print(f"égalités : {nbEgalite}")
