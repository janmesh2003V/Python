#---------------------------------------# break #------------------------------------------------#

### Break : used to terminate the loop when encountered.


# i = 1

# while i <= 5:
#     print( i )
#     if ( i == 3):
#         break               
#     i += 1

# print ("End of the loop ")


#---------------------------------------# continue #------------------------------------------------#

### Continue : terminates execution in the current iteration & continues execution of the loop with the next iteration.


i1 = 1
while i1 <= 10:
    
    if ( i1 %2 == 0):
        i1 += 1
        continue
    
    print( i1 )               
    i1 += 1

print ("End of the loop ")

