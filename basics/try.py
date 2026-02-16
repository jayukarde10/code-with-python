list=[]
t=int(input("how many insertion"))
for i in range(0,t):
     l=input("insert in list ")
     list.append(l)
list.sort()
print(list)  
list.sort(reverse=True)
print(list)
list.clear()
print(list)
