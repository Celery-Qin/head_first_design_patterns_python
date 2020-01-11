

class Waitress():
    def __init__(self, all_menus):
        self.all_menus = all_menus

    def print_menu(self):	
        self.all_menus.print()

    def print_vegetarian_menu(self):
        iterator = self.all_menus.create_component_iterator()
        print('\n ------ Vegetarian Menu ------ ')
        while iterator.has_next():
            item = iterator.next()
            if item.is_vegetarian():
                item.print()


    # print_breakfast_menu()
    # print_lunch_menu()
    # print_vegetarian_menu()
    # print_dessert_menu()
    # is_vegetarian()