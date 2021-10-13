# Multiple datatypes are available that can store group of values.
# eg. list, tuple, sets, dictionary, etc

#List :
# 1. order is important,
# 2. duplicate objects allowed,
# 3. values should be within square brackets,
# 4. Heterogenous objects are allowed,
# 5. List is growable,
# 6. List is mutable in nature i.e we can change the objects as necessary.

# syntax :
a = [10,20,30,40,10]
print(type(a))

l = []              #creating an empty list 
l.append(10)        #adding an element to list
l.append(45)
print(l)

l.remove(45)        #removing an object from list
print(l)            

a[0] = 5            #changes the object 10 to 5
print(a)

# Tuple : 
# 1. order is important,
# 2. duplicate objects allowed,
# 3. values should be within round brackets,
# 4. Heterogenous objects are allowed,
# 5. Tuple is read only form of list,
# 6. Tuple is immutable in nature i.e we cannot change the objects as necessary.


# syntax :
a = (10,20,30,40)
print(type(a))

l = ()             #creating an empty tuple 
l = (10)            # it is an int value not tuple
l = (10,)           # single value tuple should have a comma at the end

#Sets :
# syntax : a{10,20,30,40}

#Dictionary :
# suntax : {100 : 'abcd'}
