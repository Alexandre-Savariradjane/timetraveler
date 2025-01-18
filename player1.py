"""
Ce module contient la classe Player. 
Le joueur peut se déplacer dans différents lieux, 
interagir avec son inventaire, et répondre à des énigmes.
"""

class Player():
    """
    This class represents a Player. 
    A room is composed of a name, and a current location represented by the room where he is.

    Attributes:
        name (str): The name.
        current_room (bool) : The room where the player is currently located.

    Methods:
        __init__(self, name, description) : The constructor.
        move(self, direction): Moves the player to a room in the specified direction if possible.

    Examples:

    >>> from room import Room
    >>> room1 = Room("Forest", "dans une forêt enchantée. 
    Vous entendez une brise légère à travers la cime des arbres.")
    >>> room2 = Room("Cave", "dans une grotte profonde et sombre. 
    Des voix semblent provenir des profondeurs.")
    >>> room1.exits["N"] = room2
    >>> player = Player("Nom_de_la_personne")
    >>> player.current_room = room1
    >>> player.move("N")
    '\nVous êtes une cave.\n\nSorties: 'S'
    >>> player.current_room.name
    'Forest'
    >>> player.move("S")
    '\nAucune porte dans cette direction !\n'
    False
    
    """

    # Define the constructor.
    def __init__(self, name):
        """
    Initialise un nouveau joueur avec un nom et un objet de jeu.

    Parameters:
        name (str): Le nom du joueur.
        game (Game): L'objet représentant le jeu.
    """
    # code existant

        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.inventory_lieux = ()
        self.question_answered = False


    def get_history(self):
        """
        Affiche l'historique des pièces visitées par le joueur.
        Si l'historique est vide, un message l'indique.

        Exemple:
        >>> player.get_history()
        Vous avez déjà visité les pièces suivantes:
        - Forest
        """
        print("\nVous avez déjà visité les pièces suivantes:\n")
        for room in self.history:
            print('-' + room.name)
        if not self.history:
            print("\nVous n'avez visité aucune époque")

    # Define the move method.

    def move(self, direction):
        """
    Déplace le joueur dans la direction spécifiée, si possible.

    Parameters:
        direction (str): La direction dans laquelle le joueur souhaite se déplacer.

    Returns:
        None
    """
        if direction in self.current_room.exits:
            next_room = self.current_room.exits[direction]
            if next_room:
                self.current_room = next_room
                print(self.current_room.get_long_description())
                print(self.get_history())
                self.history.append(self.current_room)

            # Vérification de la condition de victoire
                if self.current_room.name == "Future":

                    # Attente de la réponse du joueur
                    answer = input("Que choisissez-vous ? go 1, go 2, go 3\n").strip()

                    # Vérification de la réponse
                    if answer == "go 1" and "machine_enigma" in self.inventory:
                        print("\nVous avez répondu correctement ! Vous avez gagné ! 🎉")
                        self.game.victory = True
                        self.game.finished = True
                    elif answer == "go 1":
                        print("\nVous avez répondu correctement.")
                        print("\nMais vous n'avez pas la machine Enigma.")
                        self.game.victory = False
                        self.game.finished = False

                    elif answer == "go 2":
                    # Envoyer le joueur vers la salle correspondante à "2"
                        print("\nMauvaise réponse.")
                        print("\nVous êtes envoyé dans une autre époque.")
                        self.current_room = self.current_room.exits.get("2")
                        print(self.current_room.get_long_description())
                        self.game.victory = False
                        self.game.finished = False

                    elif answer == "go 3":
                    # Envoyer le joueur vers la salle correspondante à "2"
                        print("\nMauvaise réponse.")
                        print("\nVous êtes envoyé dans une autre pièce.")
                        self.current_room = self.current_room.exits.get("3")
                        print(self.current_room.get_long_description())
                        self.game.victory = False
                        self.game.finished = False
                    self.question_answered = True  # Marquer la question comme répondue

                elif self.current_room.name.endswith("_apocalyptic"):
                    if direction == "1":
                        print("\nVous avez échoué, c'est la fin du jeu...")
                        self.game.defeat = True
                        self.game.finished = True
                        return

        else:
            print("Il n'y a rien dans cette direction.")

    # Define the inventory method.

    def get_inventory(self):
        """
    Affiche l'inventaire du joueur. Si l'inventaire est vide, un message le signale.

    Exemple:
        >>> player.get_inventory()
        Vous disposez des items suivants :
        - Sword
        """
        if not self.inventory:  # Vérifier si l'inventaire est vide
            print("\nVotre inventaire est vide.")

        else:
            print("\nVous disposez des items suivants :")  # Parcourir les items du dictionnaire
            for item in self.inventory.values():
                print(f"{item}")  # Utilise la méthode __str__() définie dans la classe Item

    def get_inventory_lieux(self):
        """
    Affiche les objets présents dans la pièce actuelle. Si la pièce est vide, un message le signale.

    Exemple:
        >>> player.get_inventory_lieux()
        La pièce contient:
        - Key
        """
        if not self.inventory:  # Vérifier si l'inventaire est vide
            print("\nIl n'y a rien ici.")

        else:
            print("\nLa pièce contient:")  # Parcourir les items du dictionnaire
            for item in self.inventory.values():
                print(f" -{item}")  # Utilise la méthode __str__() définie dans la classe Item
# Fin du fichier
