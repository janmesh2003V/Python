## Print the elements of the following list using a loop:
## [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]


num1 = [ 1, 4 ,9, 16, 25, 36, 49, 64, 81, 100 ] 

for i in num1:
    print ( i )


#---------------------------------------------------------------------------------------------------#
## Search for a number x in this tuple using loop:
## [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


num2 = ( 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 )

for i1 in num2:
    print ( i1 )


#---------------------------------------------------------------------------------------------------#
# Search for a number x in this tuple using loop:
# [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]


X = int ( input ("Enter number, which one want to find in tuple : "))

num3 = ( 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 )
c = False

for i3 in num3:
    if ( i3  == X ):
        print ( "Number is found in tuple" )
        c = True
        break

if ( c == False ):
    print ( "Number is not found in tuple" )


