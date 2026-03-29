class Personnage:
    def __init__(self, nom, vie, attaque):
        self.nom = nom
        self.vie = vie
        self.attaque = attaque
    
    def attaquer(self, cible):
        cible.vie = cible.vie - self.attaque
        print(self.nom, "attaque", cible.nom)
        print(cible.nom, "n'as plus que", cible.vie, "PV.")

    def est_vivant(self):
        return self.vie > 0     #Renvoie True si vie > 0 sinon False

joueur = Personnage("Player 1", 100, 25)
ennemi = Personnage("Ennemi", 50, 10)

while joueur.est_vivant() and ennemi.est_vivant():
    joueur.attaquer(ennemi)

    if ennemi.est_vivant():
        ennemi.attaquer(joueur)

if joueur.est_vivant():
    print("Tu as gagné !")

else:
    print("Tu as perdu !")