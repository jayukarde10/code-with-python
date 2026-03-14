##polymorphism 
##when the same operator is allowed to have different meaning according to the context is called polymorphism

# print(2+3) #5
# print("jay"+" ukarde") 
# print([1,2]+[3,4])

## what to achive without poly
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(self.real,"i+",self.img,"j")

    def add(self1,self2):
        newReal=self1.real+self2.real
        newImg=self1.img+self2.img
        return complex(newReal,newImg)

num1=complex(10,20)
num1.shownumber()

num2=complex(5,7)
num2.shownumber()

num3=num1.add(num2)
print(num3.shownumber())


#with poly by dunder function __ __ 
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(self.real,"i+",self.img,"j")

    def __add__(self1,self2):
        newReal=self1.real+self2.real
        newImg=self1.img+self2.img
        return complex(newReal,newImg)

num1=complex(10,20)
num1.shownumber()

num2=complex(5,7)
num2.shownumber()

num3=num1+num2 #imp
print(num3.shownumber())



#dunder function
# Method	Operator
# __add__	+
# __sub__	-
# __mul__	*
# __truediv__	/
# __str__	print()
# __len__	len()
# __eq__	==
# __lt__	<
