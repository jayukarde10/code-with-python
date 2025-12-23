list=["apple",1,3.14,True,"banana",1]
print(type(list)) #data type is list
print("List:",list) #print entire list

#List items are ordered, changeable, and allow duplicate values.
#Allow Duplicates


print(len(list)) #length of list

# this_list = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(this_list)

#Access Items
print(list[0]) #first item
print(list[-1]) #last item
print(list[1:3]) #items from index 1 to 2
print(list[2:5])
#The search will start at index 2 (included) and end at index 5 (not included).
print(list[:5])#items from beginning to index 4
