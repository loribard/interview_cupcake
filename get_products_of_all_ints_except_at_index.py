
def get_products_of_all_ints_except_at_index(list_of_ints):
    product_list = []
    if len(list_of_ints) < 2:
        return 'Getting the product of numbers at other indices\nrequires at least two numbers. You input %s .' % str(list_of_ints)
    list_lower = 1
    for i in range(len(list_of_ints)):
        if i >= 1:
            list_lower *= list_of_ints[i-1]
        list_upper = list_of_ints[i+1:]
        first = list_lower
        second = product(list_upper)
        product_list.append(first*second)
    return product_list


def product(lista):
    if len(lista) < 1:
        return 1
    product = 1
    for item in lista:
        product *= item
    return product

lista = [1, 7, 3, 4]
listb = [1]
listc = [1, 3]
listd = [2, 6, 8, 0]

print get_products_of_all_ints_except_at_index(lista)
print get_products_of_all_ints_except_at_index(listb)
print get_products_of_all_ints_except_at_index(listc)
print get_products_of_all_ints_except_at_index(listd)










