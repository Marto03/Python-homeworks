class Person:
    def __init__(self, name, last_name, age, nationality):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
    def print(self):
        print(f"I'm {self.name} {self.last_name}, {self.age} years old, {self.nationality}")

class Student(Person):
    def __init__(self, name, last_name, age, nationality, university, yearofstudy):
        super().__init__(name, last_name, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy
    def print(self):
        print(f"I'm {self.name} {self.last_name}, {self.age} years old, {self.nationality}. I'm student in {self.university} from {self.yearofstudy}.")

class Lecturer(Person):
    def __init__(self, name, last_name, age, nationality, university, experience):
        super().__init__(name, last_name, age, nationality)
        self.univerity = university
        self.experience = experience

    def print(self):
        print(f"I'm {self.name} {self.last_name}, {self.age} years old, {self.nationality}. I'm lecturer in {self.univerity} with {self.experience} years of experience.")

x = Lecturer("Martin", "Aleksandrov", 18, "Bulgarian", "Technical University", 3)
y = Student("Alex", "Petkov", "19", "Bulgarian", "Technical University", "2022")
z = Person("Atanas", "Kalev", "18", "Bulgarian")
c = Student("Luchezar", "Dimitrov", "19", "Bulgarian", "Technical University", "2022")

x.print()
y.print()
z.print()
