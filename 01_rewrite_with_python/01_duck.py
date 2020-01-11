# ---------------- FlyBehavior ---------------- #
class FlyBehavior():
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
	# 实现鸭子的各种飞行动作
    def fly(self):
        print('I\'m flying!')

class FlyNoway(FlyBehavior):
	# 啥也不做，不会飞
    def fly(self):
        print('I can\'t fly!')

class FlyRocketPowered(FlyBehavior):
	# 带着火箭飞
    def fly(self):
        print('I\'m flying with a rocket！')

# ---------------- QuackBehavior ---------------- #
class QuackBehavior():
    def quack(self):
        pass

class Quack(QuackBehavior):
	# 嘎嘎叫
    def quack(self):
        print('Quack')

class Squeak(QuackBehavior):
	# 吱吱叫
    def quack(self):
        print('Squeak')

class MuteQuack(QuackBehavior):
	# 不会叫
    def quack(self):
        print('<< Silence >>')

# ---------------- Duck ---------------- #
class Duck():
    def swim(self):
        print('All Ducks float, even decoys!')

    def display(self):
        pass

    flyBehavior = FlyBehavior()
    quackBehavior = QuackBehavior()

    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
	    self.quackBehavior.quack()

    def setFlyBehavior(self,fly_pattern):
        # 用于动态地改变飞行模式
        self.flyBehavior = fly_pattern()

    def setQuackBehavior(self,quack_pattern):
        # 用于动态地改变叫声模式
        self.quackBehavior = quack_pattern()

# ---------------- 利用MallardDuck测试不同的鸭子有不同的飞行模式和叫声模式 ---------------- #
# class MallardDuck(Duck):
#     def display(self):
#         print('I\'m a real Mallard Duck.')

#     flyBehavior = FlyWithWings()
#     quackBehavior = Quack()
# 实例化测试
# mini_duck_simulator = MallardDuck()
# mini_duck_simulator.swim()
# mini_duck_simulator.display()
# mini_duck_simulator.performFly()
# mini_duck_simulator.performQuack()

# ---------------- 利用ModelDuck测试运行过程中改变鸭子的飞行模式和叫声模式 ---------------- #
class ModelDuck(Duck):
    def display(self):
        print('I\'m a Model Duck.')

    flyBehavior = FlyNoway() # 一开始不会飞
    quackBehavior = Quack()


# 实例化测试
print('现实原来最初的modelDuck')
model = ModelDuck()
model.swim()
model.display()
model.performFly()
model.performQuack()

print('改变飞行模式和叫声模式')
model.setFlyBehavior(FlyRocketPowered)
model.setQuackBehavior(Squeak)
model.performFly()
model.performQuack()

