import os
import glob
#Feature Extraction
from Classifiers.feature_extraction import *
#Classifiers
from Classifiers.classifier_abc import Classifier
#Directions
from Classifiers.Directions import Raw_Data_Dir


class Tweetext:
    """
        Tweetext: acts as the interface between the users and the system functionalities
    """
    def __init__(self, algorithm = 'NaiveBayesAlgorithm'):
        """
            Constructor, takes Algorithm type as parameter, and create it using the factory DP.
        :param algorithm: The Classifier algorithm to be created.
        """

        self.__current_algorithm = Classifier.factory(algorithm)

    #end __init__


    def train(self, raw_data_path =Raw_Data_Dir.__getattr__(),
              train_set_no=6000, test_set_no=100,):
        """

        :param raw_data_path:
        :param raw_data_url:
        :param train_set_no:
        :param test_set_no:
        :return:
        """

        self.__current_algorithm.train(
            raw_data_path,
            train_set_no, test_set_no,)
    #end train


    def get_accuracy(self):
        return self.__current_algorithm.get_accuracy()
    #end get_accuracy


    def classify(self, statement, algorithm = 'NB'):
        return self.__current_algorithm.predict(statement)
    #end predict

