# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.points = 0

    def addItem(self, items):
        # print("add item to player")
        self.inventory.append(items)
        print(f"\nYou received {items.name}\n")

    def removeItem(self, item_name, room):
        y = [item.name.lower() for item in self.inventory]
        if item_name.lower() not in y:
            print('You dont have that item.\n')
        def remove_and_add(item):
            self.inventory.remove(item)
            print(f"\nYou dropped {item.name}\n")
            room.addItem(item)
        [remove_and_add(item) for item in self.inventory if item.name.lower() == item_name.lower()]

    def __str__(self):
        return f"\t{self.name}({self.points}gp)- ({self.current_room.name})"