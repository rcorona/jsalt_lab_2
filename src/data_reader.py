import sys
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
import numpy as np

def extract_features(text): 
    #First tokenize text into sentences. 
    sentences = sent_tokenize(text)
    
    #Average polarity scores over sentences.
    analyzer = SentimentIntensityAnalyzer()

    neg = np.zeros(shape=(len(sentences),))
    neu = np.zeros(shape=(len(sentences),))
    pos = np.zeros(shape=(len(sentences),))
    compound = np.zeros(shape=(len(sentences),))

    for i in range(len(sentences)):
        sent = sentences[i]

        polarity_scores = analyzer.polarity_scores(sent)
        
        #Add each type of score from sentence.
        neg[i] = polarity_scores['neg']
        neu[i] = polarity_scores['neu']
        pos[i] = polarity_scores['pos']
        compound[i] = polarity_scores['compound']

    #Now compute the mean of each type of score and return as feature vector. 
    avg_neg = np.mean(neg)
    avg_neu = np.mean(neu)
    avg_pos = np.mean(pos)
    avg_compound = np.mean(compound)

    return np.array([avg_neg, avg_neu, avg_pos, avg_compound])

def read_dataset(file_name):
    #First open the file for reading. 
    data_file = open(file_name, 'r')

    #Will hold dataset. 
    X = []
    Y = []

    #Each line is a separate datapoint. 
    for line in data_file: 
        x, y = read_line(line)                

        X.append(x)
        Y.append(y)

    #Now make into numpy arrays. 
    X = np.array(X)
    Y = np.array(Y)

    return (X, Y)

def read_line(line): 
    #First separate all data fields. 
    data = line.split()[7:]

    review_score = float(data[0])
    text = ' '.join(data[1:])

    #Process text into feature vector. 
    features = extract_features(text)

    #Now return tuple of score and text. 
    return (features, review_score)
