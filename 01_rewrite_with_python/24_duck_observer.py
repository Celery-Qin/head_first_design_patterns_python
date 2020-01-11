class QuackObservable():
    # 通用的可被观察对象的类
    # def __init__(self):
    #     self.observers = list()

    def register_observer(self, observer):
        # self.observers.append(observer)
        pass

    def notify_observers(self):
        pass

class Observabel(QuackObservable):
    # 辅助类，用它来实现功能
    def __init__(self, duck):
        self.observers = list()
        self.duck = duck

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.duck)

class Quackable(QuackObservable):
    # 所有呱呱叫对象都是可被观察的，所以继承一下
    def quack(self):
        pass


class Flock(Quackable):
    def __init__(self):
        self.quackers = list()
        print('Flock 创建完成！')
    
    def add(self, quacker):
        self.quackers.append(quacker)
        print('添加了呱呱叫对象{}'.format(quacker.__str__()))

    def quack(self):
        for quacker in self.quackers:
            quacker.quack()

    def register_observer(self, observer):
        for quacker in self.quackers:
            quacker.register_observer(observer)

    def notify_observers(self):
        for quacker in self.quackers:
            quacker.notify_observers()


class QuackCounter(Quackable):
    num_of_quacks = 0

    def __init__(self, duck):
        # Quackable.__init__(self)
        self.duck = duck

    def __str__(self):
        return self.duck.__str__()

    def quack(self):
        self.duck.quack()
        QuackCounter.num_of_quacks += 1

    def get_quacks(self):
        return QuackCounter.num_of_quacks

    def register_observer(self, observer):
        self.duck.register_observer(observer)

    def notify_observers(self):
        self.duck.notify_observers()


class MallardDuck(Quackable):

    def __init__(self):
        self.observable = Observabel(self)
        print('Mallard Duck 创建完成！')

    def __str__(self):
        return 'Mallard Duck'

    def quack(self):
        print('Quack!')
        self.notify_observers()

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()


class RedHeadDuck(Quackable):
    def __init__(self):
        self.observable = Observabel(self)
        print('Red Head Duck 创建完成！')

    def __str__(self):
        return 'Red Head Duck'

    def quack(self):
        print('Quack!')
        self.notify_observers()

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()


class DuckCall(Quackable):
    def __init__(self):
        self.observable = Observabel(self)
        print('Duck Call 创建完成！')

    def __str__(self):
        return 'Duck Call'

    def quack(self):
        print('Kwak!')
        self.notify_observers()

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()


class RubberDuck(Quackable):
    def __init__(self):
        self.observable = Observabel(self)
        print('Rubber Duck 创建完成！')

    def __str__(self):
        return 'Rubber Duck'

    def quack(self):
        print('Squeak!')
        self.notify_observers()

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

class Goose():
    def honk(self):
        print('Honk!')


class GooseAdapter(Quackable):
    def __init__(self, goose):
        self.observable = Observabel(self)
        self.goose = goose
        print('Goose 创建完成！')

    def __str__(self):
        return 'Goose'

    def quack(self):
        self.goose.honk()
        self.notify_observers()

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()
    


class AbstractDuckFactory():
    def create_mallard_duck(self):
        return Quackable()

    def create_red_head_duck(self):
        return Quackable()

    def create_duck_call(self):
        return Quackable()

    def create_rubber_duck(self):
        return Quackable()

    def create_goose(self):
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

    def create_goose(self):
        return GooseAdapter(Goose())


class CountingDuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return QuackCounter(MallardDuck())

    def create_red_head_duck(self):
        return QuackCounter(RedHeadDuck())

    def create_duck_call(self):
        return QuackCounter(DuckCall())

    def create_rubber_duck(self):
        return QuackCounter(RubberDuck())

    def create_goose(self):
        return QuackCounter(GooseAdapter(Goose()))


class Observer():
    def update(self):
        pass

class Quackologist(Observer):
    def update(self, duck):
        print('Quackologist: {} just quack.'.format(duck.__str__()))


class DuckSimulator():
    def __init__(self, duck_factory):

        print('创建一群其他鸭子: ')
        self.red_head_duck = duck_factory.create_red_head_duck()
        self.duck_call = duck_factory.create_duck_call()
        self.rubber_duck = duck_factory.create_rubber_duck()
        self.goose = duck_factory.create_goose()
        self.flock_of_ducks = Flock()
        self.flock_of_ducks.add(self.red_head_duck)
        self.flock_of_ducks.add(self.duck_call)
        self.flock_of_ducks.add(self.rubber_duck)
        self.flock_of_ducks.add(self.goose)

        # 创建一个呱呱叫学家
        self.quackologist = Quackologist()
        self.flock_of_ducks.register_observer(self.quackologist)

        self.simulate(self.flock_of_ducks)
        print('The ducks quacked {} times.'.format(QuackCounter.get_quacks(QuackCounter)))

    def simulate(self, duck):
        duck.quack()

duck_facoty = CountingDuckFactory()
duck_simulator = DuckSimulator(duck_facoty)
# print('The ducks quacked {} times.'.format(QuackCounter.get_quacks(QuackCounter)))