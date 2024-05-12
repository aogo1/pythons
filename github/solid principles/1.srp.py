#single responsibility

#violate
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self):
        pass

    def save(self, animal):
        pass

#applying the singler responsibility
class Animal:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self) -> Animal:
        pass

    def save(self, animal: Animal):
        pass

