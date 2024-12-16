class Inventory:
    def __init__(self):
        self.items = set()  # Utilisation d'un set

    def add_item(self, item):
        self.items.add(item)

    def get_inventory(self):
        if not self.items:
            print("Il n'y a rien ici.")
        else:
            print("Les objets présents sont :")
            for item in self.items:
                print(f"    - {item}")

