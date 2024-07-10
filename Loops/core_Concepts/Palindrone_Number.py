#--------------------------------# Palindrome number check program #---------------------------------#


def palindrome ( a ):
   
    m = a 
    sum = 0


    for i in range ( 1, a + 1 ):

        if a > 0 :

            n = a % 10

            sum = sum * ( 10 ) + n 

            a = a // 10

    print ("\nReverse of given number is :", sum )


    if ( sum == m ):
        print ( "\nThe number is palindrome\n" )

    else:
        print ( "\nThe number is not palindrome\n" )


a = int ( input ("\nEnter the number : ") )


palindrome ( a )




# O/p => 👇


# Enter the number : 1221 

# Reverse of given number is : 1221

# The number is palindrome


# O/p => 👇


# Enter the number : 146

# Reverse of given number is : 641

# The number is not palindrome    
