# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return f"{self.name}: {self.description}"
    def __repr__(self):
        return f"Room({repr(self.name)}, {repr(self.description)})"