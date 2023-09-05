# def format_ingredients(items):
#     list = items[::-1]
#     end = list[0:2]
#     end = ' и '.join(end)
#     list = list[2:]
#     list.reverse()
#     list.append(end)
#     print(items)
#     print(list)
#     print(end) 
#     return list

# format_ingredients(['яйца 2шт', 'сахар 1 л.', 'соль 1 чл.', 'уксус'])


def format_ingredients(items):
    list = items.copy()
    end = list[-2:]
    end = ' и '.join(end)
    list = list[:-2]
    list.append(end)
    print(items)
    print(list)
    print(end)
    list = ', '.join(list)
    return list

format_ingredients(['яйца 2шт', 'сахар 1 л.', 'соль 1 чл.', 'уксус'])
