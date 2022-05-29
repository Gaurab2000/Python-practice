l=[1,2,3,4]
l=set(l)
print(l)
l.add(5)
print(l)
l.add(5)
print(l)
s=l.union({6,7,8})
print(s)
print(l,s)
#similar for intersection
#try different functions