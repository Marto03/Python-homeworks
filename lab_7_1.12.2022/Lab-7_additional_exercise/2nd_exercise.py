class InvalidParameterError(Exception):
    pass


class NutrientError(Exception):
    pass

class InvalidFoodError(Exception):
    pass

class Food():
    def __init__(self, carbs, protein, fats, salt):
        self.carbs = float(carbs)
        self.protein = float(protein)
        self.fats = float(fats)
        self.salt = float(salt)
        if type(carbs) != float or type(protein) != float or type(fats) != float or type(salt) != float:
           raise InvalidParameterError
        if carbs > 100 or protein > 100 or fats > 100 or salt > 100:
            raise NutrientError
        if carbs == 0 and protein == 0 and fats == 0 and salt == 0:
            raise InvalidFoodError
    def print_label(self):
        print(f"Food{self.carbs, self.protein, self.fats, self.salt}")
#pizza = Food(3.2, 4.3, 6.1, 4.8)
#pizza.print_label()

#try:
#    pizza = Food(3.2, 4.2, 6.1, 4.8)
#    pizza.print_label()

#except InvalidParameterError:
#    print("Wrong")
for i in range(0, 120, 10):
    try:
        pizza = Food(3.4, 78.3, 23.4, 56.1)

        meat = Food(42.3, 20.8, 97.1, 2.3)
    except InvalidParameterError:
        print("Invalid parameter")
    except NutrientError:
        print("NutrientError")
    except InvalidFoodError:
        print("Invalid food")
    else:
        pizza.print_label()
        meat.print_label()
