#we learn about integer datatypes here:
#'int' can be used to represent short and long integer values in python 3
# python 2 has  a concpet of 'long' vs 'int' for long and short int values.
#There are four ways to define a int value :
#decimal, binary, octal, hexadecimal forms
#decimal number system is the default number system

#To define a binary number it should have a prefix '0b' or '0B':
a = 0b1111
A = 0B11001
print(a)
print(A)

#To define a octal number it should have a prefix '0o' or '0O':
b = 0o1341
B = 0O12301
print(b)
print(B)

#To define a hexa number it should have a prefix '0x' or '0X':
c = 0x2342AB
C = 0X43667F
print(c)
print(C)

#in case of Hexa form python does not follow case sensitiveness.
print(0xBeef)
print(0XAbcD)


#Base Conversion Functions :

#1. bin()
#can be used to convert other forms of number to binary number system.
bin(0o127)
bin(15)
bin(0X12A)

#2. oct() >>
#can be used to convert other forms of number to octal number system.
oct(0b100110)
oct(15)
oct(0X12A)

#3. hex() >>
#can be used to convert other forms of number to binary number system.
hex(0o127)
hex(15)
print(hex(0b100110))

