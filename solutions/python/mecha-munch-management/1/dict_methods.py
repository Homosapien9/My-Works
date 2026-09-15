"""
Mecha Munch(TM) shopping cart MVP functions.
"""


def add_item(current_cart, items_to_add):
    """Add items to a shopping cart.

    current_cart: dict of {item_name: quantity}
    items_to_add: any list-like iterable of item names (repeats = quantity)

    Returns a new/updated shopping cart dictionary.
    """
    new_cart = dict(current_cart)
    for item in items_to_add:
        new_cart[item] = new_cart.get(item, 0) + 1
    return new_cart


def read_notes(notes):
    """Create a shopping cart from a notes app list of items.

    notes: any list-like iterable of item names.

    Returns a new shopping cart dictionary, each item at quantity 1.
    """
    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the "ideas" recipes dictionary.

    ideas: dict of {recipe_name: {ingredient: quantity, ...}}
    recipe_updates: iterable of (recipe_name, updated_ingredients_dict) pairs.

    Returns the new/updated ideas dictionary.
    """
    new_ideas = dict(ideas)
    for recipe_name, updated_ingredients in recipe_updates:
        new_ideas[recipe_name] = updated_ingredients
    return new_ideas


def sort_entries(cart):
    """Return a new shopping cart, sorted alphabetically by item name."""
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Build a fulfillment cart combining quantity, aisle, and refrigeration info.

    cart: dict of {item_name: quantity}
    aisle_mapping: dict of {item_name: [aisle, needs_refrigeration]}

    Returns a fulfillment cart dict of {item_name: [quantity, aisle, needs_refrigeration]}
    sorted in reverse alphabetical order by item name.
    """
    fulfillment_cart = {
        item: [quantity] + aisle_mapping[item]
        for item, quantity in cart.items()
    }
    return dict(sorted(fulfillment_cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Reduce store inventory counts by amounts ordered in the fulfillment cart.

    fulfillment_cart: dict of {item_name: [quantity, aisle, needs_refrigeration]}
    store_inventory: dict of {item_name: [count, aisle, needs_refrigeration]}

    Returns the updated store inventory, with counts that reach 0 replaced
    by the string 'Out of Stock'.
    """
    new_inventory = dict(store_inventory)
    for item, (ordered_qty, *_rest) in fulfillment_cart.items():
        count, aisle, refrigerated = new_inventory[item]
        new_count = count - ordered_qty
        new_inventory[item] = [
            new_count if new_count > 0 else 'Out of Stock',
            aisle,
            refrigerated,
        ]
    return new_inventory


if __name__ == "__main__":
    # --- add_item ---
    print(add_item({'Banana': 3, 'Apple': 2, 'Orange': 1},
                    ('Apple', 'Apple', 'Orange', 'Apple', 'Banana')))
    # {'Banana': 4, 'Apple': 5, 'Orange': 2}

    print(add_item({'Banana': 3, 'Apple': 2, 'Orange': 1},
                    ['Banana', 'Orange', 'Blueberries', 'Banana']))
    # {'Banana': 5, 'Apple': 2, 'Orange': 2, 'Blueberries': 1}

    # --- read_notes ---
    print(read_notes(('Banana', 'Apple', 'Orange')))
    # {'Banana': 1, 'Apple': 1, 'Orange': 1}

    print(read_notes(['Blueberries', 'Pear', 'Orange', 'Banana', 'Apple']))
    # {'Blueberries': 1, 'Pear': 1, 'Orange': 1, 'Banana': 1, 'Apple': 1}

    # --- update_recipes ---
    print(update_recipes(
        {'Banana Bread': {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
         'Raspberry Pie': {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
        (('Banana Bread', {'Banana': 4, 'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),)
    ))

    print(update_recipes(
        {'Banana Bread': {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
         'Raspberry Pie': {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1},
         'Pasta Primavera': {'Eggs': 1, 'Carrots': 1, 'Spinach': 2, 'Tomatoes': 3, 'Parmesan': 2, 'Milk': 1, 'Onion': 1}},
        [('Raspberry Pie', {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2}),
         ('Pasta Primavera', {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1}),
         ('Blueberry Crumble', {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3})]
    ))

    # --- sort_entries ---
    print(sort_entries({'Banana': 3, 'Apple': 2, 'Orange': 1}))
    # {'Apple': 2, 'Banana': 3, 'Orange': 1}

    # --- send_to_store ---
    print(send_to_store(
        {'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},
        {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False],
         'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}
    ))
    # {'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True],
    #  'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]}

    # --- update_store_inventory ---
    print(update_store_inventory(
        {'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True],
         'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},
        {'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False],
         'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]}
    ))
    # {'Banana': [12, 'Aisle 5', False], 'Apple': [10, 'Aisle 4', False],
    #  'Orange': ['Out of Stock', 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True]}