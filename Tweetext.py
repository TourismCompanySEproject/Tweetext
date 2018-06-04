import os
import glob

#Feature Extraction
from Classifiers.feature_extraction import *

#Classifiers
from Classifiers.classifier_abc import Classifier
from Classifiers.nb_algorithm import NaiveBayesAlgorithm


class Tweetext:
    # __raw_data_path = ''
    __accuracy = 0.0
    __current_algorithm = ''

    def __init__(self, auto = False):
        if auto:
            train_set_no = 600
            test_set_no = 100
            self.doc, self.feat = self.process_data('Classifiers/Data/raw')
            self.train_set, self.test_set = self.feature_extraction(self.doc, self.feat, 600, 100)


    def process_data(self,  path = None, url = None):
        """
        :param path: directory of the raw data to be processed
        :param url: an online directory of the raw data to be processed,
                @edit still not working.
        :return: processed: the features and words after being processed,
        removing the stopwords, symbols, emoticons, and any unnecessary word.
        """
        if path is None:
            if url is None:
                return "No directory or url specified"

        elif path:
            __raw_data_path = path
            os.chdir(__raw_data_path)

            raw_txt_files = glob.glob("*.txt")
            raw_csv_files = glob.glob("*.csv")
            raw_json_files = glob.glob("*.json")

        elif url:
            pass

        processsed= clean_data(raw_txt_files, raw_csv_files, raw_json_files)

        return processsed
    #end process_data

    def feature_extraction(self, documents, word_features, train_set_no, test_set_no):
        """

        :param documents:
        :param word_features:
        :param train_set_no:
        :param test_set_no:
        :return: train_set: dictionary of labled features for training the system.
                 test_set:  dictionary of labled features for testing the system.
        """
        print(1)
        featuresets = [(extract_features(doc, word_features), c) for (doc, c) in documents]
        print(2)
        train_set, test_set = featuresets[train_set_no:], featuresets[:test_set_no]
        print("Train set length", len(train_set),"Test set length", len(test_set))
        return train_set, test_set
    #end feature_extraction


    def train(self, algorithm = 'NaiveBayesAlgorithm'):
        global __current_algorithm
        __current_algorithm = Classifier.factory("NaiveBayesAlgorithm")
        # print(__current_algorithm)



        # pass


    def get_accuracy(self):
        return __current_algorithm.get_accuracy()


    def predict(self, statment, algorithm = 'NB'):
        pass
