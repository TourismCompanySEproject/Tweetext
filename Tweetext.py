import os
import glob

#Feature Extraction
from Classifiers.feature_extraction import *

#Classifiers
from Classifiers.classifier_abc import Classifier


class Tweetext:
    # __raw_data_path = ''

    def __init__(self, auto = False):

        # if auto:
        #     train_set_no = 600
        #     test_set_no = 100
        #     self.doc, self.feat = self.process_data('Classifiers/Data/raw')
        #     self.train_set, self.test_set = self.feature_extraction(self.doc, self.feat, 600, 100)
        pass

    def train(self, algorithm = 'NaiveBayesAlgorithm'):

        __current_algorithm = Classifier.factory("NaiveBayesAlgorithm")
        print(__current_algorithm)

        # pass

    def get_accuracy(self):
        return __current_algorithm.get_accuracy()


    def predict(self, statment, algorithm = 'NB'):
        pass
