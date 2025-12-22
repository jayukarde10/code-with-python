#int
a,b,c=10,-5,0
print(type(a),type(b),type(c))

#float
x=3.14
print(type(x))

#complex
p=2+3j
print(type(p))

#bool
# = → assignment (used to assign value)
# == → comparison (used to check equality)
r=(1==1)
s=(1<2)
print(f"{r}, {s}")
flag1=True
flag2=False
print(type(flag1),type(flag2))

#str
name="Python"
print(type(name))

#list
mylist=[10,20,30,40,50]
print(type(mylist))

#tuple
mytuple=(10,20,30,40,50)
print(type(mytuple))

#set
myset={10,20,30,40,50}
print(type(myset))

#dict
mydict={"name":"Python","version":3.8}
print(type(mydict))

#none
n=None
print(type(n))  

#bytes
b=b'Hello'
print(type(b),b)

#bytearray
ba=bytearray(b'Hello')
print(type(ba)) 

#range
r=range(5)  
print(type(r))  

#frozenset
fs=frozenset([10,20,30,40,50])
print(type(fs))

#memoryview
mv=memoryview(b'Hello') 
print(type(mv))

#end of the code
