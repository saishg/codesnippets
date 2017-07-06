class Item:
    def __init__(self, value, weight):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return "(W:{},V:{})".format(self.weight, self.value)


#ITEMS = [Item(60, 10), Item(100, 20), Item(120, 30)]
#MAX_WEIGHT = 50

ITEMS = [Item(1, 1), Item(4, 3), Item(5, 4), Item(7, 5)]
MAX_WEIGHT = 7

CACHE = {}

def dynamic(item_number=len(ITEMS) - 1, remaining_weight=MAX_WEIGHT):
    key = (item_number, remaining_weight)
    if key not in CACHE:
        item = ITEMS[item_number]

        if item_number == 0:
            if item.weight > remaining_weight:
                CACHE[key] = 0
                return 0
            else:
                CACHE[key] = item.value
                return item.value

        if item.weight > remaining_weight:
            max_value = dynamic(item_number - 1, remaining_weight)
        else:
            max_value = max(dynamic(item_number - 1, remaining_weight),
                           item.value + dynamic(item_number - 1, remaining_weight - item.weight))

        CACHE[key] = max_value
    return CACHE[key]

CACHE2 = {}

def dynamic2(selected_items=(), remaining_weight=MAX_WEIGHT, value=0):
    max_value = value
    for item in ITEMS:
        if item not in selected_items:
            if item.weight <= remaining_weight:
                new_value = dynamic2(selected_items + (item,), remaining_weight - item.weight, value + item.value)
                max_value = max(new_value, max_value)
    return max_value


def recurse2(item_number=0, weight=0, value=0):
    if item_number >= len(ITEMS):
        return value

    item_weight = ITEMS[item_number].weight
    item_value = ITEMS[item_number].value

    if weight + item_weight > MAX_WEIGHT:
        return recurse2(item_number + 1, weight, value)
    else:
        return max(recurse2(item_number + 1, weight, value),
                   recurse2(item_number + 1, weight + item_weight, value + item_value))
        
def recurse(selected_items=(), remaining_weight=MAX_WEIGHT, value=0):
    max_value = value
    for item in ITEMS:
        if item not in selected_items:
            if item.weight <= remaining_weight:
                new_value = recurse(selected_items + (item,), remaining_weight - item.weight, value + item.value)
                max_value = max(max_value, new_value)
    return max_value


if __name__ == '__main__':
    print dynamic()
    print dynamic2()
    print recurse()
    print recurse2()
