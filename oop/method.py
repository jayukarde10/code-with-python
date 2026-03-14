## type of method/decorator
#instance using (self)
#static using @staticmethod 
#class using (cls) @classmethod




##static method it use if there are no use of self in method

# class student():
    
#     @staticmethod #decorator
#     def college():
#         print("hello")

#     def __init__(self,name):
#         self.name=name

# s1=student("jay")
# print(s1.name)
# s1.college()

##del keyword
##used to delete object properties or object itself
#syntax del s1.name or del s1

# del s1.name
# print(s1.name) 

#to make attribute private in class that should not visible outside the class 
# we make attribute or method private by writing atribute like __atribute

# class acc:
#     def __init__(self,accno,passwd):
#         self.accno=accno
#         self.__passwd=passwd #private 
# a1=acc(2122,"1010b")
# print(a1.accno)
# print(a1.__passwd) #you could not acces becuse it outside the class
 

##class method is bound to the class & receive the class as implicit first argument 
##static method cant access or modify class state & generrally for utility function

class student:
    name="anonymus"

    def changeName(self,name):
        self.name=name ##change to person.name

s=student()
s.changeName("Jay")
print(s.name)
print(student.name) #it still anonymus that shows class name is diiferent and object name is different

print("--------------different---------------------")
## to solve this we can change
#  self.name to student.name
# or self.__class__.name

#or class method
class student1:
    name="anonymus"
    @classmethod
    def changename(cls,name):
        cls.name=name

    

s=student1()
s.changename("Jay")
print(s.name)
print(student1.name)

print("--------property------------")

##problem
class student3:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        self.percentage=str((self.phy+self.chem+self.maths)/3)+"%"

s3=student3(91,92,93)
print(s3.percentage)

##if techer enter wrong mark and change
s3.phy=86
print(s3.phy)
print(s3.percentage) #not get change

##solution
class student4:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
       
    def percentage(self):
        return (self.phy+self.chem+self.maths)/3

s3=student4(91,92,93)
print(s3.percentage())

##if techer enter wrong mark and change
s3.phy=86
print(s3.phy)
print(s3.percentage())

##and advance python by usung @property it take method as attribute not method

class student5:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
    @property  
    def percentage(self):
        return (self.phy+self.chem+self.maths)/3

s3=student5(91,92,93)
print(s3.percentage)

##if techer enter wrong mark and change
s3.phy=86
print(s3.phy)
print(s3.percentage) ##without ()


##setter method
# control how value is changed

class Student7:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value < 0 or value > 100:
            print("Invalid marks")
        else:
            self._marks = value

s = Student7(85)

s.marks = 95
print(s.marks)
s.marks = 120

##deleter method
# control what happen when an attribute is deleted

class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        self._marks = value

    @marks.deleter
    def marks(self):
        print("Deleting marks...")
        del self._marks

s = Student(85)
print(s.marks)
del s.marks


##geter method
# control how value is accessed

class Student8:
    def __init__(self, marks):
        self._marks = marks

    def get_marks(self):
        return self._marks
    
s = Student8(85)
print(s.get_marks())#get_marks() is the getter
                    #Must call with ()

##Why _marks (underscore)?
# Convention in Python:
# _marks
# means internal/private variable.
# We don't access it directly.



#marks      → public
# _marks     → protected (convention)
# __marks    → private (name mangling)