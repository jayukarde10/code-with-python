# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

#LIST methods 
#change ex. list[index]=value
#append,extend,insert index  position.
#pop position of index ,remove clear,del
#comprehension ex. list=[x for x in list if "jay" in x]
#newlist = [expression for item in iterable if condition == True]


#sort() use only for alfhabetical or numerical order not both at one
#decending Ex. list.sort(reverse=True)
#thislist.sort(key = function name)   # customize your own function by using the keyword argument key = function.
#sort is case sensitive capital letters come before lower case letters
#list.sort(key=str.lower) #ignore case sensitivity
#list.reverse() #reverse the current order of the list

#mylist = thislist.copy() only for null list
#mylist = list(thislist)  differnt methode same result built in list
#mylist = thislist[:] #slicing to copy list same result

#list3 = list1 + list2 #join two list

#summary of list methods

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list




#list
list=[10,20,30,40,50,20]
#modify list
list[0]=100 #change 1st item
list[2:3]=[300,"jay"]
#bracket is imp


#change direct
list[1]="banana" #change 2nd item
list[2:4]=["apple","banana"] #change 3rd and 4th item



#Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
list.insert(4,"jay")
list.append("hello")#append item
list.extend(["apple","banana"])#only one element at a time get appended#extend list#extend list by adding elements of another list

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


#remove item
list.remove("banana")
list.pop(1) #remove item at index 1
del list[0] #delete item at index 0

#clear entire list
del list
#or
list.clear() #clear all items in list


#comprehension

nlist=[x for x in list if "jay" in x]