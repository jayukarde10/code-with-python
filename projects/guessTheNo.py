import random
target=random.randint(0,99)


n=int(input("Guess the number: "))
while True:
    if n<target:
        print(f"{n} is less than target")
        n=int(input("enter no once again"))
    elif n>target:
        print(f"{n} is greater than target")
        n=int(input("enter no once again"))
    elif n==target:
        print("number  matched")
        break