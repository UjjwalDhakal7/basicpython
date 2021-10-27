# Command line arguments :
'''
The arguments that are passed from command prompt directly while executing program.
We can import 'argv' variable from 'sys' module to perform this type of operation.
'''

from sys import argv
print(argv[0])
print(argv[1])

#while executing we can enter arguments as " py test.py 10 20 10 30" in cmd prompt.

# Progam to print command line information.

from sys import argv
print('The number of command line arguments : ',len(argv))
print('The list of command line argumemnts : ',argv)
print('The command line arguments one by one : ')
for x in argv:
    print(x)

# Program to print sum of arguments input from command line arguments.

from sys import argv
args = argv[1:]
sum = 0 
for x in args:
    sum = sum + int(x)
print('The sum is :', sum)

# py test.py 10 20 10 30 will return the sum.
