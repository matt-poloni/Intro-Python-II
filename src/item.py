class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    # def __str__(self):
    #     pass
    def __repr__(self):
        return f"Item({self.name}, {self.description})"