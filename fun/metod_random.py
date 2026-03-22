import random
print(random.randint(0,99))#random.randrange(start, stop, step)
print(random.choice([1,"jay",63]))
print(random.random())#gives random float value between 0 and 1

l = [1, 2, 3, 4]
random.shuffle(l)
print(l)

print(random.uniform(1, 5))#gives random float value between 1 and 5

l = [1, 2, 3, 4, 5]
print(random.sample(l, 2))#gives 2 random values from list l

