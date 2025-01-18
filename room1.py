"""
Ce module contient la classe Room, qui représente une pièce dans un jeu d'aventure.
La classe permet de définir des pièces avec des descriptions,
des sorties et des objets à l'intérieur.
"""


class Room:
    """
    This class represents a room. A room is composed of a name, an exit and a description.

    Attributes:
        name (str): The name.
        description (str) : A quick description of the room.
        exit (dict): A dictionary mapping directions (str) to adjacent Room instances


    Methods:
        __init__(self, name, description) : The constructor.
        get_exit(self, direction): Returns the room connected in the given direction if it exists,
        otherwise None.
        get_exit_string(self): Returns a formatted string describing the available exits.
        get_long_description(self): Returns a long description of the room, including its exits.


    Examples:

    >>> room = Room("Forest", "dans une forêt enchantée.
    Vous entendez une brise légère à travers la cime des arbres.")
    >>> room.name
    'Forest'
    >>> room.description
    'dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.'
    >>> room.exits
    {}
    >>> room.exits["N"] = Room("Cave",
    "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
    >>> room.get_exit("N").name
    'Cave'
    >>> room.get_exit_string()
    'Sorties: N'
    >>> print(room.get_long_description())
    '\nVous dans une forêt enchantée.
    Vous entendez une brise légère à travers la cime des arbres.\n\nSorties: N\n'
    """

    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.inventory_lieux = set()
        self.inventory = {}
        self.characters = {}
        self.question = ""
        self.reponse = {}

    # Define the get_exit method.
    def get_exit(self, direction):
        """
    Retourne la salle dans la direction spécifiée si elle existe, sinon None.

    Parameters:
        direction (str): La direction dans laquelle le joueur veut se déplacer.

    Returns:
        Room | None: La salle connectée ou None si la direction n'existe pas.
        """
        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]

        return None

    # Return a string describing the room's exits.
    def get_exit_string(self):
        """
    Retourne une chaîne formatée décrivant les sorties disponibles.

    Returns:
        str: Une chaîne indiquant les directions possibles à prendre.
        """
        exit_string = "Que choisissez-vous ?"
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        """
    Retourne une description complète de la pièce, y compris les sorties disponibles.

    Returns:
        str: La description complète de la pièce et ses sorties.
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        """
        Retourne l'inventaire du joueur
        """
        if not self.inventory:  # Vérifier si l'inventaire est vide
            print("\nIl n'y a rien ici.")

        else:
            print("\nLa pièce contient:")  # Parcourir les items du dictionnaire
            for item in self.inventory.values():
                print(f" -{item}")  # Utilise la méthode __str__() définie dans la classe Item

    def get_inventory_lieux(self):
        """
        Retourne l'inventaire de la pièce
        """
        if not self.inventory_lieux:  # Vérifier si l'inventaire est vide
            print("\nIl n'y a rien ici.")

        else:
            print("\nOn voit:")  # Parcourir les items du dictionnaire
            for item in self.inventory_lieux:
                print(f" -{item}")  # Utilise la méthode __str__() définie dans la classe Item
            for characters in self.characters.values():
                print (f" -{characters.name}, {characters.description}")

    def add_character(self, character):
        """
        Pour ajouter des pnj à la pièce
        """
        self.characters[character.name] = character

    def remove_character(self, character_name):
        """
    Supprime un personnage non-joueur (PNJ) de la pièce.

    Parameters:
        character_name (str): Le nom du PNJ à supprimer.
        """
        if character_name in self.characters:
            del self.characters[character_name]
