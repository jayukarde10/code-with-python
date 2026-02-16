list=[]
n=int(input("enter choise :: 1)Start 2)End\n"))
while n==1:
   c=int(input("enter a choise::\n 1.insert 2.delete 3.display 4.exit"))
   if(c==1):
      t=int(input("how many insertion"))
      for i in range(0,t):
         l=(input("insert in list "))
         list.append(l)
   elif(c==2):
        r=input("what have to delete")
        list.remove(r)
   elif(c==3):
       print(list)
   elif(c==4):
        break
   else:
       print("chose correct option")
while n==2:
    print("sucessfully ended")  
    break