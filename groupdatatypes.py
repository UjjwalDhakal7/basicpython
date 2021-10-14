# Multiple datatypes are available that can store group of values.
# eg. list, tuple, sets, dictionary, etc

#list :
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
l.append(10)        #adding an element to list, will always add th object at last
l.append(45)
print(l)

l.remove(45)        #removing an object from list
print(l)            

a[0] = 5            #changes the object 10 to 5
print(a)

# tuple : 
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

#sets :
# 1. order is not important, or guarenteed
# 2. duplicate objects are not allowed, but ignored
# 3. values should be within curly brackets,
# 4. Heterogenous objects are allowed,
# 5. indexing is not applicable, set object is not suscriptable(slicing not applicable)
# 6. Set is growable & mutable in nature i.e we can change the objects as necessary.


# syntax :
a = {10,20,30,40}
print(type(a))

a.add(50)  #we use .add because there is no guarentee wher the object is added in the set.
print(a)
a.remove(50)
print(a)

l = set()   #creating an empty set we have to call set function, as l = {} is an empty dcitionary.
print(type(l))

#Frozenset :
# 1. It is same as set but not mutable.

# syntax :
a = {10,20,30,40}
fs  = frozenset(a)      #we have to call the frozenset function after declaring a set.
print(type(fs))
print(fs)               #It is displayed as a frozenset.


#dict :
# 1. We use dict datatypes when we have to represent key-value pairs.
# 2. duplicate keys are not allowed, but values can be duplicated, if we add duplicate keys the old value is updated with new value.
# 3. key-values should be within curly brackets,
# 4. Heterogenous objects are allowed,
# 5. order is not important, or guarenteed
# 6. Dict is mutable in nature i.e we can change the objects as necessary.
# 7. Indexing, slicing not applicable.



# syntax :
s = {1:'Aakash', 2:'Babin', 3:'Dipesh', 4:'Zaheer'}
print(type(a))
print(a)

d={}        #creating an empty dictionary
#To add a key-value to an existing dictionary : d[key] = 'value'
d[5]='Manoj'
print(d)
d[6]='Naman'
print(d)
d[7]='Manoj'
print(d)
d[6]='Henna'
print(d)


# range :

# 1. It is inbuilt python datatypes defines a range or sequence of data,
# 2. duplicate keys are not allowed, but values can be duplicated, if we add duplicate keys the old value is updated with new value.
# 3. range is immutable in nature i.e we cannot change the objects as necessary.
# 4. Indexing, slicing is applicable.


# syntax :

r =range(10)
# s = range(0, end)
#This is the first form where the range starts from 0 to range(n-1).

print(type(r))
print(r)
#the above command will print the range of data, so to print individual data we use loop.

for x in r:
    print(x)

s = range(10,20)
# s = range(begin, end)
#This is the second form where the range starts from 10 to range(20-1).

for x in s:
    print(x)

t = range(20,31,2)
u = range(100,1,-5)
# t = range(begin, end, increment or decrement by)
#This is the third form where the range starts from 0 to range(n-1) and increment is by 2.
for x in t:
    print(x)

for x in u:
    print(x)
print(u[2])

#slicing
u1 = u[2:6]
for x in u1:
    print(x)


# bytes :
# 1. It is inbuilt python datatypes defines a range or sequence of data,
# 2. Can only represent values from 0 ro 255
# 3. bytes is immutable in nature i.e we cannot change the objects as necessary.
# 4. Indexing, slicing is applicable.
# 5. used to handle binary data like images, video files, etc.

#syntax : 
l = [10,20,25,30,40,50]
b = bytes(l)
print(type(b))
print(b)
#the above command will print binary data, so to print individual data we use loop.
for x in b:
    print(x)
#indexing :
print(b[2])


# bytearray :
# 1. bytearray is simiar as bytes but mutable in nature.

l = [10,20,30,40,50]
b = bytearray(l)
print(type(b))
for x in b:
    print(x)

#indexing :
print(b[-1])

b[-1] = 45          #replacing a value
for x in b:
    print(x)


# None datatype :
# None means nothing, no value is associated

a = 10
a = None
print(type(a))

def f1():
    return 10
x = f1()
print(x)
print(type(x))











