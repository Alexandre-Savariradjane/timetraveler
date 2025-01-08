# Description: Game class

# Import modules

from room1 import Room
from player1 import Player
from command1 import Command
from actions1 import Actions
from item import Item

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.items = {}
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help

        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit

        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go

        back = Command("back", " : retourner en arrière", Actions.back,0)
        self.commands["back"] = back

        inventory = Command("inventory", " : afficher l'inventaire des objets", Actions.inventory, 0)
        self.commands["inventory"] = inventory
    
        inventory_lieux = Command("inventory_lieux", " : afficher l'inventaire des objets présents dans la pièce", Actions.inventory_lieux, 0)
        self.commands["inventory_lieux"] = inventory_lieux

        look = Command("look", " : afficher les objets présents dans la pièce actuelle", Actions.look, 0)
        self.commands["look"] = look

        take = Command("take", " : prendre les objets présents dans la pièce actuelle", Actions.take, 1)
        self.commands["take"] = take

        drop = Command("drop", " : déposer les objets présents dans la pièce actuelle", Actions.drop, 1)
        self.commands["drop"] = drop

        

        # Setup rooms

        prehistory = Room("Prehistory", "dans une grotte. Vous voyez des peintures qui représentent des mammouths et des silouhettes humaines.")
        self.rooms.append(prehistory)

        antiquity = Room("Antiquity", "dans une immense cité en pierre entourée de tempes en marbre,sous le regard des dieux de l'Olympe.")
        self.rooms.append(antiquity)

        antiquity_apocalyptic = Room("Antiquity_apocalyptic", "dans une immense cité en pierre entourée de tempes en marbre,sous le regard des dieux de l'Olympe.")
        self.rooms.append(antiquity_apocalyptic)

        middle_age = Room("middle_age", "dans une imposante forteresse entourée de douves et de forêts profondes. Des voix semblent provenir des champs de bataille.")
        self.rooms.append(middle_age)

        middle_age_apocalyptic = Room("middle_age_apocalyptic", "dans une imposante forteresse entourée de douves et de forêts profondes. Des voix semblent provenir des champs de bataille.")
        self.rooms.append(middle_age_apocalyptic)

        modern_period = Room("Modern_period", "dans un somptueux palais aux miroirs scintillants et aux jardins parfaitement ordonnés, l'écho des pas des courtisans se mêle aux intrigues de la monarchie absolue.")
        self.rooms.append(modern_period)

        modern_period_apocalyptic = Room("Modern_period_apocalyptic", "dans un somptueux palais aux miroirs scintillants et aux jardins parfaitement ordonnés, l'écho des pas des courtisans se mêle aux intrigues de la monarchie absolue.")
        self.rooms.append(modern_period_apocalyptic)

        contemporary_times = Room("Contemporary_times", "dans une place pavée enflammée par la foule en révolte. Les drapeaux s’agitent dans ciel.")
        self.rooms.append(contemporary_times)

        contemporary_times_apocalyptic = Room("Contemporary_times_apocalyptic", "dans une place pavée enflammée par la foule en révolte. Les drapeaux s’agitent dans ciel.")
        self.rooms.append(contemporary_times_apocalyptic)

        present = Room("Present", "dans le parking de l'ESIEE, les étudiants sortent des cours.")
        self.rooms.append(present)

        future = Room("Future", "dans une cité suspendue au-dessus des nuages, des voitures volantes glissent entre les tours lumineuses.")
        self.rooms.append(future)

        future_apocalyptic  = Room("Future_apocalyptic ", "dans une cité suspendue au-dessus des nuages, des voitures volantes glissent entre les tours lumineuses.")
        self.rooms.append(future)

        # Create items

        sword = Item("sword", "une épée au fil tranchant comme un rasoir", 2)
        self.items['sword']=sword
        vase = Item("vase", "un vase décoré avec des motifs de l'Antiquité grecque",2 )
        self.items['vase']=vase
        torch = Item("torch", "une torche flamboyante éclairant comme le soleil", 1)
        self.items['torch']=torch


        # Create exits for rooms

        prehistory.exits = {"N" : middle_age, "E" : None, "S" : future, "O" : None,"Up":contemporary_times_apocalyptic, "Down": future}
        antiquity.exits = {"N" : modern_period, "E" : None, "S" : None, "O" : None}
        middle_age.exits = {"N" : None, "E" : modern_period, "S" : prehistory, "O" : None}
        modern_period.exits = {"N" : None, "E" : None, "S" : antiquity, "O" : middle_age}
        contemporary_times.exits = {"N" : antiquity, "E" : None, "S" : None, "O" : future}
        future.exits = {"N" : prehistory, "E" : contemporary_times, "S" : None, "O" : None}


        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = prehistory
        self.player.inventory = {
            "vase" : vase
        }
        prehistory.inventory_lieux.add(sword)
        middle_age.inventory_lieux.add(sword)
        antiquity.inventory_lieux.add(vase)

        # Appel de la méthode get_inventory
        self.player.get_inventory()

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print()
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())

    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()

