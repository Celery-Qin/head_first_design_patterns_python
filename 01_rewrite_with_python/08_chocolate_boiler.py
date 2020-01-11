class ChocolateBoiler():
    __unique_boiler = None # 设成私有的，外面不能访问
    
    def __new__(self):
        if self.__unique_boiler is None:
            self.__unique_boiler = super().__new__(self)
            print('Now you have a boiler!')
        else:
            print('You can only have ONE boiler!')
        return self.__unique_boiler

    def __init__(self):
        self.empty = True
        self.boiled = False 
        
    def fill(self):
        if self.empty == True and self.boiled == False:
            self.empty = False
            self.boiled = False
            print('The chocolate boiler is filled.')
        else:
            print('Please empty the boiler and stop boiling.')
    
    def drain(self):
        if self.empty == False and self.boiled == True:
            self.empty = True
            self.boiled = False
            print('The chocolate boilder is drained.')
        else:
            print('Only full and boiled boiler can be drained.')

    def boil(self):
        if self.empty == False and self.boiled == False:
            self.boiled = True
            print('The chocolate is boiling.')
        else:
            print('Only full and cold chocolate can be boiled.')


chocolate_boiler1 = ChocolateBoiler()
# chocolate_boiler1.__unique_boiler
chocolate_boiler2 = ChocolateBoiler()
print(chocolate_boiler1 == chocolate_boiler2)
chocolate_boiler1.fill()
chocolate_boiler1.boil()
chocolate_boiler1.drain()
chocolate_boiler1.drain()
chocolate_boiler1.boil()
chocolate_boiler1.empty = False
chocolate_boiler1.fill()

