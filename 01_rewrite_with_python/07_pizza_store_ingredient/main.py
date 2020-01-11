import ingredients_factory, pizza_store, pizza

if __name__ == '__main__':
    ny_pizza_store = pizza_store.NYPizzaStore()
    ny_ingredients_factory = ingredients_factory.NYIngredientfactory()
    ny_pizza_store.order_pizza(ny_ingredients_factory)

    chicago_pizza_store = pizza_store.ChicagoPizzaStore()
    chicago_ingredients_factory = ingredients_factory.ChicagoIngredientfactory()
    chicago_pizza_store.order_pizza(chicago_ingredients_factory)