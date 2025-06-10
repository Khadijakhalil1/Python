from functools import reduce
l =[555,23,88,2,7,44,88]

def greater(a,b):
    if (a>b):
        return a
    return b

print(reduce(greater,l))  