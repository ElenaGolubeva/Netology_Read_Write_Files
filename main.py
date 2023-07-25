def get_shop_list_by_dishes(dishes, person_count):
    dishes_list = {}
    for i in dishes:
        for k in cook_book[i]:
            if k['ingredient_name'] in dishes_list:
                dishes_list[k['ingredient_name']]['quantity'] += int(k['quantity'])*person_count
            else:
                dishes_list[k['ingredient_name']] = {'measure': k['measure'], 'quantity': int(k['quantity'])*person_count}
    return dishes_list


with open ("recipes.txt", encoding='utf-8') as f:
    cook_book = {}
    h = f.readlines()
    count_ = h.count('\n')
    l = 0
    for i in range(count_ + 1):
        cook_book[h[l].strip()] = []
        for j in range(l, len(h)):
            if '|' in h[j]:
                x = h[j].split('|')
                cook_book[h[l].strip()].append({'ingredient_name': x[0], 'quantity': x[1], 'measure': x[2].strip()})
            if h[j] == '\n':
                l = j+1
                break

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

