# ---------------- Component ---------------- #

class Beverage():
    def __init__(self):
        self.description = 'Unknown Beverage'

    def get_description(self):
        return self.description

    def cost(self):
        pass

# ---------------- Concrete Component ---------------- #

class HouseBlend(Beverage):
    def __init__(self):
        self.description = 'House Blend Coffee'

    def cost(self):
        return 0.89


class DarkRoast(Beverage):
    def __init__(self):
        self.description = 'Dark Roast Coffee'

    def cost(self):
        return 0.99


class Decaf(Beverage):
    def __init__(self):
        self.description = 'Decaf'

    def cost(self):
        return 1.09


class Espresso(Beverage):
    def __init__(self):
        self.description = 'Espresso'

    def cost(self):
        return 1.99


# ---------------- Decorator ---------------- #

class CondimentDecorator(Beverage):
    def __init__(self,beverage):
        self.beverage = beverage
        self.description = 'Unknown Condiment'

    def get_description(self):
        return self.beverage.get_description() + ' , ' +self.description

    def cost(self):
        pass


# ---------------- Concrete Decorator ---------------- #

class Milk(CondimentDecorator):
    def __init__(self,beverage):
        CondimentDecorator.__init__(self, beverage)
        self.description = 'Milk'

    def cost(self):
        return 0.2 + self.beverage.cost()


class Mocha(CondimentDecorator):
    def __init__(self,beverage):
        CondimentDecorator.__init__(self, beverage)
        self.description = 'Mocha'

    def cost(self):
        return 0.1 + self.beverage.cost()


class Soy(CondimentDecorator):
    def __init__(self,beverage):
        CondimentDecorator.__init__(self, beverage)
        self.description = 'Soy'

    def cost(self):
        return 0.3 + self.beverage.cost()


class Whip(CondimentDecorator):
    def __init__(self,beverage):
        CondimentDecorator.__init__(self, beverage)
        self.description = 'Whip'

    def cost(self):
        return 0.4 + self.beverage.cost()


# ---------------- Concrete Decorator ---------------- #

# 订一杯不加调料的Espresso，打印出描述和价格
beverage1 = Espresso()
print('Description is : {}'.format(beverage1.get_description()))
print('Cost is : {:.2f}'.format(beverage1.cost()))
print('\n\n')

# 订一杯DarkRoast，加两份mocha和一份whip，打印出描述和价格
beverage2 = DarkRoast()
beverage2 = Mocha(beverage2)
beverage2 = Mocha(beverage2)
beverage2 = Whip(beverage2)
print('Description is : {}'.format(beverage2.get_description()))
print('Cost is : {:.2f}'.format(beverage2.cost()))
print('\n\n')

# 订一杯HouseBlend，加一份soy、一份mocha、一份whip，打印出描述和价格
beverage3 = HouseBlend()
beverage3 = Soy(beverage3)
beverage3 = Mocha(beverage3)
beverage3 = Whip(beverage3)
print('Description is : {}'.format(beverage3.get_description()))
print('Cost is : {:.2f}'.format(beverage3.cost()))
print('\n\n')