#function call itself repeatedly

def back(n):
    if(n==0):# base case  is most imp
        return #end
    print(n)
    back(n-1) # function called insight func


back(5)

#note call stack in recursion searck pn google

#factorial in recursion

def fac(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fac(n-1)
    
    
print(fac(5))

#sum of first n natural no.
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
print(sum(10))


def p(list,idx=0):
        if (idx==len(list)):
            return 
        print(list[idx])
        p(list,idx+1)
         
n=[1,2,3,45,6]
p(n)