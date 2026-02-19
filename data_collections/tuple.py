# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#unchangeble(immutable)

tup =("this","is",1,"tup")
tup1 = 1,5,6
print(type(tup1))
print(tup)
print(tup[0])

#to create a single value tuple always use ,
singleTup=(1,) #not like (1)

#slicing
print(tup[1:3])

#methods
tup=(0,1,2,3,4,1)
print(tup.index(1)) #return index of first occurrenc
print(tup.count(1)) #count total occurance 



