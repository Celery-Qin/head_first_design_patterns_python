import ingredients_factory
import time

class Pizza():

    def __init__(self, ingredients_factory_instance):
        if isinstance(ingredients_factory_instance,ingredients_factory.Ingredientfactory):
            self.ingredients_factory = ingredients_factory_instance
            self.dough = self.ingredients_factory.dough # 面团
            self.sauce = self.ingredients_factory.sauce # 酱料
            self.veggies = self.ingredients_factory.veggies
            self.cheese = self.ingredients_factory.cheese
            self.pepperoni = self.ingredients_factory.pepperoni
            self.clams = self.ingredients_factory.clams
        else:
            print('please input a Ingredientfactory')
        self.name = 'pizza name' # 名称
        
    def prepare(self):
        time.sleep(1)
        print('Prepare ' + self.name)
        time.sleep(1)
        print('Tossing ' + self.dough)
        time.sleep(1)
        print('Adding ' + self.sauce)
        time.sleep(1)
        print('Adding Veggies:' )
        for veggie in self.veggies:
            print(veggie,end=' ')
        time.sleep(1)
        print('Adding ' + self.cheese)
        time.sleep(1)
        print('Adding ' + self.pepperoni)
        time.sleep(1)
        print('Adding ' + self.clams)

    def bake(self):
        time.sleep(1)
        print('Bake for 25 minutes at ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    def cut(self):
        time.sleep(1)
        print('Cutting the pizza into diagonal slices')

    def box(self):
        time.sleep(1)
        print('Place the pizza into the official PizzaStore box')


class NYStyleCheesePizza(Pizza):
    def __init__(self,ingredients_factory_instance):
        if isinstance(ingredients_factory_instance,ingredients_factory.NYIngredientfactory):
            Pizza.__init__(self,ingredients_factory_instance)
        else:
            print('please input a NYIngredientfactory')
        self.name = 'NY Style Sauce and Cheese Pizza' # 名称
        

class NYStyleGreekPizza(Pizza):
    def __init__(self,ingredients_factory_instance):
        if isinstance(ingredients_factory_instance,ingredients_factory.NYIngredientfactory):
            Pizza.__init__(self,ingredients_factory_instance)
        else:
            print('please input a NYIngredientfactory')
        self.name = 'NY Style Sauce Greek Pizza' # 名称
        

class NYStylePepperoniPizza(Pizza):
    def __init__(self,ingredients_factory_instance):
        if isinstance(ingredients_factory_instance,ingredients_factory.NYIngredientfactory):
            Pizza.__init__(self,ingredients_factory_instance)
        else:
            print('please input a NYIngredientfactory')
        self.name = 'NY Style Sauce Pepperoni Pizza' # 名称
    

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self,ingredients_factory_instance):
        if isinstance(ingredients_factory_instance,ingredients_factory.ChicagoIngredientfactory):
            Pizza.__init__(self,ingredients_factory_instance)
        else:
            print('please input a ChicagoIngredientfactory')
        self.name = 'Chicago Style Sauce and Cheese Pizza' # 名称
        

class ChicagoStyleGreekPizza(Pizza):
    def __init__(self,ingredients_factory_instance):
        if isinstance(ingredients_factory_instance,ingredients_factory.ChicagoIngredientfactory):
            Pizza.__init__(self,ingredients_factory_instance)
        else:
            print('please input a ChicagoIngredientfactory')
        self.name = 'Chicago Style Sauce Greek Pizza' # 名称
        

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self,ingredients_factory_instance):
        if isinstance(ingredients_factory_instance,ingredients_factory.ChicagoIngredientfactory):
            Pizza.__init__(self,ingredients_factory_instance)
        else:
            print('please input a ChicagoIngredientfactory')
        self.name = 'Chicago Style Sauce Pepperoni Pizza' # 名称
        

