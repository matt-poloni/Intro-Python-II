from room import Room
from player import Player
from textwrap import fill

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("What is your name? ")
p = Player(name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
cmd0 = ""
quitter = ["q", "quit"]
while cmd0 not in quitter:
    # Print current room & description
    curr = p.current_room
    print(f"\n{curr}\n")
    # Dictionary of directions mapping single letter to word
    dirs = {
      'n': 'north',
      's': 'south',
      'e': 'east',
      'w': 'west'
    }

    # Take user command and split into two parts
    cmd = input("Command: ").lower().strip().split(' ')
    cmd0 = cmd[0]
    try:
        cmd1 = cmd[1]
    except:
        cmd1 = "*"
    
    if cmd0 in [*dirs.keys(), *dirs.values()]:
        d = cmd0[0]
        dir = dirs[d]
        if (to := getattr(curr, f"{d}_to")) != None:
            p.current_room = to
        else:
            print(f"ERROR: You cannot travel {dir}. Try again.")
    elif cmd0 not in quitter:
        print(f"ERROR: '{cmd0}' is not a recognized command. Try again.")
