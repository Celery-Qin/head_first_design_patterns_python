# ---------------- Pizza ---------------- #

class Pizza():

    def __init__(self):
        self.type = 'Unknown'
        
    def prepare(self):
        return 'The pizza is prepared.\n'

    def bake(self):
        return 'The pizza is baked.\n'

    def cut(self):
        return 'The pizza is cut.\n'

    def box(self):
        return 'The pizza has put into a box.\n'


class CheesePizza(Pizza):
    def __init__(self):
        self.type = 'Cheese'

class GreekPizza(Pizza):
    def __init__(self):
        self.type = 'Greek'

class PepperoniPizza(Pizza):
    def __init__(self):
        self.type = 'Pepperoni'


# ---------------- Factory ---------------- #

class PizzaFactory():

    def choose_type(self):
        type_num = int(input('请选择披萨类型： \n1. Cheese\n2. Greek\n3. Pepperoni\n'))
        if type_num == 1:
            return 'Cheese'
        elif type_num == 2:
            return 'Greek'
        elif type_num == 3:
            return 'Pepperoni'

    def create_pizza(self):
        pizza_type = self.choose_type()
        if pizza_type == 'Cheese':
            pizza = CheesePizza()
        elif pizza_type == 'Greek':
            pizza = GreekPizza()
        elif pizza_type == 'Pepperoni':
            pizza = PepperoniPizza()  
        return pizza


# ---------------- Store ---------------- #

class PizzaStore():
    def __init__(self,factory):
        self.factory = factory
    
    def order_pizza(self):
        pizza = self.factory.create_pizza()
        print(pizza.prepare())
        print(pizza.bake())
        print(pizza.cut())
        print(pizza.box())
        return pizza


# ---------------- Test ---------------- #
factory = PizzaFactory()
pizza_store = PizzaStore(factory)
pizza = pizza_store.order_pizza()
print('Your '+ pizza.type + ' Pizza is ready!')
