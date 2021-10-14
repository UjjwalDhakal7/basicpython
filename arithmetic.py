# Artihmetic operators in Python


a = 20
b = 10

# Subtraction : 

print(a-b)

# Addition operator :
# It is used for arithmetic addition as well as string concatenation purpose.

print(a+b)
print('Apple'+'products')

# Multiplication operator :
# It is used for arithmetic multiplication as well as string repetition/multiplication operator.

print(a*b)
print(10*3)
print('apple\t'*3)  #It only works whwn any one of the arguments is a string.
print(3*'apple\t')  #here, in both cases output will be same, order doesn't matter.


# Division operator :

print(a/b)
# Normal division(/) operator provides result in floating point value.


# floor division operator (//)
# It gives output as int value.
# If both arguments are int then output is also int, but if any argument is float then output is float value.

#check below examples to know how normal and floor division works.
print(10//2)
print(10.0//2)

print(10/3)
print(10.0/3)
print(10//3)
print(10.0//3)

print(20/2)
print(20.5/2)
print(20//2)
print(20.5//2)
print(30//2)


# NOTE : 
# If any number is divided by zero '0', it will result in zerodivision error.
# If any string is multiplied with bool value, internally it will serve as int values :
print('apple'* True)
print('apple' * False)


# Exponential operator(**)

print(10**3)
