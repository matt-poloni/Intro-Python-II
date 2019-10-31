class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f"{self.name}"
    def __repr__(self):
        return f"Item({repr(self.name)}, {repr(self.description)})"
    def on_take(self):
        return f"You have picked up {self.name}"
    def on_drop(self):
        return f"You have dropped {self.name}"

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
    # def __str__(self):
    #     pass
    def __repr__(self):
        return f"LightSource({repr(self.name)}, {repr(self.description)})"
    def on_drop(self):
        print("It's not wise to drop your source of light!")
        super().on_drop()
