# Precedence of Operators in Python.
'''
( ) --> parenthesis

**  --> exponential operator

~,- --> bitwise complement operator, unary operator

*,/,%,//    --> multiplication, division, modulo, floor division

+,- --> addition, subtraction

<<,>>   --> left shift, right shift operator

&   --> Bitwise And

^   --> Bitwise X-OR

|   --> Bitwise OR

>, >=, <, <=, ==, !=    --> Relational / comparision operator

=, += , -=, *=  --> assignment operators

is, is not  --> Identity operators

in, not in  --> Membership operators

not --> Logical not

and --> Logical and

or --> Logical not

If two operators have same precedence then it will operate from left to right.
'''

a = 30
b = 20
c = 10
d = 5

print((a+b)*c/d)
print((a+b)*(c/d))
print((a+(b*c)/d))

print(3/2*4+3+(10/5)**3-2)
