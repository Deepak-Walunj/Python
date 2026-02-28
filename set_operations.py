# set={1,2,"I3"}
# print(set)
# set.add(4.4)
# print(set)
# set.remove(1)
# print(set)

s1={1,2,4,5}
s2={1,2,3,4,6}
# print(s1.union(s2))
# print(s1,s2)
# print(s1.intersection(s2))
# print(s1,s2)
# s1.update(s2)
# print(s1,s2)
# # s1.intersection_update(s2)
# # print(s1,s2)
# print(s1.symmetric_difference(s2))
# print(s1,s2)
# print(s1.difference(s2))
# print(s1.difference_update(s2))
# print(s1,s2)

print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s2.issuperset(s1))
print(s1.issubset(s2))
