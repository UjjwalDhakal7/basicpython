# Special Operators :

# There are two types of special operators in python.

# Identity operators :

'''
is     :
- used for address comparision only
- True iff both objects are referring to the same object.

is not :
- used for address comparision only
- True iff both objects are not referring to the same object.
'''

a = 10
b = 10
print(a is b)
print( a is not b)

L = [10,20]
M = [10,20]
print(L is M)     # is False as L and M are located in separate locations.



# Membership operators :

'''
in :
- True if certain object is in a list of sequence like list, tuple etc

not in :
- False if certain object is not in a list of sequence like list, tuple etc

'''
a = 'This is a python program'
print('z' in a)
print('r' in a)
print('p' not in a)
print('This' in a)

z = ['rohit', 'rahul', 'kohli']
print('rahul' in z)
print('chahal' in z)
