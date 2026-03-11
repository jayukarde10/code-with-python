##static method it use if there are no use of self in method

class student():
    
    @staticmethod #decorator
    def college():
        print("hello")

    def __init__(self,name):
        self.name=name

s1=student("jay")
print(s1.name)
s1.college()

##del keyword
##used to delete object properties or object itself
#syntax del s1.name or del s1

# del s1.name
# print(s1.name) 

#to make attribute private in class that should not visible outside the class 
# we make attribute or method private by writing atribute like __atribute

class acc:
    def __init__(self,accno,passwd):
        self.accno=accno
        self.__passwd=passwd #private 
a1=acc(2122,"1010b")
print(a1.accno)
print(a1.__passwd) #you could not acces becuse it outside the class
 