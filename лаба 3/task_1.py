def index_tovara(product_list, product_name):
    for index, product in enumerate(product_list): # index - индекс элемента списка, product - сам элемент и с помощью эньюмирэйт проходимся по всему списку
        if product == product_name: # если элемент совпадает с искомым, то возвращаем его индекс, иначе - пустое множество.
            return index
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index_tovara(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
