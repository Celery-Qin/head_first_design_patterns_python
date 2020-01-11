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

class Adapter(MallardDuck, WildTurkey):
    def __init__(self, bird):
        if isinstance(bird, MallardDuck):
            self.duck = bird
            self.turkey = None
        elif isinstance(bird, WildTurkey):
            self.turkey = bird
            self.duck = None

    def quack(self):
        self.turkey.gobble()

    def gobble(self):
        self.duck.quack()

    def fly(self):
        if self.turkey:
            self.turkey.fly()
            self.turkey.fly()
            self.turkey.fly()
        elif self.duck:
            self.duck.fly()
            print('a short distance.')

print('The wild turkey says:')
wild_turkey = WildTurkey()
wild_turkey.fly()
wild_turkey.gobble()
print('-----------------------------')

print('The mallard duck says:')
mallard_duck = MallardDuck()
mallard_duck.fly()
mallard_duck.quack()
print('-----------------------------')

print('The turkey adapter says:')
turkey_adapter = Adapter(wild_turkey)
turkey_adapter.fly()
turkey_adapter.quack()
print('-----------------------------')

print('The duck adapter says:')
duck_adapter = Adapter(mallard_duck)
duck_adapter.fly()
duck_adapter.gobble()
print('-----------------------------')