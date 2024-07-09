#-------------------------------# Audio to Speech #-------------------------------#


import pyttsx3

engine = pyttsx3.init()

ans = input ("What you want to speech please tell me : ")


# Rate

rate = engine.getProperty ('rate')          # getting details of current speaking rate

print ( rate )                              # printing current voice rate

engine.setProperty ('rate', 120 ) 


# Volume 

volume = engine.getProperty('volume')       # getting to know current volume level (min=0 and max=1)

print ( volume )                            # printing current volume level

engine.setProperty('volume', 1.0) 


# voice

voices = engine.getProperty('voices')        # getting details of current voice

engine.setProperty('voice', voices [0] .id ) # changing index, changes voices. 0 for male

engine.setProperty('voice', voices [1] .id )  
#
engine.say( ans )

engine.runAndWait()

engine.stop()
 

# "Saving Voice to a file" 

# We can use file extension as mp3 and wav, both will work
engine.save_to_file( ans , 'speech1.mp3')
 
# Wait until above command is not finished.
engine.runAndWait()

