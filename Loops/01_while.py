##--------------------------------------# Loops in Python #----------------------------------------##
# Loops are used to repeat instructions.


count = 1

while count <= 5:
    
    print(count)
    count += 1

# reverse 1 to 5

i = 5

while i >= 1:

    # print( i )
    i -= 1


#---------------------------------------------------------------------------------------------------#


#-----------------------------# Practice Question using while loop #-----------------------------#
## Print numbers from 1 to 100.
 
i1 = 1 

while i1 <= 100:
    # print(i1)
    i1 += 1


#----------------------------------------------------------------------------------------------------#
## Print numbers from 100 to 1.


i2 = 100

while i2 >= 1:
    # print( i2 )
    i2 -= 1


----------------------------------------------------------------------------------------------------#
## Print the multiplication table of a number n.


user = int ( input ("Enter nuber for table : ") )

i3 = 1
while i3 <= 10:
    x = user * i3
    # print( x )
    i3 += 1


----------------------------------------------------------------------------------------------------#
## Print the elements of the following list using a loop:
## [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


num1 = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]

i4 = 0

while ( i < len ( num1 ) ):
    print( num1[i] )
    i += 1


----------------------------------------------------------------------------------------------------#
## Search for a number x in this tuple using loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


X = int ( input ("Enter number, which one want to find in tuple : ") )
num2 = ( 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 )

print ( num2 )

i5 = 0

c = False

while ( i5 < len ( num2 ) ):

    if( num2 [ i5 ] ==  X ):

        print ("yes", num2 [ i5 ], "present in tuple" )

        c = True

    i5 += 1

if ( c == False ):

    print ("no", X, "not present in tuple" )
