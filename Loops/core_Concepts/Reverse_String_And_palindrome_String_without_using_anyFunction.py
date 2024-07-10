#----------------------------------------# Reverse String #------------------------------------------#


def Reverse ( a ):
    
    n = ""
    for i in range ( len (a)-1, -1 , -1 ):

        n = n + a [ i ]

        # n = print ( a [i], end="" )       # yeh direct print karane ke liye mtlb mai isho kko nhi "n" mai le kar print karunga
    
    return n
        


# print ( n )

a = str ( input ("\nEnter any word for revrse : ") )

print ( "\nthis is reverse of string :",Reverse(a) )


if ( Reverse ( a ) == a ):

    print ( "\nThe word is palindrome\n" )

else:
    
    print ( "\nThe word is not palindrome\n" )

