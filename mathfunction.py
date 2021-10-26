# Modules in Python

'''
Module is a simple python (.py) file contains a collection of variable, functions and classes.
We can use already designed module in new programs by importing them.
The biggest advantage of having a module is code reusability.
e.g : math, threading, time, random

Syntax :

import dmath            *importing a module/ dmath is a module that already exists
dmath.add(10,20)        *add, sub is a function already defined in dmath module
dmath.sub(50,20)


from math1 import *         *importing all functions from the module at once
from math2 import *
print(sqrt(4))              *In case of multiple similar imports the most recent module/function is always taken, math2 in this case

Important functions present in math module :

sqrt(x)
floor(x)
ceil(x)
pow(x)
gcd(x)
sin()

Important variables present in math module :

pi   --> pie function
exp  --> exponential function 
inf  --> infinite number
nan   --> not a number
'''


import math
print(dir(math))     # gives every functions in-built in math module


print(math.sqrt(16))
print(math.e)
print(math.pow(3,5))
print(math.floor(3.999))

'''
Since we have to use 'math.' everytime with a function, it might be boring for modules with long names,
so we can create an alias name for modules and functions to make it short,
but once we create alias name we cannot use original module name.
Also we can import one, two or all the functions at once by using 'import pow', or 'import *'
'''

import math as m         # here m is alias name for module Math
print(m.pi)             

from math import sqrt as s
print(s(16))             # gives the square root of 16



#Wap to display the area of circle using math function.

from math import *         # most commonly used import structure
r = int(input('enter the radius of circle :'))
print('The area of the circle is : ', pi*pow(r,2))







