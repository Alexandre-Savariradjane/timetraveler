# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]  
        valid_direction = {"N","S","E","O"}

        if direction in ['n', 'Nord', 'nord', 'NORD']:
            direction = 'N'
        if direction in ['s', 'sud','Sud','SUD']:
            direction = 'S'
        if direction in ['e','Est','est','EST']:
            direction = 'E'
        if direction in ['o','Ouest','ouest','OUEST']:
            direction = 'O'
        if direction not in valid_direction:
            print(f"\nDirection '{direction}' non reconnue.\n")
            print(player.current_room.get_long_description())
            return False
        # Move the player in the direction specified by the parameter.
        player.move(direction)
        player.history
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

            # Define the go_back method.
    def back(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        if not player.history :
            print("\nVous ne pouvez pas revenir en arrière, l'historique est vide !\n")
            return False
    

        # Pop the last room from the history and set it as the current room.
        player.current_room = player.history[-1]
        player.history.pop()
        print(f"\nVous êtes de retour dans l'époque précédente : {player.current_room.get_long_description()}")
        print(player.get_history())
        return True
    
    def inventory(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        game.player.get_inventory()

    def inventory_lieux(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        game.player.get_inventory_lieux()
                
    def look(game, list_of_words, number_of_parameters):
        player = game.player
        room = game.player.current_room
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        game.player.current_room.get_inventory()

        return True
    

    def take(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de ramasser un objet dans la pièce actuelle.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si l'objet a été pris avec succès, False sinon.
        """
        player = game.player
        l = len(list_of_words)
        room = game.player.current_room

        # Vérifie que le nombre de paramètres est correct
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Récupère l'objet à ramasser
        if room.inventory =={}:
            print("\n il n'y a rien !\n")

            return False

        item = list_of_words[1]

        if item not in room.inventory.keys():
            print("\n cette objets n'est pas dans cette piece!\n")

            return False




        objet=game.items[item]

        player.inventory[f'{item}']=objet

        print(f"\n vous avez ramasser,{objet.name}!\n")


        room.inventory.pop(f"{item}")
        return True


    def drop(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de déposer un objet dans la pièce actuelle.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si l'objet a été pris avec succès, False sinon.
        """
        player = game.player
        l = len(list_of_words)
        room = game.player.current_room

        # Vérifie que le nombre de paramètres est correct
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Récupère l'objet à ramasser
        if player.inventory =={}:
            print("\n il n'y a rien !\n")

            return False

        item = list_of_words[1]

        if item not in player.inventory.keys():
            print("\n cette objet n'est pas dans cette piece!\n")

            return False




        objet=game.items[item]

        room.inventory[f'{item}']=objet

        print(f"\n vous avez déposé,{objet.name}!\n")


        player.inventory.pop(f"{item}")
        return True
