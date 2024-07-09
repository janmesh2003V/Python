----------------------------------------# 1. add("Element") #-------------------------------------------#


Set1 = { 1, 2, 3, 4, 5 }

Set1.add ( 22 )
Set1.add ( 33, 10 )             # yeh Error dega, TypeError: set.add() takes exactly one argument (2 given)
Set1.add ( 55 )

print ( Set1 )                  # O/p => {1, 2, 3, 4, 5, 22, 55}

# tuple bhi Add kar sakte hai

Set1.add (( 55, 555, 5555, 55555 ))

print ( Set1 )                    # O/p => {1, 2, 3, 4, 5, 22, 55, (55, 555, 5555, 55555)} 


----------------------------------------# 2. remove("Element") #---------------------------------------#


Set2 = { 1, 2, 3, 4, 5 }

Set2.remove ( 3 )
# Set2.remove ( 3 )                # yeh bhi error hai Ek hi value ko secod time remove nhi code kar sakte hai

# Set2.remove ( 7 )                # yeh bhi Error hai remove function mein Set ke element se alag value nhi de sakte hai  
Set2.remove ( 4 )

print ( Set2 )                     # O/p => {1, 2, 5}


----------------------------------------# 3. clear() #-----------------------------------------------#
# yeh clear karta hai set ko


Set3 = { 5, 10, 15, 20, 50 }

Set3.clear()

print ( Set3 )
print ( len ( Set3 ) )              # O/p => 0


-----------------------------------------# 4. pop() #------------------------------------------------# 
# removes a random value
# yeh set ko clear nhi karta hai, yeh ek value ko remove karta``


Set4 = { 5, 10, 15, 31, 20, 50 }

Set4.pop()
print ( Set4 )                       # O/p => {20, 5, 10, 31, 15}  " Yeh koi  bhi rendom value ko reove kar deta hai "


#-----------------------------------------# 5. union() #----------------------------------------------#
## yeh dono set ko combine karke print karta hai, lekin duplicate value ko


Set5 = {"i", "am", "janmesh", "thakur"}

Set6 = {"i", "am", "janmesh", "thakur", "python", "developer"}


print ( Set5.union ( Set6 ) )       # yeh "union" function dono Set ko combine karke print karta hai or duplicate value ko Ek hi baar print kart hai
# O/p => {'janmesh', 'python', 'i', 'am', 'thakur', 'developer'}


#----------------------------------------# 6.intersection() #-----------------------------------------#


print ( Set5.intersection ( Set6 ) )    # yeh "intersection" function  dono sets mai se common value ko hi print karta hai 
# O/p => {'janmesh', 'i', 'am', 'thakur'}
