import random

def sort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        rand = random.randint(0, len(array) - 1)
        pivot = array[rand]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)   #Złączanie list
    else:
        return array


alist = [54, 26, 93, 1, 17, 77, 31, 44, 55, 20]
print(sort(alist))

