import json

#open the file that contains the twitter stream
filename = 'output1.txt'
f = open(filename, "r")

#redirect ouput to output2.txt
f2 = open("output2.txt", "w")
sys.stdout = f2
def format_tweets():
    for line in f:
        try:
            #process/read each line of the text file and convert it to json
            #this only considers tweets with a text attribute
            tweet = json.loads(line.strip())
            if 'text' in tweet:
                #print data/content of text attribute
                print tweet['text'] 

        except:
            # in case an error occurs with reading the line
            continue
            
#function call and call to run wordcount.py           
format_tweets()        
f.close()
execfile('wordcount.py')


   