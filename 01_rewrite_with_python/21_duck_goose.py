class Quackable():
    def quack(self):
        pass


class QuackCounter(Quackable):
    num_of_quacks = 0

    def __init__(self, duck):
        self.duck = duck

    def quack(self):
        self.duck.quack()
        QuackCounter.num_of_quacks += 1

    def get_quacks(self):
        return QuackCounter.num_of_quacks


class MallardDuck(Quackable):
    def quack(self):
        print('Quack!')


class RedHeadDuck(Quackable):
    def quack(self):
        print('Quack!')


class DuckCall(Quackable):
    def quack(self):
        print('Kwak!')


class RubberDuck(Quackable):
    def quack(self):
        print('Squeak!')

class Goose():
    def honk(self):
        print('Honk!')


class GooseAdapter(Quackable):
    def __init__(self, goose):
        self.goose = goose

    def quack(self):
        self.goose.honk()

class DuckSimulator():
    def __init__(self):
        self.mallard_duck = QuackCounter(MallardDuck())
        self.red_head_duck = QuackCounter(RedHeadDuck())
        self.duck_call = QuackCounter(DuckCall())
        self.rubber_duck = QuackCounter(RubberDuck())
        # self.goose = Goose()
        self.goose_adapter = GooseAdapter(Goose())

        self.simulate(self.mallard_duck)
        self.simulate(self.red_head_duck)
        self.simulate(self.duck_call)
        self.simulate(self.rubber_duck)
        self.simulate(self.goose_adapter)


    def simulate(self, duck):
        duck.quack()

duck_simulator = DuckSimulator()
print('The ducks quacked {} times.'.format(QuackCounter.get_quacks(QuackCounter)))