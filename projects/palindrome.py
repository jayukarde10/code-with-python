list=[]
t=int(input("how many insertion"))
for i in range(0,t):
     l=input("insert in list ")
     list.append(l)
palindrome=list.copy()
palindrome.reverse()
if list==palindrome:
    print("it is a palindrome")
else:    print("it is not a palindrome")
