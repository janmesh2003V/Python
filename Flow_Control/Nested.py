# ## Q=> Enter Age from user (if user is 18+ or below 80) user eligible for derive otherWise,
# ##  user is not eligible ? 
# ## By nested If else


A = int ( input ( "Enter your age :\n") )

if ( A >= 18 ) :

    if ( A > 79 ) :
        print ( "You can't derive your Age is 80+" )

    else :
        print ( "you are Eligible for Derive" )

    print ( "you are 18+" )     # yeh uper / Outside ki condition ke hisab se print hoga 


else :
    print ( "your Are not eligible, your age below 18 " )


#---------------------------------------------------------------------------------------------#

## WAP to find a greatest three(3) number entered by user


a = int ( input ( "Enter first number  :\n" ) )
b = int ( input ( "Enter second number :\n" ) )
c = int ( input ( "Enter third number  :\n" ) )

if ( ( a >= b ) and ( a >= c )):
    print ( "first number is big ", a )

elif ( b >= c ):
    print ( "second number is big ", b )

else : 
    print ( "third number is big ", c ) 

#----------------------------------------------------------#

## WAP to check if a number is a multiple of 7 or not.

user = int ( input ( "Enter number : \n" ) )

if ( user % 7 == 0 ): 
    print ( "yes this", user, "is multiple of 7 " )

else : 
    print ( "no " )
