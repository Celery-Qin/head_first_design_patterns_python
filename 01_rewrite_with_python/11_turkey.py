class Duck():
    def quack(self):
        pass

    def fly(self):
        pass

class MallardDuck(Duck):
    def quack(self):
        print('Quack!')

    def fly(self):
        print('I\'m flying!')

class Turkey():
    def gobble(self):
        pass

    def fly(self):
        pass

class WildTurkey(Turkey):
    def gobble(self):
        print('Gobble gobble!')

    def fly(self):
        print('I\'m flying a short distance.')

class TurkeyAdapter(Duck):
    def __init__(self,turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()

print('The wild turkey says:')
wild_turkey = WildTurkey()
wild_turkey.fly()
wild_turkey.gobble()

print('The mallard duck says:')
mallard_duck = MallardDuck()
mallard_duck.fly()
mallard_duck.quack()

print('The turkey adapter says:')
turkey_adapter = TurkeyAdapter(wild_turkey)
turkey_adapter.fly()
turkey_adapter.quack()