#to print addition of a n no.
sum=0
n=10
for j in range(n+1):

    sum=sum+j  #***imp***

print(sum)

#for and while imp check


#by for
# def fac(n):
#     foc=1
#     for i in range(1,n+1):
#         foc=foc*i
#     print(foc)

# fac(5)

# in while

def fac(n):
    foc=1
    i=1
    while i<=n:
        foc=foc*i
        i+=1
     
    print(foc)

fac(5)


#factorial in recursion

def fac(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fac(n-1)
    
    
print(fac(5))


#imp print list
def p(list,idx=0):
        if (idx==len(list)):
            return 
        print(list[idx])
        p(list,idx+1)
         
n=[1,2,3,45,6]
p(n)