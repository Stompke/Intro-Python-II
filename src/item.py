class Item:
    def __init__(self, name, description, value = 0):
        self.name = name
        self.description = description
        self.worth = value
    def __str__(self):
        print(f"{self.name}: {self.description}")

