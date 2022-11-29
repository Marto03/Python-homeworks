class Vehicle:
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers):

        self.brand = brand
        self.model = model
        self.engine_vol = engine_vol
        self.max_speed = max_speed
        self.total_km = total_km
        self.max_passengers = max_passengers
    def print_info(self):
        print(f"Vehicle{self.brand, self.model, self.engine_vol, self.max_speed, self.total_km, self.max_passengers}")

vehicle = Vehicle("Golf", "mk3", 1.6, 180, 112435, 5)
vehicle_1 = Vehicle("Subaru", "Impreza", 2.0, 220, 347231, 4)
vehicle_2 = Vehicle("Audi", "TT", 2.8, 260, 520340, 2)
vehicle_3 = Vehicle("Opel", "Corsa", 1.2, 120, 680962, 4)

class Motorbike(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, price, basket):
        super().__init__(brand, model, engine_vol, max_speed, total_km, None)
        self.price = price
        self.basket = basket
    def print_info(self):
        print(f"Motor{self.brand, self.model, self.engine_vol, self.max_speed, self.total_km, self.price, self.basket}")

motor = Motorbike("Yamaha", "T-max", 50, 120, 152786, 12600, True)

class Car(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, category, type_fuel):
        super().__init__(brand, model, engine_vol, max_speed, total_km, None)
        self.category = category
        self.type_fuel = type_fuel
    def print_info(self):
        print(f"Car{self.brand, self.model, self.engine_vol, self.max_speed, self.total_km, self.category, self.type_fuel}")

car = Car("Nissan", "Skyline Gtr r34", 2.6, 250, 467834, "coupe", "petrol")
car_1 = Car("Toyota", "Aygo", 1.4, 140, 730120, "hatchback", "petrol")
car_2 = Car("Toyota", "Supra", 3.0, 300, 410253, "hatchback", "petrol")
car_3 = Car("BMW", "m5 competition", 4.4, 250, 234786, "sedan", "petrol")



class Bus(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers, firm, year_of_production):
        super().__init__(brand, model, engine_vol, max_speed, total_km, max_passengers)
        self.firm = firm
        self.year_of_production = year_of_production
    def print_info(self):
        print(f"Bus{self.brand, self.model, self.engine_vol, self.max_speed, self.total_km, self.max_passengers, self.firm, self.year_of_production}")

bus = Bus("Citroen", "Jumper", 3.0, 120, 450000, 8, "Ekont", 2006)

vehicle.print_info()
vehicle_1.print_info()
vehicle_2.print_info()
vehicle_3.print_info()
motor.print_info()
car.print_info()
car_1.print_info()
car_2.print_info()
car_3.print_info()
bus.print_info()


list_1 = []

list_1.append(vehicle.brand)
list_1.append(vehicle_1.brand)
list_1.append(vehicle_2.brand)
list_1.append(vehicle_3.brand)
list_1.append(motor.brand)
list_1.append(car.brand)
list_1.append(car_1.brand)
list_1.append(car_2.brand)
list_1.append(car_3.brand)
list_1.append(bus.brand)

print(list_1)
