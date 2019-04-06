#=========================================#
#               py_bot 3.0                #
#           @author Ben Correll           #
#             Github: bcorrel2            #
#=========================================#

import time, tweepy, random, string

#--------------Access Keys----------------#

consumer_key = 'SgPN7R5Ili5c5Cvk37bmwfADB'
consumer_secret = 'Ben9qS5eyHd7H10JyrQZJ57pxUI8lXD1ifHXqsPpww7wXsu38o'
token_key = '852938638803566592-6FV88lDJwOVbXveYgnaCUVx4pi4Vmdj'
token_secret = 'e7kS3dsZiOX77Opb4lxqQ3cNz98cx0CS0c5LUzsyDHqPL'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token_key, token_secret)
account = tweepy.API(auth)

#---------------Functions-----------------#

def checkTweet(tweet):
    # Function for checking tweet validity
    # @param tweet: String containing tweet
    # @return True if valid, False if not

        if(len(tweet) > 280):
                return False

        else:
                return True

def logTweet(time_stamp):
    # Function for logging tweet post times
    # @param time_stamp: String containing time tweet was posted
    
    with open('log.txt', 'a') as log:
        log.write(time_stamp + '\n')

def postTweet(tweet):
    # Function for posting to Twitter
    # @param tweet: String containing tweet

        time_stamp = "" 

        valid = checkTweet(tweet) # Check if tweet is <280 characters

        if(valid == False):
                print '-ERROR- Invalid Tweet'

        else:

                print '-PREPARING-'
                
                try:
                        account.update_status(tweet) # Post to Twitter
                        time_stamp = time.asctime(time.localtime(time.time()))

                except tweepy.TweepError: # Twitter returns error
                        print '-ERROR- TweepError'
                        return

                logTweet(time_stamp)
                print time_stamp

                print '-POSTED-'
                print #blank line
                
def createTweet():
    # Function to write a new Tweet - used for manual posting
    
    print 'Enter Your Tweet ("..."):'
    
    try:
        tweet = input("Tweet: ")
        postTweet(tweet)
        
    except SyntaxError: 
        print "-Error- quotation marks are required"
        print
        
    except NameError:
        print "-Error- quotation marks are required"
        print
   
def addTweet():
    # Function for adding tweet to tweets.txt
    
    print 'Enter Your Tweet ("..."):'
    
    try:
        tweet = input("Tweet: ")
        with open('tweets.txt', 'a') as tweet_file:
            tweet_file.write('\n' + tweet + '\n')
        
    except SyntaxError: 
        print "-Error- quotation marks are required"
        print
        
    except NameError: 
        print "-Error- quotation marks are required"
        print
                
def getRandomTweet(last_tweet, length):
    # Function for determining which tweet should be posted - randomly
    # @param last_tweet: Integer holding line no. of the previous tweet
    # @param length: Integer holding length of tweets.txt
    # @return line no. of selected tweet
    
        line_no = random.randrange(0,length)
        
        if(line_no % 2 != 0): # Avoid empty lines
            line_no += 1
            
        if(line_no == last_tweet): # Get new line
            line_no = getRandomTweet(last_tweet, length) 
            
        return line_no
                       
def getInlineTweet (last_tweet, length):
    # Function for determining which Tweet should be posted - in order
    # @param last_tweet: Integer holding line no. of the previous tweet
    # @param length: Integer holding length of tweets.txt
    # @return line no. of next tweet
        
        if(last_tweet + 1 < length): # return next tweet
            return last_tweet + 1

        else: # all tweets have been posted
            return -2        
            
def followUser():
    # Function for following a specified user 
    
        try:
            username = input('User to be Followed ("..."): ')
            account.create_friendship(username) 
        
        except SyntaxError: 
            print "-Error- quotation marks are required"
            print
        
        except NameError: 
            print "-Error- quotation marks are required"
            print
            
def unfollowUser():
    # Function for following a specified user 
    
        try:
            username = input('User to be Unfollowed ("..."): ')
            account.destroy_friendship(username) 
        
        except SyntaxError: 
            print "-Error- quotation marks are required"
            print
        
        except NameError: 
            print "-Error- quotation marks are required"
            print
            
def reciprocalFollow():
    # Follows every user that has followed the account

        for follower in tweepy.Cursor(account.followers).items():
                follower.follow() 
        print "All Followers Have Been Followed"              
                    
def indefiniteCycle(spacing):
    #Function continues posting tweets indefinitely
    # @param spacing: Integer dictating the spacing (in seconds) between tweets
    
    lastline = -1 # holds the last line number posted

    while(1): # infinite loop
        tweet_file = open('tweets.txt', 'r') # read file
        lines = tweet_file.readlines()
        tweet_file.close()

        length = len(lines) # number of lines in file

        lastline = getRandomTweet(lastline, length)

        if( checkTweet(lines[lastline]) == False ): # identify problem tweets
            print '-Error- bad tweet'
            print # blank line
           
        else:
            
            postTweet(lines[lastline])
        
            time.sleep(spacing) # sleeps specified time 

def definiteCycle(spacing, runtime):
    #Function continues posting tweets for a set period of time
    # @param spacing: Integer dictating the spacing (in seconds) between tweets
    # @param runtime: Integer dictating total runtime (in seconds)
    
    lastline = -1 # holds the last line number posted
    
    cycles = runtime / spacing # determines how many tweet cycles can be run in alloted time
    
    for idx in range(cycles):
        
        if(idx >= cycles): 
            break
        
        tweet_file = open('tweets.txt', 'r') # read file
        lines = tweet_file.readlines()
        tweet_file.close()

        length = len(lines) # number of lines in file

        lastline = getRandomTweet(lastline, length)

        if( checkTweet(lines[lastline]) == False ): # identify problem tweets
            print '-Error- bad tweet'
            print # blank line
           
        else:
            
            postTweet(lines[lastline])
        
            time.sleep(spacing) # sleeps specified time 
    
def fullCycle(spacing):
    # Function continues posting tweets in-line until tweets.txt is exhausted 
    # @param spacing: Integer dictating the spacing (in seconds) between tweets
    
    lastline = -1 # holds the last line number posted

    while(1): 
        tweet_file = open('tweets.txt', 'r') # read file
        lines = tweet_file.readlines()
        tweet_file.close()

        length = len(lines) # number of lines in file

        lastline = getInlineTweet(lastline, length)

        if(lastline == -1):
            print "-- Full Cycle Completed --"
            break

        if( checkTweet(lines[lastline]) == False ): # identify problem tweets
            print '-Error- bad tweet'
            print # blank line
           
        else:
            
            postTweet(lines[lastline])
        
            time.sleep(spacing) # sleeps specified time
            
