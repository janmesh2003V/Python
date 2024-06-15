# S1 = "hello "
# S2 = "Sir "
# S3 = "my name is "
# S4 = "janmesh"

# print( S1 + S2 + S3 + S4 )


S6 = "hello Sir, \nmy name is janmesh"      # \n for line change 

S7 = "hello Sir, \tmy name is janmesh"      # \t for tab space 


# print ( S6 )

# print ( S7 )

#--------------------------------------------------------------------------------------#

C = 0
S8 = "hello Sir my name is janmesh"
for i in range (len(S8)):
    if ( S8[i] == " " ):
        continue
    C+=1
print( C )
print ("iss O/p mai Space bhi include hai tho, \nwo bhi cout hui hai ", len(S8) )
print ( "\nOr yeh Space Hai Baki ki" ,len (S8) - C )

#---------------------------------------------------------------------------------------#

S9 = "Janmesh Thakur"
print ( S9[2] )

#---------------------------------------------------------#

S10 = "i am janmesh thakur"
S11 = S10.endswith ("ur")    # yeh "endswith("ur")" yeh function check karta hai ki String ki end mai yeh laga hai ki nhi 

print ( S11 )

S12 = S10.capitalize ()      # yeh "capitalizer" yeh function String ke Only first letter ko Capital kar deta hai   

print ( S12 )

print ( S10.replace ("a", "i") ) # Yeh "replace ( old, new )" yeh Function "old" value ko "new" Value se replace kar deta hai 
                                 # O/p => "i im jinmesh thikur" Esa Output Ayega "a" ko "i" se replace kar diya 


