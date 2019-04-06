#=========================================#
#          py_bot 3.0 - interface         #
#           @author Ben Correll           #
#             Github: bcorrel2            #
#=========================================#

import py_bot, os, time
from py_bot import reciprocalFollow
from py_bot import indefiniteCycle
from py_bot import createTweet
from py_bot import definiteCycle
from py_bot import fullCycle
from py_bot import addTweet
from py_bot import followUser
from py_bot import unfollowUser

def clearScreen():
    # clears screen
    
        os.system('cls' if os.name == 'nt' else 'clear')
    
def printHeader(ver_no):
    # prints header
    # @param ver_no: String containing version number
    
        print "======== py_bot v" + ver_no + " ========"
        
def printNavError():
    # prints navigation error
    
    print "Error: Not a Valid Selection"

def refreshScreen(ver_no):
    # clears and refreshes screen
    # @param ver_no: String containing version number
    
        #clearScreen()
        printHeader(ver_no)
        print

def quitMessage():
    # Prints exit message upon quitting
    
    print "--Exiting py_bot--"
    
ver_no = "3.0"

#clearScreen()

printHeader(ver_no)
print "Warning: user assumes responsibility" 
print "for use of this program, and any consequences" 
print "resulting therein, including but not limited" 
print "to suspension or deletion of account," 
print "and/or legal action"
print "============================="
print
print "Please Select Operation Mode:"
print "(1) Manual"
print "(2) Automatic"
print "(3) Quit"

user_selection = input(":")

while(user_selection > 3):
    printNavError()
    user_selection = input(":")

if(user_selection == 1): # Manual
    
    while(1):
        
        refreshScreen(ver_no)
        
        print "Please Select Function:"
        print "(1) Post"
        print "(2) Follow"
        print "(3) Unfollow"
        print "(4) Reciprocate Following"
        print "(5) Quit"
        user_selection = input(":")
        
        while(user_selection > 5):
            printNavError()
            user_selection = input(":")
    
        if(user_selection == 1): # Manual -> Post
            refreshScreen(ver_no)
            createTweet()
            
        elif(user_selection == 2): # Manual -> Follow
            refreshScreen(ver_no)
            followUser()
            
        elif(user_selection == 3): # Manual -> Unfollow
            refreshScreen(ver_no)
            unfollowUser()
        
        elif(user_selection == 4): # Manual -> Reciprocal Follow 
            refreshScreen(ver_no)
            reciprocalFollow()
            
        elif(user_selection == 5): # Manual -> Quit
            quitMessage()   
            break
    
        else:
            printNavError()
            
        time.sleep(3)
    
elif(user_selection == 2): # Automatic
    
    while(1):
        
        refreshScreen(ver_no)
        
        print "Please Select Parameters:"
        print "(1) Limited Run"
        print "(2) Indefinite Run"
        print "(3) Full Run"
        print "(4) Add New Tweet"
        print "(5) Quit"
        user_selection = input(":")
        
        while(user_selection > 5):
            printNavError()
            user_selection = input(":")
    
        if(user_selection == 1): # Automatic -> Limited Run
            refreshScreen(ver_no)
            spacing = input("Define Spacing Between Tweets (in seconds): ")
            print
            runtime = input("Define Total Run Time (in seconds): ")
            print
            definiteCycle(spacing, runtime)
        
        elif(user_selection == 2): # Automatic -> Indefinite Run
            refreshScreen(ver_no)
            spacing = input("Define Spacing Between Tweets (in seconds): ")
            print
            indefiniteCycle(spacing)
            
        elif(user_selection == 3): # Automatic -> Full Run
            spacing = input("Define Spacing Between Tweets (in seconds): ")
            print
            fullCycle(spacing)
            
        elif(user_selection == 4): # Automatic -> Add New Tweet
            refreshScreen(ver_no)
            addTweet()
        
        elif(user_selection == 5): # Automatic -> Quit
            quitMessage()
            break   
    
        else:
            printNavError()
            
        time.sleep(3)
            
elif(user_selection == 3): # Quit
    quitMessage()

else:
    printNavError()
    