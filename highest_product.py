from itertools import islice

def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise Exception('Less than 3 items!')
    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # we could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest =  min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2  = list_of_ints[0] * list_of_ints[1]
    # except this one--we pre-populate it for the first *3* items.
    # this means in our first pass it'll check against itself, which is fine.
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    # walk through items, starting at index 2
    for i in range(2,len(list_of_ints)):
        # do we have a new highest product of 3?
        # it's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_3 = max(
            highest_product_of_3,
            list_of_ints[i] * highest_product_of_2,
            list_of_ints[i] * lowest_product_of_2)
        # do we have a new highest product of two?
        highest_product_of_2 = max(
            highest_product_of_2,
            list_of_ints[i] * highest,
            list_of_ints[i] * lowest)
        # do we have a new lowest product of two?
        lowest_product_of_2 = min(
            lowest_product_of_2,
            list_of_ints[i] * highest,
            list_of_ints[i] * lowest)   
        # do we have a new highest?
        highest = max(highest, list_of_ints[i])
        # do we have a new lowest?
        lowest = min(lowest, list_of_ints[i])
    return highest_product_of_3




print highest_product_of_3([1, 10, -5, 1, -100])
print '\n ' * 2
print highest_product_of_3([2,3,4,8,8,9])







