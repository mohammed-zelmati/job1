#-Class Pizza ============
class Pizza:
    def __init__(self, base, prix, diametre, style, ingredients):
        self.base = base
        self.prix = prix 
        self.diametre = diametre
        self.style = style
        self.ingredients = ingredients

    def ajouter_ingredients(self, nouvel_ingredient):
        self.ingredients.append(nouvel_ingredient)
        self.prix += 1

    def servir(self, table):
        print("Je sers la pizza a la table", table)

    def livrer(self, adresse):
        print("Je livre la pizza a l'addresse", adresse)

pizza = Pizza("Tomate", 9, 30, "Classique", ["Ail", "Olives", "Champignons", "Aubergines"])

pizza.ajouter_ingredients("Poivrons")
pizza.servir(2)
pizza.servir("Rue du bois 13")

print(pizza.ingredients)

#-Class Cybertruck  ============
class Cybertruck:
    marque = "Tesla"
    modele = "Cybertruck"
    annee = 2023

    def klaxonner(self):
        print("Tut tut !")

#-Class Voiture ============
class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def klaxonner(self):
        print("Tut tut !")