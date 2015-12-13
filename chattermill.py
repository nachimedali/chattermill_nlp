########################################
###         Chattermill.io           ###
###   Name : Mohamed Ali Nachi       ###
###   mail : nachi.med.ali@gmail.com ###
###   Date : 05/12/2015              ###
########################################

import os
import re
import numpy 
from gensim.models import Word2Vec
from sklearn.ensemble import RandomForestClassifier

import pandas 

# In a comment, this function returns average of the word vector 
def mkFeatureVec(words, model, num):

    # Defining our array
    Vectorfeature = numpy.zeros((num,),dtype="float32")
    
    nb_words = 0.
    
    index2word_set = set(model.index2word)

    # Search for each word in a comment, and add its feature vector if it is in the model 
    for w in words:
        if w in index2word_set:
            nb_words = nb_words + 1.
            Vectorfeature = numpy.add(Vectorfeature, model[w])
    #
    # Calculating the average
    Vectorfeature = numpy.divide(Vectorfeature,nb_words)
    return Vectorfeature

# with a list of comments, return the average feature and return an array

def getAvgFeatureVecs(comments, model, nbr ):
    
    i = 0.
    
    #Defining the array with numpy
    commFeatureVecs = numpy.zeros((len(comments),nbr ),dtype="float32")

    # Browsing comments
    for com in comments:
    	# Calculate different average of word vector with the mkFeatureVec defined
    	commFeatureVecs[i] = mkFeatureVec(com, model, nbr )
    	i = i + 1.
    return commFeatureVecs

#Defining function that generates cleaned sentences from the original text. It converts a comment into a 
#formatted string ready for training.


def clean_comments(comments):
    
    #delete numbers
	only_alphabet = re.sub("[^a-zA-Z]", " ", comments)

	#convert this string to words in lower
	words = only_alphabet.lower().split()

	# After cleaning our string, we can return the "cleaned" one
	return (" ".join(words))


if __name__ == '__main__':

    #This list would contain all lines cleaned from stopwords with lower letters and formed to train.
    test =""
    clean_train_comment = []
	#This list initiated would contain 
    clean_test_comment = []

	#As we are using txt files with a huge size, instead of operating in all the file, we can process line by line. This would let us gain in time processing.
    
    with open(os.path.join(os.path.dirname(__file__), 'negative_reviews.txt')) as fileobject:
    #We proceed here by every line in the file, because our data contains, in each line a comment, so this would let us 
    #extract comment without defining delimiter
        
        for line in fileobject: 
      
        # We call our "clean_string" function for every string and we append, each one, to our clean_train_comment list
        # Something cool about data provided is that there is no punctuation, so this list contains comments already ready for
        #word2vec deep learning 
        
            clean_train_comment.append(clean_comments(line).split())

    # And we proceed with the same approach with the positive files
    #print clean_train_comment

    with open(os.path.join(os.path.dirname(__file__), 'test.txt')) as fileobject:
        for line in fileobject:	
            clean_test_comment.append(clean_comments(line).split())

    print clean_test_comment[0]
    # # Initiation of Word2Vec
    # Defining the model requires at the same time defininf 5 parameters:
    # workers reflects to how many threads should run in parallel, it is suggested to 4 threads
    # size defines the dimentiality of the word vector
    # min_count defines words that should be retained basingon the nbr of their repetition
    # window defines the context window size 
    # sample defines the setting for frequent word 
    model = Word2Vec(clean_train_comment, workers=4, size= 400, min_count = 1, window = 10, sample = 1e-3, seed=1)

    #having the model trained, we call now the init_sims funtion
    model.init_sims(replace=True)

    #Svaing Model
    model_name = "Chattermill_test"
    model.save(model_name)

    ############        Ruunning some tests with the model ########################
    
    a = model.most_similar("bikini")
    print a 
		
    trainVecs = getAvgFeatureVecs( clean_train_comment, model, 400 )

    testVecs = getAvgFeatureVecs( clean_test_comment, model, 400 )


	# Using scikit-learn forest classifier
    z =[]
    for i in xrange(0,1224):
        z.append('-1')
    for i in xrange(1224,3070):
        z.append('1')	

    forest = RandomForestClassifier( n_estimators = 100 )
    forest = forest.fit( trainVecs, z )

    # Generating results
    result = forest.predict( testVecs )
    for r in result:
        if r == '1':
            print "positive comment"
        else:
            print "negative comment"
    # Write the test results

    # output = pandas.DataFrame( data={"sentiment":result} )
    # output.to_csv( "Supervised.csv", index=False, quoting=3 )
    # print "The test is done and I hope to be accepted."
