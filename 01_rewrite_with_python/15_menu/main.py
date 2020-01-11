import waitress, menu

if __name__ == '__main__':
    pancake_house_menu = menu.PancakeHouseMenu()
    dinner_menu = menu.DinnerMenu()
    cafe_menu = menu.CafeMenu()
    # print(cafe_menu.menu_items)
    # cafe_iterator = cafe_menu.create_iterator()
    # print(cafe_iterator.items)

    new_waitress = waitress.Waitress(pancake_house_menu, dinner_menu, cafe_menu)
    new_waitress.print_menu_frame()