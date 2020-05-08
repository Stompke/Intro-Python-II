# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, locked = False):
        self.name = name
        self.description = description
        self.inventory = []
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.is_locked = locked

    def addItem(self, items):
        # self.inventory.append(items)
        self.inventory.append(items)
            

    def removeItem(self, item_name, player):
        # print("remove it from room")
        y = [item.name.lower() for item in self.inventory]
        if item_name.lower() in y:
            print('🥳 Yay!')
        else:
            print('That item is not in this room.\n')
        def remove_and_add(item):
            self.inventory.remove(item)
            player.addItem(item)
        # [remove_and_add(item) if item.name.lower() == item_name.lower() else print('that item is not here') for item in self.inventory  ]
        [remove_and_add(item) for item in self.inventory if item.name.lower() == item_name.lower()]

    def __str__(self):
        return f"this is room {self.name}. Description: {self.description}"