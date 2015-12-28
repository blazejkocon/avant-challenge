import json
import time
import sys
# these are the methods from the Twitter library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream


#redirect output to output1.txt for further use
f = open("output1.txt", "w")
sys.stdout = f

# credentials needed to access Twtter API
api_key = 'dR0CZSWGwx7fr0TLio3KngqOh'
api_secret= 'stQ81o8GFI1zJGNqM6oXpfK6KvA5j5j02GVf4DHoIyKc2VvsrQ'
access_token = '4497468509-FnQaUolHJT9iVbcP2BPkzae1pmFBJF1HXoX3wQt'
access_token_secret = 'JDvVtWmfmwapGegLRmNaypYlFlfUY9LW5YDqw9bBHpl8x'


# connect to the streaming API using the credentials
twitter_stream = TwitterStream(auth=OAuth(access_token, access_token_secret, api_key, api_secret))

#get a sample of twitter statuses
iterator = twitter_stream.statuses.sample()

#the stream is set to end after 5 minutes
end = time.time() + 60*5

# this loop prints out each tweet in the stream
for tweet in iterator:
    
    # we convert each TwitterDictResponse object back to the JSON format for printing
    print json.dumps(tweet) 
    #check to see whether the specified minutes has passed
    if time.time()>=end:
        break
        
f.close()
#run formatter.py to format the twitter stream
execfile('formatter.py')
        
        
