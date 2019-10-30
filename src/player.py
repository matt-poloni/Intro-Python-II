# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name: str, current_room):
        self.name = name
        self.current_room = current_room
    # def __str__(self):
    #     pass
    def __repr__(self):
        return f"Player({repr(self.name)}, {repr(self.current_room)})"