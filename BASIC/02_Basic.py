n = 2
m = 3
# Strr = "@"
Strr2 = "A"

# print(n*m*Strr)     #ISka O/p = @@@@@@ yeh Ayega 
# print(n*m*Strr2)    #ISka O/p = AAAAAA yeh Ayega 

# print ( (n+Strr2) * m)      # Yeh Error Dega = TypeError: unsupported operand type(s) for +: 'int' and 'str'

## But, 
k = "2"

# print ( (k+Strr2) * m )    #Iska O/p = 2A2A2A yeh Ayega 

#----------------------------------#

###************************ (a//b) is Same As Floor (a/b) ******************************###


a = 12
b = 5
c = a//b
# print ( c )  # Iska O/p = 2 Ayega, kyuki 12/5 = 2.4 but yeh 2.4 ko floor mai karke dega  like " 2 "

## Again,

A = -12
B = 5
# print (A//B) # Iska O/p = -3 Ayega, kyuki -12/5 = -2.4 but yeh -2.4 ko floor mai arke Dega like " -3 " 


#--------------------------------------#

## denominator   :  -    +   +    - 
## numerator     :  +    -   +    -
## Result(A % B) :  +    -   +    +
A1 = 5
B1 = 2
print ( A1 % B1 )  ## +ve Output

A2 = -5
B2 = 2
print ( A2 % B2 ) ## Iska bhi +ve Output

#where,

A3 = 5
B3 = -2
print ( A3 % B3 ) ## Iska O/p = -1, -ve Value mai Ayega " kyuki Denominator -ve Hai "



