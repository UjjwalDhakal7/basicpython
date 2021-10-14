# Equailty operators

# equals to (==)
print(10==20)
print(1==True)


# not equals to (!=)
print(10!=20)
print(0!=False)

# equality results 'False' as output when incompatible datatypes are compared
print(10 == 'apple')
print(10 == '10')


#chain of  equality operators

# if all comparisions is True, result is True.
# If at least one comparision if False, result is False.

print(10 == 20 == 40)
print(10 == 10 == 10)


# NOTE :  The difference between '==' and 'is' operators :

# '==' is use for content comparision.
# 'is' is used for reference(address) comparision.

l1 = [10,20,30]
l2 = [10,20,30]

print(l1 is l2) # the result will be False as l1 and l2 are located at separate address location.
print(l1 == l2) # the result will be True as the content is same.

l3 = []
l1 = l3

print(l1 is l3) # the result will be True as both l1 and l3 refers to the same address location.
