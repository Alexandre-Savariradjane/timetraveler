"""
Ce module contient la classe Inventory, qui gère l'inventaire des objets dans le jeu.
"""

class Inventory:
    """
    Gère l'inventaire des objets d'un joueur ou d'un lieu dans le jeu.

    Attributs :
        items (set) : Ensemble des objets présents dans l'inventaire.
    """

    def __init__(self):
        self.items = set()  # Utilisation d'un set

    def add_item(self, item):
        """
        Ajoute un objet à l'inventaire.

        :param item: L'objet à ajouter.
        """
        self.items.add(item)

    def get_inventory(self):
        """
        Ajoute un objet à l'inventaire.

        :param item: L'objet à ajouter.
        """
        if not self.items:
            print("Il n'y a rien ici.")
        else:
            print("Les objets présents sont :")
            for item in self.items:
                print(f"    - {item}")
# Fin du fichier
