import menu

class Waitress():
    def __init__(self, *menus):
        # self.pancake_house_menu = menu.PancakeHouseMenu()
        # self.dinner_menu = menu.DinnerMenu()
        self.menus_tuple = menus

    def print_menu_frame(self):
        print(' ------ MENU ------ ')
        # print(' ------ BREAKFAST ------ ')
        # self.print_menu(self.pancake_iterator)
        # print(' ------ LUNCH ------ ')
        # self.print_menu(self.dinner_iterator)
        for menu in self.menus_tuple:
            print('\n------ ' + menu.__str__() + ' ------') 
            menu_iterator = menu.create_iterator()
            self.print_menu(menu_iterator)

    def print_menu(self, iterator):	
        while iterator.has_next():
            menu_item = iterator.next()
            print('Dish: ' + menu_item.get_name())
            print('Description: ' + menu_item.get_description())
            print('Price: ' + menu_item.get_price())


    # print_breakfast_menu()
    # print_lunch_menu()
    # print_vegetarian_menu()
    # print_dessert_menu()
    # is_vegetarian()