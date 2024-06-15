St = "Janmesh Thakur"
# St1 = St [8 : ]  
# print ( St1 )

print ( St [ : 7] )     # [0 : 7]         Or Ismai Range Inclucde nhi hoti
print ( St [8 : ] )     # [8 : len(St)]   Or Ismai Range Inclucde nhi hoti

#---------------------------------------------------------------------------------#

St2 = "APPLE"
print ( St2 [-3 : -1 ] )           # O/p => PL Ayega kyuki yeh Pichhe se Value ko lena Start karta hai
                                   # or Ismai bhi Range Include nhi hoti kyuki yeh Slice Functon hai
print ( St2 [-len(St2) : -1] )     # o/P => APPL

print ( St2 [-3 : ] )              # O/P => PLE
print ( St2 [ : -2])               # O/p => APP -2 ka mtlb hi yeh hai ki last ki 2 Charater ko chod kar 







