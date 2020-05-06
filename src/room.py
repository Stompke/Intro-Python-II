# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, inventory = []):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def addItem(self, item):
        self.inventory.append(item)

    def removeItem(self, item, player):
        if item in self.inventory:
            self.inventory.remove(item)
            player.addItem(item)

    def __str__(self):
        return f"this is room {self.name}. Description: {self.description}"