#input() ALWAYS RETURNS STRING (str)

a=input()
print(type(a),a)
b=input("Enter value of b: ")
age=int(input("age"))
price=float(input("price of item: "))

a, b = map(int, input("Enter two numbers: ").split())
print(a, b)
a,b=map(int,input().split())