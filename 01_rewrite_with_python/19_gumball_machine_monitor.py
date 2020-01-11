import random

class State():
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def __str__(self):
        return 'default state'

    def insert_quarter(self):
        pass 

    def eject_quarter(self):
        pass 

    def turn_crank(self):
        pass 

    def dispense(self):
        pass

class SoldState(State):
    def __str__(self):
        return 'Sold State'

    def insert_quarter(self):
        print('Please wait, we are already giving you a gumball!!!')

    def eject_quarter(self):
       print('Sorry, you already turn the crank.')

    def turn_crank(self):
        print('Turning more doesn\'t give you more gumballs!')

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() == 0:
            print('Oops, out of gumballs!')
            self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())
        else:
            self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())

class SoldOutState(State):
    def __str__(self):
        return 'Sold Out State'

    def insert_quarter(self):
        print('You can not insert a quarter, the machine is sold out.')

    def eject_quarter(self):
        print('You haven\'t inserted a quarter!')

    def turn_crank(self):
        print('You haven\'t inserted a quarter!')

    def dispense(self):
        print('No gumball dispensed.')

class NoQuarterState(State):
    def __str__(self):
        return 'No Quarter State'

    def insert_quarter(self):
        self.gumball_machine.set_state(self.gumball_machine.get_has_quarter_state())
        print('You inserted a quarter!')

    def eject_quarter(self):
        print('You haven\'t inserted a quarter!')

    def turn_crank(self):
        print('Please inserted a quarter!')

    def dispense(self):
        print('Please inserted a quarter!')

class HasQuarterState(State):
    def __str__(self):
        return 'Has Quarter State'

    def insert_quarter(self):
        print('You can not insert another quarter!')

    def eject_quarter(self):
        self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
        print('Quarter returned.')

    def turn_crank(self):
        print('You turned...')
        winner_num = random.randint(0, 9)
        if winner_num == 0 and self.gumball_machine.get_count() > 1:
            self.gumball_machine.set_state(self.gumball_machine.get_winner_state())
        else:
            self.gumball_machine.set_state(self.gumball_machine.get_sold_state())
        
    def dispense(self):
        print('No gumball dispensed.')

class WinnerState(State): # 类似于Sold State
    def __str__(self):
        return 'Winner State'

    def insert_quarter(self):
        print('Please wait, we are already giving you TWO gumballs !!!')

    def eject_quarter(self):
        print('Sorry, you already turn the crank.')

    def turn_crank(self):
        print('Turning more doesn\'t give you more gumballs!')

    def dispense(self):
        print('YOU ARE A WINNER! You get two gumballs for your quarter. ')
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() == 0:
            print('Oops, out of gumballs!')
            self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())
        else:
            self.gumball_machine.release_ball()
            if self.gumball_machine.get_count() == 0:
                print('Oops, out of gumballs!')
                self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())
            else:
                self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())


class GumballMachine():
    def __init__(self, location='', count=0):
        self.sold_out_state = SoldOutState(self)
        self.sold_state = SoldState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.winner_state = WinnerState(self)
        self.location = location
        self.count = count
        if count > 0 :
            self.state = self.no_quarter_state
        else:
            self.state = self.sold_out_state

    # def __str__(self):
    #     return '【state】' + self.state.__str__() + '\n【count】' + str(self.count)

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def set_state(self, state):
        self.state = state

    def release_ball(self):
        print('A gumball comes rolling out the slot !')
        if self.count > 0:
            self.count -= 1

    def get_sold_out_state(self):
        return self.sold_out_state

    def get_sold_state(self):
        return self.sold_state

    def get_no_quarter_state(self):
        return self.no_quarter_state

    def get_has_quarter_state(self):
        return self.has_quarter_state

    def get_winner_state(self):
        return self.winner_state

    def get_count(self):
        return self.count

    def get_state(self):
        return self.state

    def get_location(self):
        return self.location


class GumballMonitor():
    def __init__(self, machine):
        self.machine = machine

    def report(self):
        print('\n------ Gumball Machine Report ------')
        print('Location: {}'.format(self.machine.get_location()))
        print('Current inventory: {}'.format(self.machine.get_count()))
        print('Current state: {}'.format(self.machine.get_state()))


if __name__ == '__main__':
    print('\n------ Initialize a gumball machine ------')
    gumball_machine = GumballMachine(5)
    # print(gumball_machine)
    gumball_monitor = GumballMonitor(gumball_machine)
    gumball_monitor.report()

    # print('\n------ Insert a quarter, turn the crank ------')
    # gumball_machine.insert_quarter()
    # gumball_machine.turn_crank()
    # print(gumball_machine)

    # print('\n------ Insert, eject, turn ------')
    # gumball_machine.insert_quarter()
    # gumball_machine.eject_quarter()
    # gumball_machine.turn_crank()
    # print(gumball_machine)

    print('\n------ Insert, turn, insert, turn, eject ------')
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.eject_quarter()
    # print(gumball_machine)
    gumball_monitor.report()

    # print('\n------ Insert, insert, turn, insert, turn, insert, turn ------')
    # gumball_machine.insert_quarter()
    # gumball_machine.insert_quarter()
    # gumball_machine.turn_crank()
    # gumball_machine.insert_quarter()
    # gumball_machine.turn_crank()
    # gumball_machine.insert_quarter()
    # gumball_machine.turn_crank()
    # print(gumball_machine)