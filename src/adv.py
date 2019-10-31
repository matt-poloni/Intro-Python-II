from room import Room
from item import Item, LightSource
from player import Player
from parse import parse

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Place items in rooms
room['outside'].list.append(LightSource("Lamp", "A source of light for any dark places you may find yourself."))
room['foyer'].list.append(Item("Wallet", "A place to store money."))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("What is your name? ")
p = Player(name, room['outside'])

cmd0 = ""
while cmd0 != "q":
    if cmd0 == "i":
        list = f"[{', '.join([i.name for i in p.list])}]"
        print(f"Inventory: {list}\n-------")
    else:
        # Print current room & description
        print(f"\n{p.current_room}\n-------")

    # Take command from user
    cmd = input("Command: ")
    # Update primary command and current room
    cmd0 = parse(cmd, p)

print(f"\nThanks for playing, {p.name}!\n==============")
