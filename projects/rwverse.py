n=input("")
s=""
for i in range(len(n)-1,-1,-1):
    s+=n[i]

print(s)

print(n[::-1])

#sliceslicing
l=[]
for i in range(len(n)):
    l.append(n[i])
print(l)

