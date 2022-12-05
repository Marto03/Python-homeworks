import random


class InvalidParameterError(Exception):
    def __init__(self, message="Invalid class parameter: name", name=""):
        self.name = name
        super().__init__(message)

        #print(message)
greshka = InvalidParameterError("Invalid class parameter: " "Ivan.") # Test
print(greshka) # Test

class InvalidAgeError(InvalidParameterError):
    def __init__(self, message="Invalid parameter: age", age=""):
        super().__init__(message)
        self.age = age

age = InvalidAgeError("Invalid parameter: " "20") # Test
print(age) # Test

class InvalidSoundError(InvalidParameterError):
    def __init__(self, message="Invalid parameter: sound", sound=""):
        super().__init__(message)
        self.sound = sound

sound = InvalidSoundError("Invalid parameter: " "Something") # Test
print(sound) # Test

class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
        if type(name) != str:
            raise InvalidParameterError("name")
        if type(age) != int:
            raise InvalidAgeError
        if type(sound) != str:
            raise InvalidSoundError

    def make_sound(self, name, sound):
        print(f"{name} says {sound}!")

    def print(self, name, age, sound):
        pass

    def daily_task(self, animals, name):
        pass

class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        counter = 0
        if age > 15:
            raise InvalidAgeError
        for chr in sound:
            if "r" in sound:
                counter += 1
        if counter < 2:
            raise InvalidSoundError

    def print(self, name, age, sound):
        print(f"Jaguar({name}, {age}, {sound})")

    def daily_task(self, animals, name):
        animal_1 = ("Topcho", 3, "fish")
        animal_2 = ("Ares", 2, "granules")
        animal_3 = ("Donald", 1, "seeds")
        animal_4 = ("Vihur", 7, "hay")
        animal_5 = ("Purko", 1, "fish")
        animal_6 = ("Reksi", 8, "granules")
        animal_7 = ("Golden", 2, "seeds")
        animal_8 = ("Spark", 11, "hay")
        animal_9 = ("Chubaka", 4, "granules")
        animal_10 = ("Leo", 14, "fish")
        list_1 = [animal_1, animal_2, animal_3, animal_4, animal_5, animal_6, animal_7, animal_8, animal_9, animal_10]
        if "Lemur" or "Human" in list_1:
            #list_1.remove("Lemur")
            print(f"{name} the Jaguar hunted down {animals} the {animal.__name__}")



jaguar = Jaguar("Petur", 3, "Rawwr") # Test
print(jaguar) # Test

class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 10:
            raise InvalidAgeError
        for chr in sound:
            if not "e":
                raise InvalidSoundError

    def print(self, name, age, sound):
        print(f"Lemur({name}, {age}, {sound})")

    def daily_task(self, name, fruits):
        self.fruits = fruits
        if fruits >= 10:
            fruits -= 10
            print(f"{name} the Lemur ate a full meal of 10 fruits")
            return fruits
        if fruits < 10:
            fruits -= fruits
            print(f"{name} the Lemur could only find {fruits} fruits")
            return 0
        if fruits <= 0:
            self.make_sound(name, sound)
            print(f"{name} the Lemur couldn't find anything to eat")
            return 0

class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 10:
            raise InvalidAgeError
        for chr in sound:
            if not "e":
                raise InvalidSoundError

    def print(self, name, age, sound):
        print(f"Human({name}, {age}, {sound})")

    def daily_task(self, animals, buildings):
        pass

class Building:
    def __init__(self, type):
        self.type = type



names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

rand = random.randint(1, 10)
for i in range(rand):
    if 1 <= rand <= 3:
        animal = Lemur
    elif 4 <= rand <= 7:
        animal = Jaguar
    else:
        animal = Human
#print(animal)
rand_age = random.randint(7, 20)
for age_random in range(rand_age):
    pass
#print(age_random)

fruits = 100
animals = []
#buildings = []

for x in range(10):
    animals.append(animal)
    animals.append(rand_age)
    animals.append(sounds)

print(f"The jungle now has {len(animals)} animals")
print(animals) # не дава random на всички а само веднъж и след това показва същото.

for anim in animals:
    Lemur.daily_task(Lemur, fruits, 100)
    Jaguar.daily_task(Jaguar, sounds, 20)
    Human.daily_task(names, animals, buildings="")

print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
#print(buildings)

# задачата не работи изцяло, малко ми остава, но не съм сигурен къде бъркам
