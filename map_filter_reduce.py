l=[1,2,3,4,5,6,7,8,7,6,5,4,3,2,1]
def map_test(a,b):
    return a+b
l2=[1,2,3,4,5,1,2]
print(list(map(map_test,l,l2)))


def filter_test(a):
    return a%2==0

print(list(filter(filter_test,l)))

from functools import reduce
def sum(a,b):
    return a+b
print(reduce(sum,l))