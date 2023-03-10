from pprint import pprint


def dict_collector(file_recipes):
    with open(file_recipes, 'rt', encoding='utf 8') as file:
        cook_book = {}
        for line in file:
            cook_book_name = line.strip()
            emp_count = int(file.readline())
            employees = []
            for i in range(emp_count):
                structure = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                ingridient = file.readline().strip().split(' | ')
                for _ in ingridient:
                    structure['ingredient_name'] = ingridient[0]
                    structure['quantity'] = ingridient[1]
                    structure['measure'] = ingridient[2]
                employees.append(structure)
                menu = {cook_book_name: employees}
                cook_book.update(menu)
            file.readline()

    return cook_book


dict_collector('recipes.txt')


def get_shop_list_by_dishes(dishes, person_count):
    menu_cook_book = dict_collector('recipes.txt')
    print('Меню :')
    pprint(menu_cook_book)
    print()
    shopping_list = {}

    try:
        for dish in dishes:
            for item in (menu_cook_book[dish]):
                items_list = dict([(item['ingredient_name'],
                                    {'measure': item['measure'],
                                     'quantity': int(item['quantity']) * person_count
                                     })])
                if shopping_list.get(item['ingredient_name']):
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item

                else:
                    shopping_list.update(items_list)

        print(f"Для выбранных блюд на {person_count} персоны необходимы ингредиенты:")
        pprint(shopping_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# visitor_1 = input("Введите блюдо 1: ")
# visitor_2 = input("Введите блюдо 2: ")
# # Омлет, Утка по-пекински, Запеченный картофель, Фахитос

# get_shop_list_by_dishes([visitor_1, visitor_2], 2)
