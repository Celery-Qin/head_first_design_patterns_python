
class Quackable():
    def quack(self):
        pass


class Flock(Quackable):
    def __init__(self):
        self.quackers = list()
        # self.len = self.quackers.__len__()
        self.current_position = 0

    def __iter__(self):
        return iter(self.quackers)

    def __next__(self): 
    # Python3中只能使用__next__()而Python2中只能命名为next()
        quacker = self.quackers[self.current_position]
        self.current_position +=1
        return quacker

    def __has_next__(self):
        if (self.current_position >= self.quackers.__len__()) or (self.quackers.__len__() == 0):
            return False
        else:
            return True    
    
    def add(self, quacker):
        self.quackers.append(quacker)

    def quack(self):
        while self.__has_next__():
            self.__next__().quack()


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
        # 创建一群Mallards
        self.mallard_duck1 = duck_factory.create_mallard_duck()
        self.mallard_duck2 = duck_factory.create_mallard_duck()
        self.mallard_duck3 = duck_factory.create_mallard_duck()
        self.mallard_duck4 = duck_factory.create_mallard_duck()
        self.flock_of_mallards = Flock()
        self.flock_of_mallards.add(self.mallard_duck1)
        self.flock_of_mallards.add(self.mallard_duck2)
        self.flock_of_mallards.add(self.mallard_duck3)
        self.flock_of_mallards.add(self.mallard_duck4)

        # 创建一群其他鸭子
        self.red_head_duck = duck_factory.create_red_head_duck()
        self.duck_call = duck_factory.create_duck_call()
        self.rubber_duck = duck_factory.create_rubber_duck()
        self.goose_adapter = GooseAdapter(Goose())
        self.flock_of_ducks = Flock()
        self.flock_of_ducks.add(self.red_head_duck)
        self.flock_of_ducks.add(self.duck_call)
        self.flock_of_ducks.add(self.rubber_duck)
        self.flock_of_ducks.add(self.goose_adapter)

        self.simulate(self.flock_of_mallards)
        self.simulate(self.flock_of_ducks)
        print('The ducks quacked {} times.'.format(QuackCounter.get_quacks(QuackCounter)))

    def simulate(self, duck):
        duck.quack()

duck_facoty = CountingDuckFactory()
duck_simulator = DuckSimulator(duck_facoty)
# print('The ducks quacked {} times.'.format(QuackCounter.get_quacks(QuackCounter)))