# Dictionary of directions mapping single letter to word
dirs = {
  'n': 'north',
  's': 'south',
  'e': 'east',
  'w': 'west'
}
# Dictionary of user commands
cmds = {
  "dirs": [*dirs.keys(), *dirs.values()],
  "inv": ["i", "inventory"],
  "take": ["g", "get", "t", "take"],
  "drop": ["d", "drop"],
  "quit": ["q", "quit"]
}

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

def parse(cmd, p):
    # Take user command, normalize it, & split into two parts
    cmd = cmd.lower().strip().split(' ')
    cmd0 = cmd[0]
    try:
        cmd1 = cmd[1]
    except:
        cmd1 = "*"

    # Directional commands
    if cmd0 in cmds["dirs"]:
        p.travel(cmd0, dirs)
    # Inventory commands
    elif cmd0 in cmds["inv"]:
        pass
    # Item acquisition
    elif cmd0 in cmds["take"]:
        p.take_drop(cmd0, cmd1, p.current_room.list, p.list)
    # Item deposit
    elif cmd0 in cmds["drop"]:
        p.take_drop(cmd0, cmd1, p.list, p.current_room.list)
    # Unknown commands
    elif cmd0 not in cmds["quit"]:
        print(f"ERROR: '{cmd0}' is not a recognized command. Try again.")

    # Return first command for while loop
    return (cmd0, p)
