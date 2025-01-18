"""
Ce module contient la classe Item, qui représente les objets manipulables dans le jeu.
"""

class Item:
    """
    Représente un objet utilisable dans le jeu.

    Attributs :
        name (str) : Nom de l'objet.
        description (str) : Description de l'objet.
        weight (float) : Poids de l'objet.
    """

    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"- {self.name} : {self.description}, ({self.weight} kg)"

    def get_weight(self):
        """
        Retourne le poids de l'objet.

        :return: Poids de l'objet (float)
        """
        return self.weight

# Fin du fichier
