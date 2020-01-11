import pizza

class PizzaStore():
    def choose_type(self):
        pass

    def create_pizza(self,ingredients_factory):
        pizza_created = pizza.Pizza(ingredients_factory)
        return pizza_created
    
    def order_pizza(self,ingredients_factory):
        pizza_ordered = self.create_pizza(ingredients_factory)
        pizza_ordered.prepare()
        pizza_ordered.bake()
        pizza_ordered.cut()
        pizza_ordered.box()
        print('Your \"'+ pizza_ordered.name + '\" is ready!')


class NYPizzaStore(PizzaStore):
    def choose_type(self):
        type_num = int(input('请选择披萨类型： \n1. CheesePizza\n2. GreekPizza\n3. PepperoniPizza\n'))
        if type_num == 1:
            return 'NYStyleCheesePizza'
        elif type_num == 2:
            return 'NYStyleGreekPizza'
        elif type_num == 3:
            return 'NYStylePepperoniPizza'

    def create_pizza(self,ingredients_factory):
        pizza_type = self.choose_type()
        if pizza_type == 'NYStyleCheesePizza':
            pizza_created = pizza.NYStyleCheesePizza(ingredients_factory)
        elif pizza_type == 'NYStyleGreekPizza':
            pizza_created = pizza.NYStyleGreekPizza(ingredients_factory)
        elif pizza_type == 'NYStylePepperoniPizza':
            pizza_created = pizza.NYStylePepperoniPizza(ingredients_factory)  
        return pizza_created


class ChicagoPizzaStore(PizzaStore):
    def choose_type(self):
        type_num = int(input('请选择披萨类型： \n1. CheesePizza\n2. GreekPizza\n3. PepperoniPizza\n'))
        if type_num == 1:
            return 'ChicagoStyleCheesePizza'
        elif type_num == 2:
            return 'ChicagoStyleGreekPizza'
        elif type_num == 3:
            return 'ChicagoStylePepperoniPizza'

    def create_pizza(self,ingredients_factory):
        pizza_type = self.choose_type()
        if pizza_type == 'ChicagoStyleCheesePizza':
            pizza_created = pizza.ChicagoStyleCheesePizza(ingredients_factory)
        elif pizza_type == 'ChicagoStyleGreekPizza':
            pizza_created = pizza.ChicagoStyleGreekPizza(ingredients_factory)
        elif pizza_type == 'ChicagoStylePepperoniPizza':
            pizza_created = pizza.ChicagoStylePepperoniPizza(ingredients_factory)  
        return pizza_created
