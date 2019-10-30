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

def parse(cmd, cur):
    # Take user command, normalize it, & split into two parts
    cmd = cmd.lower().strip().split(' ')
    cmd0 = cmd[0]
    try:
        cmd1 = cmd[1]
    except:
        cmd1 = "*"

    # Directional commands
    if cmd0 in cmds["dirs"]:
        d = cmd0[0]
        dir = dirs[d]
        if (to := getattr(cur, f"{d}_to")) != None:
            cur = to
        else:
            print(f"ERROR: You cannot travel {dir}. Try again.")
    # Item acquisition
    elif cmd0 in cmds["take"]:
        pass
    # Item deposit
    elif cmd0 in cmds["drop"]:
        pass
    # Unknown commands
    elif cmd0 not in cmds["quit"]:
        print(f"ERROR: '{cmd0}' is not a recognized command. Try again.")

    # Return first command for while loop
    return (cmd0, cur)