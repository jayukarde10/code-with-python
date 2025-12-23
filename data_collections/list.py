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

print(list[-4:-2]) #items from index -4 to -3
#The search will start at index -4 (included) and end at index -2 (not included).

if "apple" in list:
    print(f"yess it present in position {list.index("apple")}") #check if item present in list

for index, value in enumerate(list):
    print(index, value)

list[1]="banana" #change 2nd item
print("Updated List:",list)

list[2:4]=["apple","banana"] #change 3rd and 4th item
list[5:3]=["Jay"] #insert item at index 5
print("Modified List:",list)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

list.insert(5,"jay") #insert item at index 5
print("After Insertion:",list)

list.append("hello") #append item at end cant specify index
print("After Append:",list)

list.extend(["welcome",123]) #add multiple items at end
print("After Extend:",list)



