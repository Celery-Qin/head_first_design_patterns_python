import waitress, menu

if __name__ == '__main__':
    all_menus = menu.MenuComponent('All Menus', 'This is the total menus component.')

    pancake_house_menu = menu.MenuComponent('Pancake House Menu', 'Offer Breakfast')
    dinner_menu = menu.MenuComponent('Dinner Menu', 'Offer Lunch')
    cafe_menu = menu.MenuComponent('Cafe Menu', 'Offer Evening Cafe')

    dessert_menu = menu.MenuComponent('Dessert Menu','Offer Dessert of Dinner')
    
    pancake = menu.MenuItem('Pancake','Pancake with cream and honey', False, '$6.18')
    milk = menu.MenuItem('Milk','Hot Milk with sugar', False, '$2.18')
    steak = menu.MenuItem('Steak','Fresh Steak Medium done', False, '$18.99')
    wine = menu.MenuItem('Wine','White Wine in 1920', True, '$3.18')
    coffee = menu.MenuItem('Coffee','House blend coffee', False, '$4.99')
    pudding = menu.MenuItem('Pudding','Fruit Pudding with Sugar', True, '$5.08')

    all_menus.add(pancake_house_menu)
    all_menus.add(dinner_menu)
    all_menus.add(cafe_menu)
    dinner_menu.add(dessert_menu)

    pancake_house_menu.add(pancake)
    pancake_house_menu.add(milk)
    dinner_menu.add(steak)
    dinner_menu.add(wine)
    cafe_menu.add(coffee)
    dessert_menu.add(pudding)

    new_waitress = waitress.Waitress(all_menus)
    new_waitress.print_menu()
    new_waitress.print_vegetarian_menu()