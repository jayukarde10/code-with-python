##syntax to create class and object

# class student: #creating class
#     name="jay"
# s1=student()   #creating object or instance
# print(s1.name)

# class car():
#     color="blue"
#     brand="kia"
# car1=car()
# print(car1.color)
# print(car1.brand)


# #constructor
##self parameter is reference to the current object of class
# class student2():
#     def __init__(self): #its run as self without any object calling like that we write  s1=.. ex print(s1.name) it will be s1.self insted it is same 
#          print(self) 
#          print("hello")
# s1=student2()
# print(s1)  #run it it print same s1 and self

class student():
    # #defualt constructor
    def __init__(self): ##self is noting but object
        pass 
  
    ##parameterized constructor
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks #object atribute
    
    def hello(self): #method 
        print("hello",self.name)
    def mark(self):
        return self.marks

    college="APShah" # class atribute that for all student is same

s1=student("jay",70) #constructor get executed that have same no. of parameter
print(s1.name,s1.marks,s1.college)
s2=student("jay",70)
s2.hello()     #calling methods ( ) is imp
print(s2.mark())