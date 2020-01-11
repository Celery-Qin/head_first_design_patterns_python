'''
这里的是两家餐厅的原始设计，变更较小。
'''

import iterator

class MenuItem():
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def is_vegetarian(self):
        return self.vegetarian

    def get_price(self):
        return self.price

class PancakeHouseMenu():
    def __init__(self):
        self.menu_items = list()
        self.add_item('Dish name 1','Dish description...',True,'$ 12.88')
        self.add_item('Dish name 2','Dish description...',True,'$ 3.99')
        self.add_item('Dish name 3','Dish description...',False,'$ 6.28')
        self.add_item('Dish name 4','Dish description...',False,'$ 9.08')

    def __str__(self):
        return 'Pancake House Menu'

    def add_item(self, name,description,vegetarian,price):
        menu_item = MenuItem(name,description,vegetarian,price)
        self.menu_items.append(menu_item)

    def create_iterator(self):
        # 新增方法
        return iterator.PancakeHouseMenuIterator(self.menu_items)

class DinnerMenu():
    def __init__(self):
        self.max_len = 6
        self.num_of_items = 0
        self.menu_items = set()
        self.add_item('Dish name 1','Dish description...',True,'$ 12.88')
        self.add_item('Dish name 2','Dish description...',True,'$ 3.99')
        self.add_item('Dish name 3','Dish description...',False,'$ 6.28')
        self.add_item('Dish name 4','Dish description...',False,'$ 9.08')

    def __str__(self):
        return 'Dinner Menu'

    def add_item(self, name,description,vegetarian,price):
        if self.num_of_items >= self.max_len:
            print('Menu is full, can not add more dish!')
        else:
            menu_item = MenuItem(name,description,vegetarian,price)
            self.menu_items.add(menu_item)
            self.num_of_items += 1

    def create_iterator(self):
        # 新增方法
        return iterator.DinnerMenuIterator(self.menu_items)


class CafeMenu():
    def __init__(self):
        self.menu_items = dict()
        self.add_item('Cafe name 1','Dish description...',True,'$ 12.88')
        self.add_item('Cafe name 2','Dish description...',True,'$ 3.99')
        self.add_item('Cafe name 3','Dish description...',False,'$ 6.28')
        self.add_item('Cafe name 4','Dish description...',False,'$ 9.08')

    def __str__(self):
        return 'Cafe Menu'

    def add_item(self, name, description, vegetarian, price):
        menu_item = MenuItem(name,description,vegetarian,price)
        self.menu_items[name] = menu_item

    def create_iterator(self):
        # 新增方法
        return iterator.CafeMenuIterator(self.menu_items)