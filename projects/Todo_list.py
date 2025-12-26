g=int(input("chose a option \n1.start\n ::::"))
list=[]
while g==1:
    print("It's Todo List \n chose a option\n 1.add in list \n 2.remove from list\n 3.show list\n4.end ")
    option=int(input("enter a option no."))
    

    if option==1:
       n=int(input("enter how many task"))
       for i in range(0,n):
          a=input("enter a task one by one")
          list.append(a)
     
  
    if option==2:
       print(list)
       b=int(input("chose which task has to delete"))
       list.pop(b-1)
       print(list)
    
    if option==3:
       print(list)
       
    if option==4:
        print("byy")
        break