# Output statements in python :

 # print() without any arguments :
'''
 This will insert  new line (\n) after the phrase
 e.g : print('abcd')
       print('defg')

 print(string) : In this we can use escape characters in between the phrase.

 print('abc'+'def'), Print('abc'*10) : we can use concatenation and string multiplication

 - We can print multiple arguments at once :

 eg : print('Given value are : ',a,b,c)
 '''
 
# print() with sep attribute :
'''
 - By default, the seperator between arguments is space ' ', but we can change the separator
   by using 'sep' attribute.
 eg : print('Given value are : ',a,b,c,sep=':')
 - We use this attribute when there are multiple arguments.
'''
# print() with end attribute :
'''
 - we know that python inserts new line character after given phrase. We can change that by using
   end attribute. This will lead to printing new phrase along with the previous phrase.
   e.g : print('hello')
         print('world')
         print('hello', end = '')
         print('wprld')
         
- Similarly we can add separator by using end attribute after end of a phrase.
   e.g : print('hello', end = '::')
         print('world')
         print('hello', end = '+')
         print('world')
-  - We use this attribute when there are multiple print statements.
'''

a,b,c = 1,2,3
print('Given value are : ',a,b,c)
print('Given value are : ',a,b,c, sep=':')

print('hello')
print('world')
print('hello', end = '')
print('world')

print('hello', end = '+')
print('world')

print('hello', end = '::')
print('world')


print(10,20,30, sep=':', end='**')
print(40,50,60, sep=':')
print(70,80, sep='**', end='$$')
print(90,100)


# print(object)
'''
- We can pass any type of object to the argument.
- The object can be list, tuple, set, etc.
'''
# print() with replacement operator {}
'''
- in this method we can create placeholder and later enter value by using '.format' function.

e.g :print('Hello {}, your salary is {}, you work on the {} floor and live in {}'.format(name,salary,floor,address))

- we can also use indexing in the palceholder. The index value will be accessed from the arguments in .format()
    print('Hello {0}, your salary is {1}, you work on the {2} fl oor and live in {3}'.format(name,salary,floor,address))

- we can also use keyword alteration i.e we can pass altered keyword in place of index.
   name = 'Abish'
   print('Hello {a}, your salary is {s}).format(n=name,s=salary))

'''

name = 'Shivam'
salary = 45000
floor = '4th'
address = 'Kathmandu'
print('Hello {}, your salary is {}, you work on the {} floor and live in {}'.format(name,salary,floor,address))
print('Hello {0}, your salary is {2}, you work on the {1} floor and live in {3}'.format(name,salary,floor,address))
print('Hello {n}, your salary is {s}'.format(n=name,s=salary))

# print() with formatted string
'''
- This format is more powerful than replacement operator. 
%i --> signed integer value
%d --> signed decimal value
%s --> signed string value
%f --> signed float value

syntax : print('formatted string'%variable)
e.g : print('The value of a is %i'%a)

'''

a = 20
print('The value of a is %i'%a)

a,b,c = 10,20,30
print('THe value of a=%d,b=%d,c=%d'%(a,b,c))

name = 'Shivam'
marks = [10,20,30]
print('Hello %s, your marks are %s'%(name,marks))


