"""
Classe principale du jeu.

Ce fichier contient la définition de la classe `Game`, qui gère les mécaniques principales
du jeu.
"""

# Import modules

from room1 import Room
from player1 import Player
from command1 import Command
from actions1 import Actions
from item import Item
from character import Characters

DEBUG = True

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.victory = False
        self.defeat = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.items = {}
        self.characters = {}


    # Setup the game
    def setup(self):
        """
        Configure le jeu en initialisant les commandes, les salles, les objets, les PNJ,
        et le joueur.
        """
        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help

        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit

        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)",
                      Actions.go, 1)
        self.commands["go"] = go

        back = Command("back", " : retourner en arrière", Actions.back,0)
        self.commands["back"] = back

        inventory = Command("inventory", " : afficher l'inventaire des objets",
                             Actions.inventory, 0)
        self.commands["inventory"] = inventory

        inventory_lieux = Command("inventory_lieux",
                                  " : afficher l'inventaire des objets présents dans la pièce",
                                    Actions.inventory_lieux, 0)
        self.commands["inventory_lieux"] = inventory_lieux

        look = Command("look",
                        " : afficher les objets présents dans la pièce actuelle",
                          Actions.look, 0)
        self.commands["look"] = look

        take = Command("take",
                        " : prendre les objets présents dans la pièce actuelle",
                          Actions.take, 1)
        self.commands["take"] = take

        drop = Command("drop", " : déposer les objets présents dans la pièce actuelle",
                        Actions.drop, 1)
        self.commands["drop"] = drop

        talk = Command("talk", " : faire parler les PNJ",
                        Actions.talk, 1)
        self.commands["talk"] = talk





        # Setup rooms

        prehistory = Room("Prehistory", "à la préhistoire."
                           "Quel événement marque respectivement"
                           "le début et la fin de la préhistoire ?"
                          "\n1 : C’est l’apparition de l’Homme qui"
                          "en marque le début et celle de l’écriture qui en marque la fin"
                          "\n2 : C’est l’apparition des dinosaures"
                          "qui en marque le début et la victoire des hommes"
                          "sur eux qui en marque la fin.")
        self.rooms.append(prehistory)

        antiquity = Room("Antiquity", "à l'antiquité."
                         "Quand ont eu lieu les premiers Jeux Olympiques ?"
                         "\n1 : Avant l’Antiquité."
                         "\n2 : Après l’Antiquité."
                         "\n3 : Pendant l’Antiquité."
                         )
        self.rooms.append(antiquity)

        antiquity_apocalyptic = Room("Antiquity_apocalyptic",
                                      "à l'antiquité apocalyptique. Vous êtes en face d’une armée de Romains,"
                                      "leur chef vous demande de capituler, que décidez vous de faire ?"
                                     "\n1 : Capituler."
                                     "\n2 : Fuir"
                                     "\n3 : Vous battre"
                                     )
        self.rooms.append(antiquity_apocalyptic)

        middle_age = Room("middle_age",
                           "au moyen âge. Quel évènement marque le début et la fin du Moyen-Age ?"
                          "\n 1 : La chute de l’empire Romain en marque"
                          "le début et la découverte de l’Amérique en marque la fin."
                          "\n 2 : Le couronnement de Charlemagne"
                          "marque le début et le changement de nom de la GAULE pour devenir la FRANCE la fin"
                          "\n 3 : La découverte du RNB en marque"
                          "le début et celle du RAP en marque la fin.")
        self.rooms.append(middle_age)

        middle_age_apocalyptic = Room("middle_age_apocalyptic",
                                       "au moyen âge apocalyptique.Vous êtes à côté d’un"
                                       "pommiers et vous apercevez une meute de loups devant vous"
                                       " et une meute de hyènes derrière vous, vous êtes paniqués mais"
                                       "vous devez prendre une décision pour espérer survivre:"
                                      "\n1 : Faire le mort"
                                      "\n2 : Courir vers la droite"
                                      "\n3 : Grimper au pommier"
                                      )
        self.rooms.append(middle_age_apocalyptic)

        modern_period = Room("Modern_period", "aux temps modernes."
                             "Comment se nomme le siècle le plus connu des Temps Modernes ?"
                            "\n1 : Le siècle des Lumières"
                            "\n2 : Le siècle de la musique"
                            "\n3 : Le siècle de la révolution")
        self.rooms.append(modern_period)

        modern_period_apocalyptic = Room("Modern_period_apocalyptic",
                                          "aux temps modernes apocalyptiques... "
                                          "Vous souhaitez faire fortune dans le commerce "
                                          "pour cela vous hésitez entre trois marques à succès"
                                          " de votre époque que vous pourriez copier:"
                                         "\n1 : Louis Vuitton"
                                         "\n2 : Apple"
                                         "\n3 : Une épicerie avec des épices du monde")
        self.rooms.append(modern_period_apocalyptic)

        contemporary_times = Room("Contemporary_times", "à l'époque contemporaine."
                                  " Quelles sont les dates du début et de la fin de la première guerre mondiale ?"
                                  "\n 1 : 1914 - 1918"
                                  "\n 2 : 1939 - 1945"
                                  "\n 3 : Il n'y a jamais eu de Guerre Mondiale")                              
        self.rooms.append(contemporary_times)

        contemporary_times_apocalyptic = Room("Contemporary_times_apocalyptic",
                                               "à l'époque contemporaine apocalyptique..."
                                               "Nous sommes le 11 septembre 2001, vous avez une forte"
                                               " envie de voyager, quel mode de transport allez vous choisir:"
                                              "\n1 : La voiture"
                                              "\n2 : L'avion"
                                              "\n3 : Le bateau")
        self.rooms.append(contemporary_times_apocalyptic)


        future = Room("Future", "dans le futur. Si vous deviez le noter, combien mettriez vous à ce jeu:"
                      "\n1 : (20 ou +)/20"
                      "\n2 : (entre 18 et 20)/20"
                      "\n3 : (entre 15 et 17)/20")
        self.rooms.append(future)

        future_apocalyptic  = Room("Future_apocalyptic ", "dans le futur apocalyptique"
                                   "...Vous présidez une conférence réunissant toutes"
                                   " les puissances mondiales et ayant pour but de décider"
                                   " vous devez continuer à investir dans l’IA, lors du débat,"
                                   " les avis sont mitigés et aucune décision ne met tout le monde d’accord"
                                   ".En tant que président vous avez le dernier mot, que décidez vous de faire:"
                                   "\n1 : continuer à investir dans l’IA "
                                   "\n2 : stopper immédiatement tout investissement"
                                   "\n3 : reporter le débat ")
        self.rooms.append(future)

        # Create items

        sword = Item("sword", "une épée au fil tranchant comme un rasoir", 2)
        self.items['sword']=sword
        vase = Item("vase", "un vase décoré avec des motifs de l'Antiquité grecque",2 )
        self.items['vase']=vase
        torch = Item("torch", "une torche flamboyante éclairant comme le soleil", 1)
        self.items['torch']=torch
        tesla = Item("tesla", "une voiture qui n'a pas besoin de conducteur", 1000)
        self.items['tesla']=tesla
        gant_de_l_infini = Item("gant_de_l_infini", "un gant avec 5 pierres capable de détruire l'univers", 3)
        self.items['gant_de_l_infini']=gant_de_l_infini
        machine_enigma = Item("machine_enigma", "utilisé pour coder des messages pendant la seconde guerre mondiale", 3)
        self.items['machine_enigma']=machine_enigma
        parchemin = Item("parchemin", "contient un odre de mission impérial", 0.5)
        self.items['parchemin']=parchemin


        # Create PNJ

        lucy = Characters("lucy", "le premier homme préhistorique" ,prehistory,msgs= ["Tu sembles perdu", "Les animaux sont tes alliés","Suis les traces de ce cerf..."])
        self.characters['lucy']=lucy

        socrate = Characters("socrate", "un vieil homme sage" ,antiquity, msgs = ["Connais-toi toi même...", "Je ne suis ni Athénien ni grec, je suis un citoyen du monde",
                             "Tout ce que je sais, c'est que je ne sais rien"])
        self.characters['socrate']=socrate

        jeanne_d_arc = Characters("jeanne_d_arc", "une jeune femme vête d'une armure et un drapeau français à la main" ,middle_age,
                                   msgs = ["Seul un coeur pur peut guider à la victoire","Vivre, c’est du courage, et non pas de la crainte !"
                                   "Je n’ai pas peur... "])
        self.characters['jeanne_d_arc']=jeanne_d_arc

        napoleon = Characters("napoleon", "un homme petit de taille mais d'une grande présence" ,modern_period, msgs = ["Un génie stratégique ne suit pas les règles",
                              "Si tu veux devenir plus grand, il faut aller au-delà des frontières",
                             "L'imagination gouverne le monde"])
        self.characters['napoleon']=napoleon

        alan_turing = Characters("alan_turing", "un homme intelligent et réservé" ,contemporary_times, msgs = ["Le logique est la clé pour déverouiller l'inconnu",
                              "Commence par déchiffrer les codes invisibles"])
        self.characters['alan_turing']=alan_turing

        elon_musk = Characters("elon_musk", "un génie excentrique" ,future, msgs = [ "Je travaille sur le futur de l'humanité",
                              "Avez-vous des idées révolutionnaires à partager ?"])
        self.characters['elon_musk']=elon_musk

        thanos = Characters("thanos", "un géant à la peau violette avec le gant de l'infini" ,future_apocalyptic, msgs = ["Tout équilibre nécessite un sacrifice",
                              "Le destin est inévitable"])
        self.characters['thanos']=thanos


        # Create exits for rooms

# Prehistory exits
        prehistory.exits = {"1": antiquity, "2": antiquity_apocalyptic, "3": None}
        prehistory.reponse = {"1": "1", "2": "2", "3": "3"}

# Antiquity exits
        antiquity.exits = {"1": prehistory, "2": antiquity_apocalyptic, "3": middle_age}
        antiquity.reponse = {"1": "1", "2": "2", "3": "3"}

# Antiquity Apocalyptic exits
        antiquity_apocalyptic.exits = {"1": antiquity_apocalyptic, "2": middle_age, "3": modern_period}
        antiquity_apocalyptic.reponse = {"1": "1", "2": "2", "3": "3"}

# Middle Age exits
        middle_age.exits = {"1": modern_period, "2": antiquity, "3": middle_age_apocalyptic}
        middle_age.reponse = {"1": "1", "2": "2", "3": "3"}

# Middle Age Apocalyptic exits
        middle_age_apocalyptic.exits = {"1": middle_age_apocalyptic, "2": antiquity, "3": middle_age}
        middle_age_apocalyptic.reponse = {"1": "1", "2": "2", "3": "3"}

# Modern Period exits
        modern_period.exits = {"1": contemporary_times, "2": middle_age, "3": modern_period_apocalyptic}
        modern_period.reponse = {"1": "1", "2": "2", "3": "3"}

# Modern Period Apocalyptic exits
        modern_period_apocalyptic.exits = {"1": modern_period_apocalyptic, "2": middle_age, "3": modern_period}
        modern_period_apocalyptic.reponse = {"1": "1", "2": "2", "3": "3"}

# Contemporary Times exits
        contemporary_times.exits = {"1": future, "2": modern_period, "3": contemporary_times_apocalyptic}
        contemporary_times.reponse = {"1": "1", "2": "2", "3": "3"}

# Contemporary Times Apocalyptic exits
        contemporary_times_apocalyptic.exits = {"1": contemporary_times_apocalyptic, "2": modern_period, "3": contemporary_times}
        contemporary_times_apocalyptic.reponse = {"1": "1", "2": "2", "3": "3"}

# Future exits
        future.exits = {"1": future, "2": contemporary_times, "3": future_apocalyptic}
        future.reponse = {"1": "1", "2": "2", "3": "3"}

# Future Apocalyptic exits
        future_apocalyptic.exits = {"1": contemporary_times_apocalyptic, "2": middle_age_apocalyptic, "3": modern_period_apocalyptic}
        future_apocalyptic.reponse = {"1": "1", "2": "2", "3": "3"}



        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "),
                             current_room=None,
                             game=self)
        self.player.current_room = prehistory
        self.player.game = self

        self.player.inventory = {
            "torch" : torch
        }
        prehistory.inventory_lieux.add(torch)
        antiquity.inventory_lieux.add(vase)
        middle_age.inventory_lieux.add(sword)
        modern_period.inventory_lieux.add(parchemin)
        contemporary_times.inventory_lieux.add(machine_enigma)
        future.inventory_lieux.add(tesla)
        future_apocalyptic.inventory_lieux.add(gant_de_l_infini)



        prehistory.characters = {"lucy" : lucy}
        antiquity.characters = {"Socrate" : socrate}
        middle_age.characters = {"Jeanne_d_Arc" : jeanne_d_arc}
        modern_period.characters = {"Napoléon" : napoleon}
        contemporary_times.characters = {"Alan_Turing" : alan_turing}
        future.characters = {"Elon_Musk" : elon_musk}
        future_apocalyptic = {"Thanos" : thanos}





    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()

        # Appel de la méthode get_inventory
        self.player.get_inventory()
    # Loop until the game is finished
        while not self.finished:
        # Si le joueur a gagné, affichez un message et terminez le jeu
            if self.victory:
                print("\nFélicitations ! Vous avez atteint le futur et gagné le jeu ! 🎉")
                self.finished = True
                break
            if self.defeat:
                print("Vous avez échoué, c'est la fin du jeu...")
                self.finished = True
                break
            if self.finished:
                break

        # Get the command from the player
            self.process_command(input("> "))
        print("Merci d'avoir joué !")

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

        if self.finished:
            return

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !"
              "\nLors d'une expérience qui a mal tournée, vous avez été envoyé dans le passé or votre objectif est d'aller dans le futur."
              "\nPour cela, vous devrez répondre correctement aux questions qui vous serons posées."
              "\nAttention, si vous répondez mal, vous risquez de retourner à une époque différente, ou pire, apocalyptique.")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())



def main():
    # Create a game object and play the game
    Game().play()


if __name__ == "__main__":
    main()
