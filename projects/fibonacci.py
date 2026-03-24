# n=int(input("enter a range"))   #0+1+1+2+3+5
# a=0
# b=1
# print(a,"+",b)
# for i in range(1,n+1):
#     c=a+b
#     print("+",c)
#     a=b
#     b=c

n = int(input("enter a range: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

    
