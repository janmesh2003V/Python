#-------------------------------------------# Set in Python #-----------------------------------------#

# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable.


num1 = {1, 2, 3, 4, 5}

print ( num1 )

print ( type (num1) )

# but,

num2 = {1, 2, 3, 3, 3, " hello ", "janmesh", "janmesh"}

print ( num2 ) # O/p => {1, 2, 3, 'janmesh', ' hello '} " duplicate value ko ignore karega "


## Empty Set kaise banta hai 👇


num3 = {}                   # Isko python mai Empty Dictionary hi samjhega

print ( num3 )              # O/p => {} but , " Yeh Set nhi hai"
print ( type ( num3 ) )     # O/p => <class 'dict'>  "Yeh tho Set nhi hai "


num4 = set ()               # yeh hai tarika Empty set ko create karne ka

print ( type ( num4 ) )     # O/p => <class 'set'>  


