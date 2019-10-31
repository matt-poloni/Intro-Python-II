# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, list=None):
        self.name = name
        self.current_room = current_room
        self.list = [] if list is None else list
    def __str__(self):
        return f"{self.name}: {self.list}"
    def __repr__(self):
        return f"Player({repr(self.name)}, {repr(self.current_room)})"
    def travel(self, cmd0, dirs):
        d = cmd0[0]
        dir = dirs[d]
        if (to := getattr(self.current_room, f"{d}_to")) != None:
            self.current_room = to
            print(f"Traveling {dir} to {to.name}...\n==============")
        else:
            print(f"ERROR: You cannot travel {dir}. Try again.")
    def take_drop(self, cmd0, cmd1, rmv, ins):
        for i in rmv:
            if i.name.lower() == cmd1:
                rmv.remove(i)
                ins.append(i)
                tkdp = "drop" if cmd0[0] == 'd' else "take"
                msg = getattr(i, f"on_{tkdp}")()
                print(msg)
                break
        else:
            print(f"ERROR: '{cmd1}' isn't there. Try again.")
