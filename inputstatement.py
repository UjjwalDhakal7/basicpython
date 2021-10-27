#Wap to read data from employee from the keyboard and print the data.
'''
eno = int(input('Enter employee number :'))
ename = input('Enter Employee name :')
esal = float(input('Enter Employee salary : '))
eadd = input('Enter Employee address :')
estatus = eval(input('Enter marriage status? [True|False] :'))

print('Please confirm entered info')
print('Your entered info : \n', eno, ename, esal, eadd, estatus)

'''
# reading multiple value from the keyboard in a single line :
'''
a,b = [int(x) for x in input('Enter 2 numbers : ').split()]     # .split() splits a string based on space by default
print('Sum : ',a+b)
'''

#WAP to read 3 float values from the key board with ',' separation and print the sum.

a,b,c = [float(x) for x in input('Enter 3 float numbers:').split(',')]
print('Sum: ', a+b+c)


# eval() fuction :

# This function evaluates entered input and return their corresponding datatypes.
# If an expression is provided then it will convert values internally and return the output.

x = eval(input('Enter  something: '))
print(type(x))

