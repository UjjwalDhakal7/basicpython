#String datatypes
#Any sequence of characters within single or double quotes is a string.

a = 'Hello World'
A = "Hello World"

print(type(A))
print(type(a))


#Using triple quotes to represent a string.

#1. To define a doc string.
#2. To enclose string values having single or double quotes.

a = 'I love python programming.'
b = 'I want to be a "Python developer".'
c = "I am learning 'string' literals."
d = """It is 'fun to learn' when you understand the concept."""
e = '''"Python" is the 'msot popular' language in the world.'''

print(a,b,c,d,e)

#3. To define multi line string literals.

f = """I
am
a
programmer."""
print(f)


#Accesing a character by Index

#We can use the index to fetch a character.

print(a[2])
print(a[-3])
#Python supports both forward and negative index

#Slicing a string

#syntax : s[beginning index : (end-1) index]

z = 'abcdefghijklmnopqrstuvwxyz'
print(z[3:9])

#If we don't assing the beginning index, the default value will be last.

print(z[:10])

#If we don't assing the ending index, the default value will be last.

print(z[3:])

#example : if we have to print love from 'a' then:

print(a[2:6])

print(z[:]) #will print the whole string.

#slice operators never gives index error.

print(z[5:2000])  #will print from the 5th to last.

print(z[20:1]) #will return an empty value as there in not 1 index after 20.



#Applications of Slice operators

# Concatenation ; '+' can be used to join strings together

i = 'Nation'+'300'
print(i)

#Star Operator : string repetition operator

j = 'Nepal'
print(j*5)
print(5*j)
print(j*len(j))

#Note : * operator works as long as one argument is string and other is int.


#to print the first character in uppercase
b = 'apple'
output = b[0].upper()+b[1:]
print(output)

#to print the last character in uppercase

output = b[0:4]+b[-1].upper()
print(output)

#to print the first and last character in uppercase

p = 'this is my program'
output = print(p[0].upper()+p[1:len(p)-1]+p[-1].upper())


