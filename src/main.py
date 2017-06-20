import SentimentAnalysis
import data_reader

#Path to our datasets. 
data_path = '/home/rcorona/jsalt/lab2/data'

if __name__ == '__main__':
    #First read in our datasets. 
    training = data_reader.read_dataset(data_path + '/reviews10k.txt.train.train')
    dev = data_reader.read_dataset(data_path + '/reviews10k.txt.train.test')
    test = data_reader.read_dataset(data_path + '/reviews10k.txt.test')
