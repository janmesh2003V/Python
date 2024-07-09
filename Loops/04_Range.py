
#-----------------------------------------# range() #-----------------------------------------------#


## Range functions returns a sequence of numbers, starting from 0 by default, and increments by
## 1 (by default), and stops before a specified number.

range( start?, stop, step?) ## Where, ? Show that it is optional


for i in range ( 5 ):             # first way to print, using "range" function
    print ( i )


for i2 in range ( 3, 9 ):         # Second Way to print, using "range" function  
    print ( i2 )


for i3 in range ( 3, 10 , 3 ):    # third and best way to print, using "range" function
    print ( i3 )


#---------------------------------------------------------------------------------------------------#
## print Odd number 1 to 20 using " range " 


# range( start?, stop, step? )
for i4 in range ( 1, 20, 2 ):
    print ( i4 )


#---------------------------------------------------------------------------------------------------#
## print Even number 1 to 20 using " range " function


# range( start?, stop, step? )
for i5 in range (2, 21, 2 ):
    print ( i5 )


#---------------------------------------------------------------------------------------------------#
## practice 


for i6 in range ( 1000, 200, -1 ):
    print ( i6 )


#---------------------------------------------------------------------------------------------------#
## Print the multiplication table of a number n.


a = int ( input ("Enter number for table : ") )
c = 1
for i7 in range ( a, a*11, a ):

    print ( a, " * ", c, " = ", i7 )

    c += 1


# O/p => 👇
# Enter number for table : 5
# 5  *  1  =  5
# 5  *  2  =  10
# 5  *  3  =  15
# 5  *  4  =  20
# 5  *  5  =  25
# 5  *  6  =  30
# 5  *  7  =  35
# 5  *  8  =  40
# 5  *  9  =  45
# 5  *  10  =  50


#---------------------------------------------------------------------------------------------------#
# WAP to find the sum of first n numbers. (using while)


a1 = int ( input ("Enter number : ") )

i8 = 0
sum = 0
while ( i8 <= a1 ):
    sum += i8
    i8 += 1

print ( a1, "number tak ka sum : ", sum  )


#---------------------------------------------------------------------------------------------------#
# WAP to find the factorial of first n numbers. (using for)


a3 = int ( input ( "Enter number : ") )

i9 = 1
fact = 1

for i9 in range (1, a3+1, 1):
    fact *= i9

print ( a3, "ka factorial : ", fact )
