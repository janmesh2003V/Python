#------------------------------# Tuple Methods #----------------------------------#

#------------------------------# 1. index (idx) #-------------------------------#


t1 = (1, 2, 4, 5, 6, 9)         

print ( t1.index ( 9 ) )            # returns index of first occurrence  t1.index( 9 ) is 5

t2 = ("janmesh", "thakur", "pan", "new", "ram", "pan", "pain")

# print ( t2.index ( "pan" ) )        # returns index of first occurrence  t1.index ( "pan" ) is 2


#-------------------------------# 2. count ( value ) #-----------------------------------#


t3 = ( 1, 2, 4, 5, 6, 9, 2, 2, 2, 9 )

# print ( t3.count (9) )              # t3.count()  #counts total occurrences  t3.count ( 9 ) is 2

# a3 = int ( input ("Enter search number ") )

# print ( t3.count ( a3 ), "times in tuples" )  # user se value le kar print kiya hai  


t4 = ("janmesh", "thakur", "pan", "new", "ram", "pan", "pain")

print ( t4.count ("pan") )
