# Define the Room class.

class Room:
    """
    This class represents a room. A room is composed of a name, an exit and a description.

    Attributes:
        name (str): The name.
        description (str) : A quick description of the room.
        exit (dict): A dictionary mapping directions (str) to adjacent Room instances


    Methods:
        __init__(self, name, description) : The constructor.
        get_exit(self, direction): Returns the room connected in the given direction if it exists, otherwise None.
        get_exit_string(self): Returns a formatted string describing the available exits.
        get_long_description(self): Returns a long description of the room, including its exits.


    Examples:

    >>> room = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
    >>> room.name
    'Forest'
    >>> room.description
    'dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.'
    >>> room.exits
    {}
    >>> room.exits["N"] = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
    >>> room.get_exit("N").name
    'Cave'
    >>> room.get_exit_string()
    'Sorties: N'
    >>> print(room.get_long_description())
    '\nVous dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.\n\nSorties: N\n'
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

    



    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
    
    def get_inventory(self):
        if not self.inventory:  # Vérifier si l'inventaire est vide
            print("\nIl n'y a rien ici.")
        
        else:
            print("\nLa pièce contient:")  # Parcourir les items du dictionnaire
            for item in self.inventory.values():
                print(f" -{item}")  # Utilise la méthode __str__() définie dans la classe Item

    def get_inventory_lieux(self):
        if not self.inventory_lieux:  # Vérifier si l'inventaire est vide
            print("\nIl n'y a rien ici.")
        
        else:
            print("\nOn voit:")  # Parcourir les items du dictionnaire
            for item in self.inventory_lieux:
                print(f" -{item}")  # Utilise la méthode __str__() définie dans la classe Item
            for characters in self.characters.values():
                print (f" -{characters.name}, {characters.description}")

        def add_character(self, character):
            self.characters[character.name] = character

    def remove_character(self, character_name):
        """
        Supprime un PNJ de la pièce.
        :param character_name: Nom du PNJ à supprimer
        """
        if character_name in self.characters:
            del self.characters[character_name]