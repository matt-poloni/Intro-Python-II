# Dictionary of directions mapping single letter to word
dirs = {
  'n': 'north',
  's': 'south',
  'e': 'east',
  'w': 'west'
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

    # Dictionary of user commands mapped to actions
    dir_kv = [*dirs.keys(), *dirs.values()]
    switch = {
      **dict.fromkeys(
        dir_kv,
        lambda: p.travel(cmd0, dirs)
      ),
      **dict.fromkeys(
        ["i", "inventory"],
        lambda: None
      ),
      **dict.fromkeys(
        ["g", "get", "t", "take"],
        lambda: p.take_drop(cmd0, cmd1, p.current_room.list, p.list)
      ),
      **dict.fromkeys(
        ["d", "drop"],
        lambda: p.take_drop(cmd0, cmd1, p.list, p.current_room.list)
      ),
      **dict.fromkeys(
        ["q", "quit"],
        lambda: None
      )
    }

    try:
        switch[cmd0]()
    except:
        print(f"ERROR: '{cmd0}' is not a recognized command. Try again.\n-------")

    # Return first command for while loop
    return cmd0
