import random
class Animal:
    def __init__(self, name, years, type_food):
        self.name = name
        self.years = years
        self.type_food = type_food
    def make_sound(self):
        pass
    def eat_food(self, eat_food):
        pass

class Cat(Animal):
    def __init__(self, name, years, type_food):
        super().__init__(name, years, type_food)

    def make_sound(self):
        print("Meow!")

    def eat_food(self, eat_food):
        if eat_food == 0:
            for i in range(4):
                self.make_sound()

            if 0< eat_food < 10:
                for i in range(2):
                    self.make_sound()
            return 0
        return eat_food - 10

class Dog(Animal):
    def __init__(self, name, years, type_food):
        super().__init__(name, years, type_food)


    def make_sound(self):
        print("Bark!")

    def eat_food(self, eat_food, eat_quantity=5):
        if eat_food > eat_quantity:
            return eat_food - eat_quantity
        self.make_sound()
        return 0

class Duck(Animal):
    def __init__(self, name, years, type_food):
        super().__init__(name, years, type_food)

    def make_sound(self):
        print("Quack!")

    def eat_food(self, eat_food):
        self.make_sound()
        number = random.randint(1,9)
        if eat_food > number:
            return eat_food - number
        return 0

class Horse(Animal):
    def __init__(self, name, years, type_food):
        super().__init__(name, years, type_food)

    def make_sound(self):
        print("Neigh!")
    def eat_food(self, eat_food):
        if 30 > eat_food > 8:
            return eat_food - 8
        if eat_food > 30:
            return eat_food - 15

        if eat_food == 0:
             self.make_sound()
        return 0

animal_1 = Cat("Topcho", 3, "fish")
animal_2 = Dog("Ares", 2, "granules")
animal_3 = Duck("Donald", 1, "seeds")
animal_4 = Horse("Vihur", 7, "hay")
animal_5 = Cat("Purko", 1, "fish")
animal_6 = Dog("Reksi", 8, "granules")
animal_7 = Duck("Golden", 2, "seeds")
animal_8 = Horse("Spark", 11, "hay")
animal_9 = Dog("Chubaka", 4, "granules")
animal_10 = Cat("Leo", 14, "fish")
list_1 = [animal_1, animal_2, animal_3, animal_4, animal_5, animal_6, animal_7, animal_8, animal_9, animal_10]

food = {"fish": 150, "granules": 42, "seeds": 720, "hay": 50}

for i in list_1:
    print("============")
    for x in range(len(list_1)):
        food_quantity = food[i.type_food]
        food[i.type_food] = i.eat_food(food_quantity)
        print(f"{i.name} the {type(i).__name__} just ate {food_quantity - food[i.type_food]} {i.type_food}, there's {food[i.type_food]} left")
