# Ternary operators :

# Ternary operators in python is user friendly compared to other languages.
# Syntax : x = first value if condition else second value

a= 10
b = 20
c = 30 if  a>b else 40
print(c)


# WAP to read two int values and print minimum value by using ternary operatora = int(input('Enter first value :'))
b = int(input('Enter second value :'))

min = a if a<b else b
print(min)


# Ternary operators can be nested :

# WAP to read three int values and print minimum value by using ternary operator.

a = int(input('Enter first value :'))
b = int(input('Enter second value :'))
c = int(input('Enter third value :'))
min = a if a<b and a<c else b if b<c else c
print(min)


# WAP to read two int values and print minimum value by using ternary operator.

a = int(input('Enter first value :'))
b = int(input('Enter second value :'))

x = 'equal' if a == b else 'small' if a<b else 'great' 
print(x)
