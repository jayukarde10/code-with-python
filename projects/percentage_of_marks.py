n=int(input("enter no of subjects"))
list=[]
for i in range(0,n):
    a=int(input("enter marks of subject"))
    list.append(a)

percentage=(sum(list)/(n*100))*100 #property of list sum()
print("percentage is :",percentage)