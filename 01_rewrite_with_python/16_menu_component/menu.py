import iterator

class MenuComponent():
    # 菜单组合
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.menu_items = list()

    def print(self):
        print('\n【'+self.get_name()+'】' + self.get_description())
        menu_iterator = iterator.Iterator(self.menu_items)
        while menu_iterator.has_next():
            menu_iterator.next().print()
        
    def get_name(self):
        return self.name
        
    def get_description(self):
        return self.description

    def add(self, component):
        self.menu_items.append(component) 

    def remove(self, component):
        self.menu_items.remove(component) 

    def get_children(self):
        return self.menu_items

    def create_component_iterator(self):
        return iterator.CompositeIterator(self)

class MenuItem(MenuComponent):
    # Leaf 菜单里的菜项
    def __init__(self,name,description,vegetarian,price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def print(self):
        print(self.get_name())
        print(self.get_description())
        print(self.get_price())
        print('-------------------')

    def is_vegetarian(self):
        return self.vegetarian

    def get_price(self):
        return self.price

    def create_component_iterator(self):
        return iterator.NullIterator(self)

