class Characters:

    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def __str__(self):
        return f"- {self.name} : {self.description}, {self.current_room}, {self.msgs}"

    def move(self):
        """
        Déplace le PNJ dans une pièce adjacente au hasard (1 chance sur 2).
        :return: True si le PNJ s'est déplacé, False sinon.
        """
        import random

        if random.choice([True, False]):  # 1 chance sur 2 de se déplacer
            if self.current_room.exits:  # Vérifie qu'il y a des pièces adjacentes
                self.current_room = random.choice(list(self.current_room.exits.values()))
                print(f"{self.name} se déplace de {self.current_room.exits.name} vers {self.current_room}. ")
                return True
        return False
    


