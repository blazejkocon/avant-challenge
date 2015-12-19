import re
import operator
from collections import OrderedDict

#reset the ouput to the console
sys.stdout = sys.__stdout__

#list of stop words (not comprehensive but for the purpose of this assignment it will suffice)
stopwords = ['the', 'that', 'to', 'as', 'there', 'has', 'and', 'or', 'is', 'not', 'a', 'of', 'but', 'in', 'by', 'on', 'are', 'it', 'if','me','i','you','rt','my','at','this','thats','that\'s','my','his','hers','what','where','who','why','all','its','it\'s','im','dont','youre','cant','no']

#ope the file containing the extracted text from the twitter stream
filename = 'output2.txt'
f = open(filename, "r+")

def count_words():
    wordcount={}
    for word in f.read().split():
        word=word.lower()
        #the following regular expressions filter out anything that is not a word by removing any special characters, urls, and numbers.
        word = re.sub(r'^https?:\/\/.*[\r\n]*', '', word, flags=re.MULTILINE)
        word= re.sub('/[^a-zA-Z0-9\s]/gi','', word)
        word= re.sub('^((?!_)[A-Za-z0-9])+$','', word)
        word=re.sub("[\W\d]", "", word.strip())
        word=re.sub("[\W_]+", "", word)
        #check to see whether the word is a stopword of an empty string otherwise increase the count value
        if word not in stopwords and word != '':
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
            
    #reverse the dictionary to display it in descending order and display the 10 most frequent words          
    wordcount = OrderedDict(sorted(wordcount.items(),key=operator.itemgetter(1), reverse=True)[:10])
    #print each key and value from the dictionary(i.e. the word and it's count)
    for k,v in wordcount.items():
        print k, v
        
#function call        
count_words()
f.close()
    