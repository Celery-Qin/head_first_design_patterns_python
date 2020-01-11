class Iterator():
    def __init__(self):
        self.items = list()
        self.position = 0
        
    def next(self):
        pass
        
    def has_next(self):
        pass

class DinnerMenuIterator(Iterator):
    def __init__(self, iterator):
        Iterator.__init__(self)
        self.items = iterator   # set
        self.temp_set = set()

    def next(self):
        menu_item = self.items.pop()
        self.temp_set.add(menu_item)
        return menu_item
        
    def has_next(self):
        if len(self.items) == 0:
            self.items.update(self.temp_set)
            self.temp_set.clear()
            return False
        else:
            return True


class PancakeHouseMenuIterator(Iterator):
    def __init__(self, iterator):
        Iterator.__init__(self)
        self.items = iterator

    def next(self):
        menu_item = self.items[self.position]
        self.position += 1
        return menu_item
        
    def has_next(self):
        if (self.position >= len(self.items)) or (self.items[self.position] == None):
            return False
        else:
            return True


class CafeMenuIterator(Iterator):
    def __init__(self, iterator):
        Iterator.__init__(self)
        # dict_values = iterator.values()
        self.items = list(iterator.values())

    def next(self):
        menu_item = self.items[self.position]
        self.position += 1
        return menu_item
        
    def has_next(self):
        if (self.position >= len(self.items)) or (self.items[self.position] == None):
            return False
        else:
            return True
