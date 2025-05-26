class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        print(f"{self.name} the {self.species} is eating.")

    def sleep(self):
        print(f"{self.name} the {self.species} is sleeping.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")


class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cow")

    def make_sound(self):
        print(f"{self.name} says Moo!")

    def produce_milk(self):
        print(f"{self.name} is producing milk.")


class Pig(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Pig")

    def make_sound(self):
        print(f"{self.name} says Oink!")

    def roll_in_mud(self):
        print(f"{self.name} is rolling in the mud.")


class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Chicken")

    def make_sound(self):
        print(f"{self.name} says Cluck!")

    def lay_egg(self):
        print(f"{self.name} laid an egg.")

class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        print(f"Added {animal.name} the {animal.species} to the farm.")

    def show_all_animals(self):
        print("\n--- Farm Animals ---")
        for animal in self.animals:
            print(f"{animal.name} ({animal.species}), Age: {animal.age}")

    def make_all_sounds(self):
        print("\n--- Animal Sounds ---")
        for animal in self.animals:
            animal.make_sound()
    def remove_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                print(f"Removed {animal.name} the {animal.species} from the farm.")
                return
        print(f"No animal named {name} found on the farm.")
