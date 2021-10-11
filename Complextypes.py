#It is a python specific datatype for enginnering and working with complex number.
# The symbol should be in the form 'a+2j', only 'j' or 'J' both canbe used.
#'a' represents the real part and 'j' represents imaginary part.


x = 10+20j
print(type(x))

#we can print real and imaginery values separately.
print(x.real)
print(x.imag)

#we can take int or float values in both real and imaginery part.
y = 10+20j
y = 10+20.6j
y = 10.5+20j

#we can take input in any form of number system in real part but only in decimal system in imaginery part.
z = 0b1110+20j
#z = 10+0b1001j is wrong

#we can perform arithmetic operations between complex numbers.
print(x+y)
print(x-y)
print(x*y)
print(x/y)
