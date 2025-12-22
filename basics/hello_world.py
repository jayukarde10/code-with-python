print("hello world !")
# different way of printing statement

a=10
print(a)
print("value of a is ",a)
print(f"value of a is {a}")
print("value of a is {}".format(a))
print("value of a is %d"%a)
print("value of a is "+str(a))
print("value of a is ",a,end="-""\n")
print("value of a is ",a,sep="---")
# end and sep are special parameters of print function
# end is used to specify what to print at the end of the statement (default is newline)
# sep is used to specify what to print between multiple values (default is space)       
print("hello","world","from","python",sep="***",end="!!!\n")
# different ways of printing multiple values
print("value of a is ",a,"and value of b is ",20)
b=20
print(f"value of a is {a} and value of b is {b}")
print("value of a is {} and value of b is {}".format(a,b))
print("value of a is %d and value of b is %d"%(a,b))
print("value of a is "+str(a)+" and value of b is "+str(b))

