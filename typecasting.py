#Type Casting or Type Cohersion
# The process of converting one type of vaue to other type.

#Five types of data can be used in type casting
# int, float, bool, str, complex

#converting float to int type :
a = int(10.3243)
print(a)
#converting complex to int type cannot be done.

#converting bool to int :

b = int(True)
c = int(False)
print(b,c)
#converting string to int type :

#string should contain int or float values which should be specified in base 10.

d = int('50')
print(d)


#converting int to float :

print(float(12))
print(float(0b101))


#converting complex to float is also not possible.

#converting bool to float :
print(float(True))
print(float(False))

#converting str to float :
print(float('200'))

#converting int, float into complex :

#Form 1 :
#entering only one argument, pvm will assume it as real value.

print(complex(1))
print(complex(10.4))
print(complex(True))
print(complex(False))
print(complex('50'))



#Form 2 :
#entering two arguments, pvm will assume first argument as real and the other as imaginery value.

print(complex(10,3))
print(complex(10.4, 10.2))
#str to complex has various restrictions.


#converting to bool types:
#For int and float types,
#if the argument is 0, the bool value will be False, else true.
print(bool(10))
print(bool(0))

#For complex types,
#if real and imaginary part is 0, bool value is False, else True.

print(bool(10+10j))
print(bool(0j))


#For str types,
#if the argument is empty then only bool value is False, else any value is True.

print(bool('True'))
print(bool("False"))
print(bool(''))



#converting to str types :

a = str(10)
b = str(0b1010)
c = str(10.67)
d = str(10+2j)
print(type(a), type(b), type(c))




