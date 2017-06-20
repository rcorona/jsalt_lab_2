import SentimentAnalysis
import data_reader

#Path to our datasets. 
data_path = '/home/rcorona/jsalt/lab2/data'

if __name__ == '__main__':
    #First read in our datasets.
    print('Reading in data...')
    train_x, train_y = data_reader.read_dataset(data_path + '/reviews10k.txt.train.train')
    #dev = data_reader.read_dataset(data_path + '/reviews10k.txt.train.test')
    test_x, test_y = data_reader.read_dataset(data_path + '/reviews10k.txt.test')

    #Instantiate and train a model.
    print('Training...')
    analyzer = SentimentAnalysis('linear_regression')
    analyzer.fit(train_x, train_y) 
