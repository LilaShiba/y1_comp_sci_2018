#https://www.codewars.com/kata/permutations/train/python
def permute(list, s):
    if list == 1:
        return s
    else:
        meow = [ x + y
                 for y in permute(1, s)
                 for x in permute(list - 1, s)
                 ]

    #    for x in meow:
    #        if x[0] == x[1]:
    #            meow.remove(x)

    #    for x in meow:
    #        for y in meow:
    #            if y[::-1] == x:
    #                meow.remove(y)
    print(meow)
    return meow


print(permute(1, ["a","b","c"]))
print(permute(2, ["a","b","c"]))
