import time
# ---------------- Pizza ---------------- #

class Pizza():

    def __init__(self):
        self.type = 'Unknown'
        self.name = 'pizza name' # 名称
        self.dough = 'dough' # 面团
        self.sauce = 'sauce' # 酱料
        self.toppings = list() # 佐料
        
    def prepare(self):
        time.sleep(1)
        print('Prepare ' + self.name)
        time.sleep(1)
        print('Tossing ' + self.dough)
        time.sleep(1)
        print('Adding ' + self.sauce)
        time.sleep(1)
        print('Adding Toppings:' )
        for topping in self.toppings:
            print(topping)

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
    def __init__(self):
        self.type = 'NYStyleCheesePizza'
        self.name = 'NY Style Sauce and Cheese Pizza' # 名称
        self.dough = 'Thin Crust Dough' # 面团
        self.sauce = 'Marinara Sauce' # 酱料
        self.toppings = ['Grated Reggiano Cheese'] # 佐料

class NYStyleGreekPizza(Pizza):
    def __init__(self):
        self.type = 'NYStyleGreekPizza'
        self.name = 'NY Style Sauce Greek Pizza' # 名称
        self.dough = 'Thin Crust Dough' # 面团
        self.sauce = 'Marinara Sauce' # 酱料
        self.toppings = ['Grated Reggiano Cheese'] # 佐料

class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        self.type = 'NYStylePepperoniPizza'
        self.name = 'NY Style Sauce Pepperoni Pizza' # 名称
        self.dough = 'Thin Crust Dough' # 面团
        self.sauce = 'Marinara Sauce' # 酱料
        self.toppings = ['Grated Reggiano Cheese'] # 佐料

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.type = 'ChicagoStyleCheesePizza'
        self.name = 'Chicago Style Sauce and Cheese Pizza' # 名称
        self.dough = 'Thick Crust Dough' # 面团
        self.sauce = 'Plum Tomato Sauce' # 酱料
        self.toppings = ['Shredded Mozzarella Cheese'] # 佐料

class ChicagoStyleGreekPizza(Pizza):
    def __init__(self):
        self.type = 'ChicagoStyleGreekPizza'
        self.name = 'Chicago Style Sauce Greek Pizza' # 名称
        self.dough = 'Thick Crust Dough' # 面团
        self.sauce = 'Plum Tomato Sauce' # 酱料
        self.toppings = ['Shredded Mozzarella Cheese'] # 佐料

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        self.type = 'ChicagoStylePepperoniPizza'
        self.name = 'Chicago Style Sauce Pepperoni Pizza' # 名称
        self.dough = 'Thick Crust Dough' # 面团
        self.sauce = 'Plum Tomato Sauce' # 酱料
        self.toppings = ['Shredded Mozzarella Cheese'] # 佐料


# ---------------- Store ---------------- #

class PizzaStore():
    def choose_type(self):
        pass

    def create_pizza(self):
        pizza = Pizza()
        return pizza
    
    def order_pizza(self):
        pizza = self.create_pizza()
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        print('Your '+ pizza.type + ' Pizza is ready!')


class NYPizzaStore(PizzaStore):
    def choose_type(self):
        type_num = int(input('请选择披萨类型： \n1. NYStyleCheesePizza\n2. NYStyleGreekPizza\n3. NYStylePepperoniPizza\n'))
        if type_num == 1:
            return 'NYStyleCheesePizza'
        elif type_num == 2:
            return 'NYStyleGreekPizza'
        elif type_num == 3:
            return 'NYStylePepperoniPizza'

    def create_pizza(self):
        pizza_type = self.choose_type()
        if pizza_type == 'NYStyleCheesePizza':
            pizza = NYStyleCheesePizza()
        elif pizza_type == 'NYStyleGreekPizza':
            pizza = NYStyleGreekPizza()
        elif pizza_type == 'NYStylePepperoniPizza':
            pizza = NYStylePepperoniPizza()  
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def choose_type(self):
        type_num = int(input('请选择披萨类型： \n1. ChicagoStyleCheesePizza\n2. ChicagoStyleGreekPizza\n3. ChicagoStylePepperoniPizza\n'))
        if type_num == 1:
            return 'ChicagoStyleCheesePizza'
        elif type_num == 2:
            return 'ChicagoStyleGreekPizza'
        elif type_num == 3:
            return 'ChicagoStylePepperoniPizza'

    def create_pizza(self):
        pizza_type = self.choose_type()
        if pizza_type == 'ChicagoStyleCheesePizza':
            pizza = ChicagoStyleCheesePizza()
        elif pizza_type == 'ChicagoStyleGreekPizza':
            pizza = ChicagoStyleGreekPizza()
        elif pizza_type == 'ChicagoStylePepperoniPizza':
            pizza = ChicagoStylePepperoniPizza()  
        return pizza

# ---------------- Test ---------------- #

ny_pizza_store = NYPizzaStore()
ny_pizza_store.order_pizza()

chicago_pizza_store = ChicagoPizzaStore()
chicago_pizza_store.order_pizza()
