import menu

class Iterator():
    def __init__(self, items):
        self.items = items
        self.position = 0
        
    def next(self):
        menu_item = self.items[self.position]
        self.position += 1
        return menu_item
        
    def has_next(self):
        if (self.position >= len(self.items)) or (self.items[self.position] == None):
            return False
        else:
            return True

class CompositeIterator(Iterator):
    def __init__(self, component):
        self.component = component
        self.stack = list()
        self.position = 0
        self.iterator = Iterator(component.get_children())
        while self.iterator.has_next():
            next_item = self.iterator.next()
            if isinstance(next_item, menu.MenuItem):
                self.stack.append(next_item)
            else:  #  if isinstance(next_item, menu.MenuComponent):
                next_iterator = next_item.create_component_iterator()
                self.stack.extend(next_iterator.get_stack())
            

    def get_stack(self):
        return self.stack

    def next(self):
        menu_item = self.stack[self.position]
        self.position += 1
        return menu_item

    def has_next(self):
        if self.position >= len(self.stack) or self.stack[self.position] == None:
            return False
        else:
            return True


class NullIterator(Iterator):
    def next(self):
        return None

    def has_next(self):
        return False