# Logical Operators

''' For boolean types :

and --> returns True iff both arguments are True
or  --> returns True iff any one argument is True
not --> returns True iff input argument is False '''

# truth table for and
print(True and False)
print(True and True)
print(False and True)
print(False and False)

# truth table for or
print(True or False)
print(True or True)
print(False or True)
print(False or False)

# truth table not
print(not True)
print(not False)


#Wap to check if the username and password of user is correct.


username1 = input('Enter your username : ')
password1 = input('Enter your password: ')
        
if username1 == 'apple123' and password1 == 'password321':
    print('Welcome to the app ...')
else:
    print('Please enter correct username or password')


''' For non-boolean types :

In non boolean types the result is not True or False, but is either x|y.

x and y --> result is x|y but not boolean type :
if x evaluates to False, the result is y.
if x evaluates to true, the result is x.

x or y --> result is x|y but not boolean type :
if x evaluates to True, the result is x.
if x evaluates to False, the result is y.

NOTE:
0  means False
non-zero means True
empty(string, lists, tuples, dict, sets) are False
'''

print(10 and 20) # here 10 is True and 20 is True, result is 20
print(0 and 20) #here 0 is False and 20 is True, result is 0

print(10 or 20) # here 10 is True, result is 10
print(0 or 20) #here 0 is False and 20 is True, result is 20

a = {}
print('apple' and a) # here apple is True but a if False, the  ans is {} i.e a






