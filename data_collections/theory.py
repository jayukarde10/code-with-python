# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

#list
list=[10,20,30,40,50,20]
#modify list
list[0]=100 #change 1st item
list[2:3]=[300,"jay"]
#bracket is imp

#Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
list.insert(4,"jay")
print("List:",list)

#append item
list.append("hello")
print("After Append:",list)
#only one element at a time get appended
#extend list
list.extend(["apple","banana"])#extend list by adding elements of another list
print("After Extend:",list)
#or
thislist=[1,2,3]
anotherlist=[4,5,6]
thislist.extend(anotherlist)
print("Extended List:",thislist)

#property of extend
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



