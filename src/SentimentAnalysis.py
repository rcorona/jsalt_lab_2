from nltk.sentiment import SentimentAnalyzer
from sklearn.linear_model import LogisticRegression

class SentimentAnalysis:
    #Initialize sentiment analyzer with a given model type. 
    def __init__(self, model): 
        if model == 'logistic_regression':
            self.model = LogisticRegression()

    def train(X,Y): 
        self.model.fit(X,Y)

    def test(X, Y): 
        predictions = self.model.predict(Y)
