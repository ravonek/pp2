#Syntax 

if 5 > 2:
  print("Five is greater than two!")
  


if 5 > 2:
print("Five is greater than two!") #error

#---------------------------------------------------------------------------------

#Comments 

#---------------------------------------------------------------------------------

#This is a comment
print("Hello, World!")

print("Hello, World!") #This is a comment

#print("Hello, World!")
print("Cheers, Mate!")

#This is a comment
#written in
#more than just one line
print("Hello, World!")

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")


#-------------------------------------------------------------------------

#Variables

#-------------------------------------------------------------------------

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#-------------------------------------------------------------------------

#Casting

#-------------------------------------------------------------------------

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#-------------------------------------------------------------------------

#Variables

#-------------------------------------------------------------------------

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

#Legal var names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)     


x = 5
y = 10
print(x + y)


x = 5
y = "John"
print(x, y)


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()



x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#-------------------------------------------------------------------------

#Data types

#-------------------------------------------------------------------------

x = 5
print(type(x))

x = str("Hello World")	                    str	
x = int(20)	                                int	
x = float(20.5)	                            float	
x = complex(1j)	                            complex	
x = list(("apple", "banana", "cherry"))	    list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	                            range	
x = dict(name="John", age=36)	            dict	
x = set(("apple", "banana", "cherry"))	    set	
x = frozenset(("apple", "banana", "cherry") frozenset	
x = bool(5)                             	bool	
x = bytes(5)	                            bytes	
x = bytearray(5)	                        bytearray	
x = memoryview(bytes(5))	                memoryview



#-------------------------------------------------------------------------

#Numbers

#-------------------------------------------------------------------------

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))


x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


import random

print(random.randrange(1, 10))



#-------------------------------------------------------------------------

#Casting

#-------------------------------------------------------------------------


x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'



#-------------------------------------------------------------------------

#Strings

#-------------------------------------------------------------------------


print("Hello")
print('Hello')


a = "Hello"
print(a)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = "Hello, World!"
print(a[1])


for x in "banana":
  print(x)
  
  
  a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
  
  
txt = "The best things in life are free!"
print("expensive" not in txt)


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
  
  
b = "Hello, World!"
print(b[2:5])


b = "Hello, World!"
print(b[:5])



b = "Hello, World!"
print(b[2:])


b = "Hello, World!"
print(b[-5:-2])


a = "Hello, World!"
print(a.upper())


a = "Hello, World!"
print(a.lower())


a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


a = "Hello, World!"
print(a.replace("H", "J"))


a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


a = "Hello"
b = "World"
c = a + b
print(c)




a = "Hello"
b = "World"
c = a + " " + b
print(c)



age = 36
txt = "My name is John, I am " + age
print(txt)


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



txt = "We are the so-called \"Vikings\" from the north."




