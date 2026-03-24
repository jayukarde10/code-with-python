n=input("")
s=""
for i in range(len(n)-1,-1,-1):
    s+=n[i]

print(s)

print(n[::-1])

#sliceslicing
l=[]
for i in range(len(n)-1,-1,-1):
    l.append(n[i])
print(l)

#
n = int(input("Enter a number: "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reversed number:", rev)

