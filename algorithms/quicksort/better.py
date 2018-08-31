import random

meow = random.sample(range(0,100), 10)
print('not sorted',meow)

def quick(list_to_sort):
    ans = quick_sort(list_to_sort, 0, len(list_to_sort)-1)
    print('sorted', ans)

def quick_sort(list_to_sort, low, hi):
    if ((hi - low) > 0):
        p = partition(list_to_sort, low, hi)
        quick_sort(list_to_sort, low, p - 1)
        quick_sort(list_to_sort, p + 1, hi)
    return list_to_sort


def partition(list_to_sort, low, hi):
    divider = low
    pivot = hi

    for i in range(low, hi):
        if (list_to_sort[i] < list_to_sort[pivot]):
            list_to_sort[i], list_to_sort[divider] = list_to_sort[divider], list_to_sort[i]
            divider +=1

    list_to_sort[pivot], list_to_sort[divider] = list_to_sort[divider], list_to_sort[pivot]

    return divider

quick(meow)
