# Define the Player class.
class Player():
    """
    This class represents a Player. A room is composed of a name, and a current location represented by the room where he is.

    Attributes:
        name (str): The name.
        current_room (bool) : The room where the player is currently located.

    Methods:
        __init__(self, name, description) : The constructor.
        move(self, direction): Moves the player to a room in the specified direction if possible.

    Examples:

    >>> from room import Room
    >>> room1 = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
    >>> room2 = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
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
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.inventory_lieux = ()
        self.question_answered = False


    def get_history(self):
            print("\nVous avez déjà visité les pièces suivantes:\n")
            for i in range (len(self.history)):
                print('-'+ self.history[i].name)
            if not self.history:
                print("\nVous n'avez visité aucune époque")

        
    # Define the move method.

    def move(self, direction):
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
                        print("\nVous avez répondu correctement, mais vous n'avez pas la machine Enigma.")
                        self.game.victory = False
                        self.game.finished = False

                    elif answer == "go 2":
                    # Envoyer le joueur vers la salle correspondante à "2"
                        print("\nMauvaise réponse. Vous êtes envoyé dans une autre époque.")
                        self.current_room = self.current_room.exits.get("2")  # Déplacement automatique
                        print(self.current_room.get_long_description())
                        self.game.victory = False
                        self.game.finished = False

                    elif answer == "go 3":
                    # Envoyer le joueur vers la salle correspondante à "2"
                        print("\nMauvaise réponse. Vous êtes envoyé dans une autre pièce.")
                        self.current_room = self.current_room.exits.get("3")  # Déplacement automatique
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
        if not self.inventory:  # Vérifier si l'inventaire est vide
            print("\nVotre inventaire est vide.")
        
        else:
            print("\nVous disposez des items suivants :")  # Parcourir les items du dictionnaire
            for item in self.inventory.values():
                print(f"{item}")  # Utilise la méthode __str__() définie dans la classe Item
    
    def get_inventory_lieux(self):
        if not self.inventory:  # Vérifier si l'inventaire est vide
            print("\nIl n'y a rien ici.")
        
        else:
            print("\nLa pièce contient:")  # Parcourir les items du dictionnaire
            for item in self.inventory.values():
                print(f" -{item}")  # Utilise la méthode __str__() définie dans la classe Item


        

         
    




    