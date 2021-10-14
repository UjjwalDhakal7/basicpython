# Relational Operators

# used for the basic comparision features.
a = 10
b = 20

print(a<b)
print(a>b)
print(a<=b)
print(a>=b)


# relational operators can be used to compare str values too, compares based on unicode (ASCII) value.
s1 = 'rabbit'
s2 = 'leopard'
print(s1<s2)

# to find the ASCII value of a character :
print(ord('a'))

#to find the character from ASCII value:
print(chr(97))

# chain comparision

# If all comparisions is true, result is true.
# If any of the comparision is false, result is false.
print(10<20<30)
print(10<20<30<40)
print(10<20<30<40>50)



#WAP to input two numbers and compare them.
a = input('enter a numbers : ')
b = input('enter a number : ')
if a> b:
    print('a is greater')
else:
    print('b is greater')
