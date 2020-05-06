# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def addItem(self, item):
        self.inventory.append(item)

    def removeItem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_room.addItem(item)

    def __str__(self):
        return f"{self.name} is in room "