# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = []
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def addItem(self, items):
        # self.inventory.append(items)
        self.inventory.extend(items)
            

    def removeItem(self, item_name, player):
        # print("remove it from room")
        [self.inventory.remove(item) if item.name.lower() == item_name.lower() else print('not here!') for item in self.inventory  ]

    def __str__(self):
        return f"this is room {self.name}. Description: {self.description}"