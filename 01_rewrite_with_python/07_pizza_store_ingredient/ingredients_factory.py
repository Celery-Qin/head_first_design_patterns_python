class Ingredientfactory():
    def __init__(self):
        self.dough = self.create_dough()
        self.sauce = self.create_sauce()
        self.cheese = self.create_cheese()
        self.veggies = self.create_veggies()
        self.pepperoni = self.create_pepperoni()
        self.clams = self.create_clams()

    def create_dough(self):
        return 'dough'

    def create_sauce(self):
        return 'sauce'

    def create_cheese(self):
        return 'cheese'

    def create_veggies(self):
        return ['veggie']

    def create_pepperoni(self):
        return 'pepperoni'

    def create_clams(self):
        return 'clams'

class NYIngredientfactory(Ingredientfactory):
    def create_dough(self):
        return 'Thin Crust Dough'

    def create_sauce(self):
        return 'Marinara Sauce'

    def create_cheese(self):
        return 'Reggiano Cheese'

    def create_veggies(self):
        return ['Garlic', 'Mushroom', 'Onion', 'Redpepper']

    def create_pepperoni(self):
        return 'Sliced Pepperoni'

    def create_clams(self):
        return 'Fresh Clams'
		
class ChicagoIngredientfactory(Ingredientfactory):
    def create_dough(self):
        return 'Thick Crust Dough'

    def create_sauce(self):
        return 'Chicago Sauce'

    def create_cheese(self):
        return 'Chicago Cheese'

    def create_veggies(self):
        return ['Garlic', 'Mushroom', 'Onion', 'Redpepper']

    def create_pepperoni(self):
        return 'Chicago Pepperoni'

    def create_clams(self):
        return 'Frozen Clams'
		