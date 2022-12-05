class InvalidParameterError(Exception):
    pass


class NutrientError(Exception):
    pass

class InvalidFoodError(Exception):
    pass

class Food():
    def __init__(self, carbs, protein, fats, salt):
        self.carbs = carbs
        self.protein = protein
        self.fats = fats
        self.salt = salt
        if carbs != float or protein != float or fats != float or salt != float:
            raise InvalidParameterError
    def print_label(self):
        print(f"Food{self.carbs, self.protein, self.fats, self.salt}")
#pizza = Food(3.2, 4.3, 6.1, 4.8)
#pizza.print_label()
try:
    pizza = Food(3.2, 4.2, 6.1, 4.8)
    pizza.print_label()
except InvalidParameterError:
    print("Wrong")
