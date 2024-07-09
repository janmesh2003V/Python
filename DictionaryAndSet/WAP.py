### Store following word meanings in a python dictionary :

# table : "a piece of furniture”, “list of facts & figures”
# cat : “a small animal”


Dict1 = {

    "table" :[ "a piece of furniture", "list of  facts & figures" ],
    "cat" :[ "a small animal" ]

}


# print ( Dict1 )


#---------------------------------------------------------------------------------------------------#


### You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students
# “python”, “java”, "C++”, "python”, “javascript”,
# "java", “python", "java", “C++, "C”


Set1 = { "python", "java", "C++", "Python", "javaScript", "java", "Python", "java", "C++", "C" }

# print ( len ( Set1 ), "classrooms are needed by all students" )


#---------------------------------------------------------------------------------------------------#


# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

dict1 = {}


name1 = int ( input ("hindi : " ) )
name2 = int ( input ("English : " ) )
name3 = int ( input ("Maths: " ) )

dict1.update ( {"hindi" : name1} )
dict1.update ( {"English" : name2} )
dict1.update ( {"Maths" : name3} )

print ( dict1 )



