inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def stuff(game_inventory):
    print("Inventory".upper())
    sum_of_items = 0
    for i, v in game_inventory.items():
        each_item = f"{v} {i}"
        sum_of_items += v
        print(each_item)
    print(f'Total number of items:{sum_of_items}')


stuff(inventory)
