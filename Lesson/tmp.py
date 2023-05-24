#def all(iterable):
#   for element in iterable:
#       if not element:
#           return False
#   return True
lst=[1,2,3,4,5,11]
lst2=[-1,-2,-3,-4,-5,11]
print(all( e > 0 for e in lst))
print(all( e > 0 for e in lst2))