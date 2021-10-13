#Mutable objects :
# Objects that are changeable are mutable.


#Immutable objects :
# Once we create an object we cannot peform any changes, if we try to perform any change, those changes will create a new object.

x = 1
print(id(x))
x = x+1
# here, the value of x increases to 2, 1 doesn't have a reference variable and is subjected to garbage collection.
# also, 2 is the newly created object while we tried to change an exisiting object 1, shows the immutability of int datatypes.
print(id(x))


# Importanc of immutability :


#memory utilization.
a= 10
b =10
c =10

print(id(a))
print(id(b))
print(id(c))
#while creating a new object, python checks if the required new value already exists, is it exists then the reference is directed to the existing object.

#It also improves the performance.

#It is applicable for int, float, str and bool but not for complex among the fundamental datatypes.

