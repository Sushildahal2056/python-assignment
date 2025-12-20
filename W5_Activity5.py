class Animal:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Animal Name: {self.name}")


class Mammal(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature


class Bird(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature


class Fish(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature


class Dog(Mammal):
    def walk(self):
        print(f"{self.name} walks on four legs")


class Cat(Mammal):
    def walk(self):
        print(f"{self.name} walks silently")


class Eagle(Bird):
    def fly(self):
        print(f"{self.name} flies very high")


class Penguin(Bird):
    def swim(self):
        print(f"{self.name} swims but cannot fly.")


class Salmon(Fish):
    def swim(self):
        print(f"{self.name} swims upstream.")


class Shark(Fish):
    def swim(self):
        print(f"{self.name} swims fast and hunts prey.")


def main():
    dog = Dog("Dog", "Has fur")
    cat = Cat("Cat", "Has fur")
    eagle = Eagle("Eagle", "Has wings")
    penguin = Penguin("Penguin", "Has wings")
    salmon = Salmon("Salmon", "Has fins")
    shark = Shark("Shark", "Has fins")

    dog.walk()
    cat.walk()
    eagle.fly()
    penguin.swim()
    salmon.swim()
    shark.swim()


if __name__ == "__main__":
    main()
