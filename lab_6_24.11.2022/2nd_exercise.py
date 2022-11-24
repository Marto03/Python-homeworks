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

#students = []
x = Student("Martin", "Aleksandrov", "18", "Bulgarian", "Technical University", "2022")
y = Person("Alex", "Petkov", "19", "Bulgarian")
z = Student("Atanas", "Kalev", "18", "Bulgarian", "Technical University", "2022")
c = Student("Luchezar", "Dimitrov", "19", "Bulgarian", "Technical University", "2022")
#students.append(x)
#students.append(y)
#students.append(z)
#students.append(c)
x.print()
y.print()
z.print()
c.print()
