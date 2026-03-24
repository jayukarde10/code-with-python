n=int(input("enter a number to check if it is prime or not: "))

if (n<2):
    print("not prime")
else:
    for i in range(2,n):
        if(n%i==0):
            print("not prime")
            break           
    else:
        print("prime")

##optimize

n=int(input("enter a number to check if it is prime or not: "))

if (n<2):
    print("not prime")
else:
    for i in range(2,int(n**0.5)+1):  # if n is 36 privious check for 2 to 36 but this whill root of 36 = 6 if it get divisible then not prime
        if(n%i==0):
            print("not prime")
            break
    else:
        print("prime")