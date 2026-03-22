import random
import string

charvalues=string.ascii_letters+string.digits+string.punctuation

password=""
for i in range(8):
    password+=random.choice(charvalues)
print(password)


l=[random.choice(charvalues) for i in range(8)]
print(l)


l="".join([random.choice(charvalues) for i in range(8)])
print(l)

l="*".join([random.choice(charvalues) for i in range(8)])
print(l)