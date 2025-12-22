# strings in Python are arrays of unicode characters.

a="hello"
print(a[1])  #prints 'e'    
#strings are immutable

#slicing
b="Hello, World!"   
print(b[2:5])   #prints 'llo'
print(b[:5])    #prints 'Hello' 
print(b[2:])    #prints 'llo, World!'
print(b[-5:-2]) #prints 'orl'

#string length
print(len(b))   #prints 13

#string methods
txt="hello world"
for x in txt:
    print(x)    #prints each character in new line
print(txt.upper())    #prints 'HELLO WORLD'
print(txt.lower())    #prints 'hello world'
print(txt.strip())    #removes whitespace from both ends
print(txt.replace("h","j"))   #prints 'jello world'
print(txt.split(" "))    #prints ['hello', 'world']
print("hello" in txt)   #prints True
print("hi" not in txt)  #prints True
print(txt.index("w"))   #prints 6
print(txt.count("l"))   #prints 3

#string concatenation
a="Hello"
b="World"
c=a+" "+b
print(c)    #prints 'Hello World'

#string formatting
age=25
txt="My name is John, and I am {}"
print(txt.format(age))   #prints 'My name is John, and I am 25'
txt="My name is John, and I am {} years old"
print(txt.format(age))   #prints 'My name is John, and I am 25
txt="My name is John, and I am {age} years old"
print(txt.format(age=age))   #prints 'My name is John, and I am 25 years old'
txt="My name is {0}, I am {1} years old"
print(txt.format("John",age))   #prints 'My name is John, I am 25 years old'

#
txt="the best thing in live is to live"
if "live" in txt:
    print("yes, 'live' is present.")   #prints yes, 'live' is present.

print("live" in txt)  #prints True

if "hate" not in txt:
    print("no, 'hate' is not present.")  #prints no, 'hate' is not present.
print("hate" not in txt)  #prints True


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)  #prints The price is 59.00 dollars

#escape characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)  #prints We are the so-called "Vikings" from the north

txt = 'It\'s alright.'
print(txt)  #prints It's alright.
txt = "Line1\nLine2\nLine3"
print(txt)
 
 #Escape Characters
#Other escape characters used in Python:

#Code	Result	Try it
#\'	Single Quote	
#\\	Backslash	
#\n	New Line	
#\r	Carriage Return	
#\t	Tab	
#\b	Backspace	
#\f	Form Feed	
#\ooo	Octal value	
#\xhh	Hex value

#------------------------------------------------------

#string methods
# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
