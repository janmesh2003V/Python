#----------------------------------------# Reverse String #------------------------------------------#


def Reverse ( a ):
    
    n = ""
    for i in range ( len (a)-1, -1 , -1 ):

        n = n + a [ i ]

        # n = print ( a [i], end="" )       # yeh direct print karane ke liye mtlb mai isho kko nhi "n" mai le kar print karunga
    
    return n
        


# print ( n )

a = str ( input ("\nEnter any word for revrese : ") )

print ( "\nthis is reverse of string :",Reverse(a) )


if ( Reverse ( a ) == a ):

    print ( "\nThe word is palindrome\n" )

else:
    
    print ( "\nThe word is not palindrome\n" )




# O/p => 👇


# Enter any word for reverse : janmesh thakur

# this is reverse of string : rukaht hsemnaj

# The word is not palindrome


# O/p => 👇


# Enter any word for revrse : madam

# this is reverse of string : madam

# The word is palindrome

