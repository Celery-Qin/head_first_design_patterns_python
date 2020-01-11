class CaffeineBevarage():
    def prepare_recipe(self):
        print('\n---- Start to prepare ----')
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if(self.customer_wants_condiments()):
            self.add_condiments()
        print('---- Please enjoy! ----\n')


    def boil_water(self):
        print('Boil water...')

    def brew(self):
        pass

    def pour_in_cup(self):
        print('Pour hot water into the cup...')

    def add_condiments(self):
        pass

    def customer_wants_condiments(self):
        while True:
            answer = input('Would you like some condiments?(y/n)').lower()
            if answer.startswith('y'):
                return True
            elif answer.startswith('n'):
                return False
            else:
                print('Please enter y / n, enter again:')



class Coffee(CaffeineBevarage):
    def brew(self):
        print('Brew coffee grinds...')

    def add_condiments(self):
        print('Add milk & sugar...')

class Tea(CaffeineBevarage):
    def brew(self):
        print('Steep tea bag...')

    def add_condiments(self):
        print('Add lemon...')


if __name__ == '__main__':
    coffee = Coffee()
    tea = Tea()

    coffee.prepare_recipe()
    tea.prepare_recipe()

