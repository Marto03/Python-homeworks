class Person:
    def __init__(self, name, last_name, age, nationality):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality

    def print_1(self):
        print(f"My name is {self.name} {self.last_name} and I'm {self.nationality}.")

first_person = Person("Maritn", "Aleksandrov", "19", "Bulgarian")
second_person = Person("Petur", "Petkov", "23", "Italian")
third_person = Person("Alex", "Petkov", "20", "Bulgarian")
#list_1 = []
#list_1.append(first_person.name)
#list_1.append(first_person.nationality)
#list_1.append(second_person.name)
#list_1.append(second_person.nationality)
#list_1.append(third_person.name)
#list_1.append(third_person.nationality)
first_person.print_1()