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
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    
