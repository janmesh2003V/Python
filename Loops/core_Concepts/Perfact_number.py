#---------------------------------------# perfact program #------------------------------------------#

a = int ( input ("Enter the number : ") )

c = 0 

for i in range ( 1 , a ):

    if ( a % i == 0 ):

        c += i

if c == a :
    print ("this is prefact number ")

else :
    print ("this is not prefact number ") 




# O/p => 👇

# Enter the number : 28
# this is prefact number 


# next O/p => 👇

# Enter the number : 25
# this is not prefact number   
