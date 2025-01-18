"""
Ce fichier contient la classe Characters, qui gère les PNJ (personnages non-joueurs).
"""


import random


class Characters:
    """
    Représente un personnage non joueur (PNJ) dans le jeu.

    Attributs :
        name (str) : Nom du personnage.
        description (str) : Description du personnage.
        current_room (Room) : Salle actuelle du personnage.
        msgs (list[str]) : Liste des messages associés au personnage.
    """


    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def __str__(self):
        return f"- {self.name} : {self.description}"

    def move(self):
        """
        Déplace le PNJ dans une pièce adjacente de façon aléatoire.
        Retourne True si le PNJ a bougé, False sinon.
        """
        import game1
        if random.choice([True, False]):  # Chance 50% de se déplacer
            if not self.current_room.exits:  # Si aucune sortie n'est disponible
                if game1.DEBUG:  # Accède à DEBUG via game1
                    print(f"DEBUG: {self.name} ne peut pas se déplacer, aucune sortie disponible.")
                return False

            # Choisir une direction au hasard parmi les sorties possibles
            direction = random.choice(list(self.current_room.exits.keys()))
            next_room = self.current_room.get_exit(direction)
            if next_room:
                self.current_room = next_room  # Déplace le PNJ dans la nouvelle pièce
                if game1.DEBUG:  # Accède à DEBUG via game1
                    print(f"{self.name} se déplace vers {next_room.name}.")
                return True
            if game1.DEBUG:  # Accède à DEBUG via game1
                print(f"{self.name} ne peut pas se déplacer dans cette direction.")
            return False
        if game1.DEBUG:  # Accède à DEBUG via game1
            print(f"{self.name} reste sur place.")
        return False

    def get_msgs(self):
        """
        Retourne le message suivant de manière cyclique parmi ceux du PNJ.
        S'il ne reste plus de message, il recommence à zéro.

        :return: Le message du PNJ
        """

        if len(self.msgs) == 0:  # Si aucun message n'est défini
            return "Ce personnage n'a rien à dire."

        # Extraire le premier message
        message = self.msgs.pop(0)
        # Ajouter le message à la fin pour un comportement cyclique
        self.msgs.append(message)

        return message
