from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("🗻  Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("🍽  Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("🌋  Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("⛰⛰ Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("💰  Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# declares all items

items = {
    'knife':  Item("Knife",
                     "🔪 A long pointy sharp knife"),
    'shovel':  Item("Spade Shovel",
                     "⛏ Very good at digging holes."),
    'candle':  Item("Gold Candlestick",
                     "🕯 It will light your path. Or buy you something nice"),
                     
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# room items


room['outside'].addItem([items['shovel']])
room['outside'].addItem([items['knife']])
room['foyer'].addItem([items['candle']])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

myPlayer = Player('😎 Shawn', room['outside'])

print(f"\n\n ✨✨✨ WELOME TO THE JOURNEY {myPlayer.name}!!! ✨✨✨ \n\n")

while True:
    print(myPlayer)
    command=input('\tEnter a command: ')
    print("\n\n\n\n\n\n\n")
    if command == 'q':
        break
    if command == "n":
        if myPlayer.current_room.n_to:
            myPlayer.current_room=myPlayer.current_room.n_to
            print(f"\t\t You entered: -> {myPlayer.current_room.name}: {myPlayer.current_room.description}\n") #prints location
        else:
            print("\t\t There is no room there...\n")
    if command == "s":
        if myPlayer.current_room.s_to:
            myPlayer.current_room=myPlayer.current_room.s_to
            print(f"\t\t You entered: -> {myPlayer.current_room.name}: {myPlayer.current_room.description}\n") #prints location
        else:
            print("\t\t There is no room there...\n")
    if command == "e":
        if myPlayer.current_room.e_to:
            myPlayer.current_room=myPlayer.current_room.e_to
            print(f"\t\t You entered: -> {myPlayer.current_room.name}: {myPlayer.current_room.description}\n") #prints location
        else:
            print("\t\t There is no room there...\n")
    if command == "w":
        if myPlayer.current_room.w_to:
            myPlayer.current_room=myPlayer.current_room.w_to
            print(f"\t\t You entered: -> {myPlayer.current_room.name}: {myPlayer.current_room.description}\n") #prints location
        else:
            print("\t\t There is no room there...\n")
    
    if command == "look":
        
        # print(type(myPlayer.current_room.inventory))
        if len(myPlayer.current_room.inventory) > 0:
            # print(myPlayer.current_room.inventory)
            print("Items in this room:\n")
            [ print(item.name) for item in myPlayer.current_room.inventory]
        # print(myPlayer.current_room.inventory)
        # [ print(f"{item.name} - {item.description}") for item in myPlayer.current_room.inventory]
        else:
            print("\tThere is nothing here...\n")
        
    if command == "inv":
        # print(f"\t My Inventory: {[ [item.name, item.description] for item in myPlayer.inventory]}\n")
        print(f"\t My Inventory: \n")
        print(myPlayer.inventory)
        [ print(item.name) for item in myPlayer.inventory]
        # print(myPlayer.inventory)
        # [ print(f"{item[0].name} - {item[0].description}") for item in myPlayer.inventory]
        # print(f"\t My Inventory: {[ (item.name, item.description) for item in myPlayer.inventory]}\n")

    if command == "take":
        stuff = myPlayer.current_room.inventory
        # take_this=input('\tWhat to take?: ')
        if len(stuff) > 0:
            # print(f"\t You took it!")
            print(f"stuff to take: \n")
            [print(item.name) for item in stuff]
            item_chosen = input("\t which item:")
            myPlayer.current_room.removeItem(item_chosen, myPlayer)
        else:
            print(f"\t There is nothing to get.\n")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap modulse might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
