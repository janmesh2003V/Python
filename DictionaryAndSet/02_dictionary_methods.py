#----------------------------------# 1. keys() #--------------------------------------------#

dict = {
    "name" : "rahul",
    "age" : 20,
    "city" : "delhi",
    "id" : 111
}

## yeh keys batata hai dictionary ki
print ( len ( dict ) )              # O/p  => 4

print ( dict.keys () )              # O/p  => dict_keys(['name', 'age', 'city', 'id'])

print ( list ( dict.keys () ) )     # O/p  => ['name', 'age', 'city', 'id']  "list" lagane se yeh sab list ke form mai aa jayenge


#-----------------------------------# 2. values() #-------------------------------------------#
## yeh value batata hai dictonary ki


print ( dict.values() )             # O/p  => dict_values(['rahul', 20, 'delhi', 111])

print ( list ( dict.values() ) )    # O/p  => ['rahul', 20, 'delhi', 111] 


#-----------------------------------# 3.items() #-------------------------------------------#
## yeh function key - value ko print karta hai 


print (  dict.items() )             # O/p  => dict_items([('name', 'rahul'), ('age', 20), ('city', 'delhi'), ('id', 111)])

print ( list ( dict.items() ) )     # O/p  =>[('name', 'rahul'), ('age', 20), ('city', 'delhi'), ('id', 111)]


#-----------------------------------# 4.get("key") #-----------------------------------------#


print ( dict ["name2"] )           # yeh " error de dega " pr aError ke baad aage ka code bhi Exceute nhi hoga 

print ( dict.get ("name2") )       # or yeh "none" show kar dega pr error hi dega isse ky ahog aki aage ka code continue chalega 


#----------------------------------# 5. update(new key pair ) #---------------------------------#

# yeh dictionary mai new key pair add karta hai
dict2 = {
    "class" : "full",
    "roll" : 1,
    
}

dict.update( dict2 )             # yeh dictionary mai new key pair add karta hai
print ( dict )                   # O/p => {'name': 'rahul', 'age': 20, 'city': 'delhi', 'id': 111, 'class': 'full', 'roll': 1}

# update ka dusra tarika 

dict2.update( { "bhai" : "shivam" } )

print ( dict2 )                    # O/p => {'class': 'full', 'roll': 1, 'bhai': 'shivam'}

