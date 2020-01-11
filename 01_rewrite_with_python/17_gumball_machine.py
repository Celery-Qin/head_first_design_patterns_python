class GumballMachine():
    SOLD_OUT = 0   # include NO_QUARTER
    NO_QUARTER = 1
    HAS_QUARTER = 2
    SOLD = 3

    def __init__(self, count):
        self.count = count
        if self.count > 0 :
            self.state = self.NO_QUARTER
        else:
            self.state = self.SOLD_OUT

    def __str__(self):
        if self.state == 0:
            result = '【state】 SOLD OUT'
        elif self.state == 1:
            result = '【state】 NO QUARTER'
        elif self.state == 2:
            result = '【state】 HAS QUARTER'
        elif self.state == 3:
            result = '【state】 SOLD'
        result += '\n【count】 '+ str(self.count)
        return result

    def user_insert_quarter(self):
        if self.state == self.HAS_QUARTER:
            print('You can not insert another quarter!')
        elif self.state == self.SOLD_OUT:
            print('You can not insert a quarter, the machine is sold out.')
        elif self.state == self.SOLD:
            print('Please wait, we are already giving you a gumball!!!')
        elif self.state == self.NO_QUARTER:
            self.state = self.HAS_QUARTER
            print('You inserted a quarter!')

    def user_eject_quarter(self):
        if self.state == self.HAS_QUARTER:
            self.state = self.NO_QUARTER
            print('Quarter returned.')
        elif self.state == self.NO_QUARTER:
            print('You haven\'t inserted a quarter!')
        elif self.state == self.SOLD:
            print('Sorry, you already turn the crank.')
        elif self.state == self.SOLD_OUT:
            print('You haven\'t inserted a quarter!')

    def user_turn_crank(self):
        if self.state == self.SOLD:
            print('Turning more doesn\'t give you more gumballs!')
        elif self.state == self.NO_QUARTER:
            print('Please inserted a quarter!')
        elif self.state == self.SOLD_OUT:
            print('You haven\'t inserted a quarter!')
        if self.state == self.HAS_QUARTER:
            self.state = self.SOLD
            print('You turned...')
            self.dispense()

    def dispense(self):
        if self.state == self.SOLD:
            print('A gumball comes rolling out the slot !')
            self.count -= 1
            if self.count == 0:
                print('Oops, out of gumballs!')
                self.state = self.SOLD_OUT
            else:
                self.state = self.NO_QUARTER
        elif self.state == self.NO_QUARTER:
            print('Please inserted a quarter!')
        elif self.state == self.SOLD_OUT:
            print('No gumball dispensed.')
        elif self.state == self.HAS_QUARTER:
            print('No gumball dispensed.')


if __name__ == '__main__':
    print('\n------ Initialize a gumball machine ------')
    gumball_machine = GumballMachine(5)
    print(gumball_machine)

    print('\n------ Insert a quarter, turn the crank ------')
    gumball_machine.user_insert_quarter()
    gumball_machine.user_turn_crank()
    print(gumball_machine)

    print('\n------ Insert, eject, turn ------')
    gumball_machine.user_insert_quarter()
    gumball_machine.user_eject_quarter()
    gumball_machine.user_turn_crank()
    print(gumball_machine)

    print('\n------ Insert, turn, insert, turn, eject ------')
    gumball_machine.user_insert_quarter()
    gumball_machine.user_turn_crank()
    gumball_machine.user_insert_quarter()
    gumball_machine.user_turn_crank()
    gumball_machine.user_eject_quarter()
    print(gumball_machine)

    print('\n------ Insert, insert, turn, insert, turn, insert, turn ------')
    gumball_machine.user_insert_quarter()
    gumball_machine.user_insert_quarter()
    gumball_machine.user_turn_crank()
    gumball_machine.user_insert_quarter()
    gumball_machine.user_turn_crank()
    gumball_machine.user_insert_quarter()
    gumball_machine.user_turn_crank()
    print(gumball_machine)