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

    'bedroom': Room("🛏  Bedroom", """You've walked into the masters bedroom. It looks pretty tidy in here, but something shiny is under the bed."""),

    'locked_room': Room("🔒 Locked Room", """You have made it into the locked room! its cold in here, but smells like food."""),
}

# declares all items

items = {
    'knife':  Item("Knife",
                     "🔪 A long pointy sharp knife"),
    'shovel':  Item("Shovel",
                     "⛏ Very good at digging holes."),
    'candle':  Item("Candlestick",
                     "🕯 It will light your path. Or buy you something nice"),
    'key':  Item("Key",
                     "🔑  A key!! But what does it open?"),
                     
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
room['treasure'].n_to = room['locked_room']
room['locked_room'].s_to = room['treasure']
room['overlook'].w_to = room['bedroom']
room['bedroom'].e_to = room['overlook']

# Locked Rooms



# room items


room['outside'].addItem(items['shovel'])
room['outside'].addItem(items['knife'])
room['foyer'].addItem(items['candle'])
room['bedroom'].addItem(items['key'])


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

    split_command = command.split(' ')

    if len(split_command) == 1:

        # Help commands

        if command == 'h':
            print('\n These are your avaible one word commands:\n')

            print('Directions:')
            print('\tn = north')
            print('\te = east')
            print('\ts = west')
            print('\tw = south\n')

            print('Other:')
            print('\tq = Quit Game')
            print("\tinv = View your Inventory")
            print("\tlook = Look whats in a room")

            print("\n")
        elif command == 'h2':
            print('\n These are your avaible two word commands:\n')
            
            print('Actions:')
            print('\ttake [object] = Take a object by name')
            print('\tdrop [object] = Take a object by name')


            print("\n")
        
        elif command == 'q':
            break
        
        elif command == "n":
            if myPlayer.current_room.n_to:
                myPlayer.current_room=myPlayer.current_room.n_to
                print(f"\t\t You entered: -> {myPlayer.current_room.name}: {myPlayer.current_room.description}\n") #prints location
            else:
                print("\t\t There is no room there...\n")
        elif command == "s":
            if myPlayer.current_room.s_to:
                myPlayer.current_room=myPlayer.current_room.s_to
                print(f"\t\t You entered: -> {myPlayer.current_room.name}: {myPlayer.current_room.description}\n") #prints location
            else:
                print("\t\t There is no room there...\n")
        elif command == "e":
            if myPlayer.current_room.e_to:
                myPlayer.current_room=myPlayer.current_room.e_to
                print(f"\t\t You entered: -> {myPlayer.current_room.name}: {myPlayer.current_room.description}\n") #prints location
            else:
                print("\t\t There is no room there...\n")
        elif command == "w":
            if myPlayer.current_room.w_to:
                myPlayer.current_room=myPlayer.current_room.w_to
                print(f"\t\t You entered: -> {myPlayer.current_room.name}: {myPlayer.current_room.description}\n") #prints location
            else:
                print("\t\t There is no room there...\n")

        elif command == "inv":
            print(f"\t My Inventory: \n")
            # print(myPlayer.inventory)
            [ print(f"{item.name} - {item.description}\n") for item in myPlayer.inventory]
    
        elif command == "look":
            
            # print(type(myPlayer.current_room.inventory))
            if len(myPlayer.current_room.inventory) > 0:
                # print(myPlayer.current_room.inventory)
                print("Items in this room:\n")
                [ print(f"{item.name} - {item.description}") for item in myPlayer.current_room.inventory]
                print("\n")
            # print(myPlayer.current_room.inventory)
            # [ print(f"{item.name} - {item.description}") for item in myPlayer.current_room.inventory]
            else:
                print("\tThere is nothing in this room...\n")
        else:
            print("\n Not a valid command. Type h1 for all 1 word commands. \n")


    elif len(split_command) == 2:

        if split_command[0] == "take":
            room_stuff = myPlayer.current_room.inventory
            # take_this=input('\tWhat to take?: ')
            if len(room_stuff) > 0:
                # print(f"\t You took it!")
                # print(f"room_stuff to take: \n")
                # [print(f"{item.name} - {item.description}") for item in room_stuff]
                print("\n")
                # item_chosen = input("\t which item:")
                myPlayer.current_room.removeItem(split_command[1], myPlayer)
                # myPlayer.addItem(room_stuff)
            else:
                print(f"\n There is nothing here.\n")

        elif split_command[0] == "drop":
            my_stuff = myPlayer.inventory
            # take_this=input('\tWhat to take?: ')
            if len(my_stuff) > 0:
                # print(f"\t You took it!")
                # print(f"my_stuff to take: \n")
                # [print(f"{item.name} - {item.description}") for item in my_stuff]
                print("\n")
                # item_chosen = input("\t which item:")
                myPlayer.removeItem(split_command[1], myPlayer.current_room)
                # myPlayer.addItem(my_stuff)
            else:
                print(f"\n You do not have any items.\n")
        
        else:
            print("\n Not a valid command. Type h2 for all 2 word commands. \n")
        

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
