import random

# create list to sort
sort_me = random.sample(range(0,10), 10)
print('befor the sort', sort_me)

def quick_sort(sort_me):
    # pass in the list, low idx, and high idx
    ans = quick_sort2(sort_me, 0, len(sort_me) - 1)
    print(ans)

def quick_sort2(sort_me, low_idx, hi_idx):
    # if more than one item to be sorted
    if low_idx < hi_idx:
        # returns new pivot
        p = partition(sort_me, low_idx, hi_idx)
        # perform on left
        quick_sort2(sort_me, low_idx, p-1)
        # perform on right
        quick_sort2(sort_me, p+1, hi_idx)
    return sort_me
def partition(sort_me, low_idx, hi_idx):
    # get that pivot, which returns index value
    pivot_idx = get_pivot(sort_me, low_idx, hi_idx)
    pivot_value = sort_me[pivot_idx]
    # swap pivot value into left most part of list
    sort_me[pivot_idx], sort_me[low_idx] = sort_me[low_idx], sort_me[pivot_idx]
    border = low_idx

    for i in range(low_idx, hi_idx + 1):
        if sort_me[i] < pivot_value:
            # each time we swap pivot to left, we move the border to the right
            border += 1
            # swap to left side of list
            sort_me[i], sort_me[border] = sort_me[border], sort_me[i]
    # low value swaps with border
    sort_me[low_idx], sort_me[border] = sort_me[border], sort_me[low_idx]

    # return this index for pivot
    return border


def get_pivot(sort_me, low_idx, hi_idx):
    mid = (hi_idx + low_idx) // 2
    pivot = hi_idx
    # get the middle of the three index
    if sort_me[low_idx] < sort_me[mid]:
        if sort_me[mid] < sort_me[hi_idx]:
            pivot = mid
    elif sort_me[low_idx] < sort_me[hi_idx]:
        pivot = low_idx
    return pivot

quick_sort(sort_me)
