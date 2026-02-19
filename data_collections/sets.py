#set is mutable but it is unordered and unindexed. It does not allow duplicate members.
# Set → Unordered, Mutable, Unindexed, No Duplicates  

#set is changeble(mutable) but element in set are immutable

set0={1,3.14,"jay",True,False,tuple([1,2,3])} #no list no dictnory becuse it is mutable means changeble

print(set0)
set1={1,2,3,4,5}
print(set1)
set2={1,1,1,2,3}
print(set2) #duplicate value get ignor  not get displyed
null_set=set() #empty set not set1={} becuse it is dictonary
print(null_set)

#methods
set3={1,4,33,55,67}
set3.add(2)
print(set3 )
set3.remove(1)
print(set3)
set3.pop() #removed random value/element
#if want to know which value get pop then put it in print
print(set3.pop())
print(set3)
set3.clear()
print(set3)


#union intersection
set4={1,2,3,4,5,6}
set5={5,6,7,8,9,0}
 
print(set4.union(set5))
print(set4.intersection(set5))
