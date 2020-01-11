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


class AbstractDuckFactory():
    def create_mallard_duck(self):
        return Quackable()

    def create_red_head_duck(self):
        return Quackable()

    def create_duck_call(self):
        return Quackable()

    def create_rubber_duck(self):
        return Quackable()


class Duckfactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return MallardDuck()

    def create_red_head_duck(self):
        return RedHeadDuck()

    def create_duck_call(self):
        return DuckCall()

    def create_rubber_duck(self):
        return RubberDuck()


class CountingDuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return QuackCounter(MallardDuck())

    def create_red_head_duck(self):
        return QuackCounter(RedHeadDuck())

    def create_duck_call(self):
        return QuackCounter(DuckCall())

    def create_rubber_duck(self):
        return QuackCounter(RubberDuck())


class DuckSimulator():
    def __init__(self, duck_factory):
        self.mallard_duck = duck_factory.create_mallard_duck()
        self.red_head_duck = duck_factory.create_red_head_duck()
        self.duck_call = duck_factory.create_duck_call()
        self.rubber_duck = duck_factory.create_rubber_duck()
        self.goose_adapter = GooseAdapter(Goose())

        self.simulate(self.mallard_duck)
        self.simulate(self.red_head_duck)
        self.simulate(self.duck_call)
        self.simulate(self.rubber_duck)
        self.simulate(self.goose_adapter)


    def simulate(self, duck):
        duck.quack()

duck_facoty = CountingDuckFactory()
duck_simulator = DuckSimulator(duck_facoty)
print('The ducks quacked {} times.'.format(QuackCounter.get_quacks(QuackCounter)))