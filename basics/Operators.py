# Operator	Name	Example	
# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y

a=int(input("enter a value"))
b=int(input("enter b value"))

print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Modulus:",a%b)
print("Exponentiation:",a**b)
print("Floor Division:",a//b)

# Comparison Operators
# Operator	Name	Example
# ==	Equal	x == y
# !=	Not equal	x != y      
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y

print("Equal:",a==b)# give True if a is equal to b else False


# Operator	Example	Same As	Try it
# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	.... bit wise ,0-1,and
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3	
# :=	print(x := 3)	x = 3  ... it assigh under print and return value
#                       print(x)



#logical Operators
# Operator	Description	Example	
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	

x=10
print("Logical AND:",x>5 and x<15) #True and True → True
print("Logical OR:",x>5 or x<8)   #True or False → True
print("Logical NOT:",not(x>5 and x<15)) #not(True and True
# → not(True) → False

#identity Operators
# Operator	Description	Example	Try it
# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

print(x is not y) #True because x is not the same object as y

# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal

#membership Operators
# Operator	Description	Example	
# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

#bitwise Operators
# Operator	Name	Description	Example	
# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

a = 60        # 60 = 0011 1100
b = 13        # 13 = 0000 1101      

print("a & b =", a & b)  # 12 = 0000 1100
print("a | b =", a | b)  # 61 = 0011 1101
print("a ^ b =", a ^ b)  # 49 = 0011 0001 The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
print("~a =", ~a)        # -61 = 1100 0011

#opwerator precedence
#Left-to-Right Evaluation
# Operator	Description	
# ()	Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR	
# |	Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	OR