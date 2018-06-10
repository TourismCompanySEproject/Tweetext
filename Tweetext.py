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
    def __init__(self, algorithm = "NaiveBayes"):
        """
            Constructor, takes Algorithm type as parameter, and create it using the factory DP.
        :param algorithm(optional): The Classifier algorithm to be created.
        """
        self.__current_algorithm = Classifier.factory(algorithm= algorithm)
        print(self.__current_algorithm)
    #end __init__


    def train(self, raw_data_path =Raw_Data_Dir.__getattr__(),
              train_set_no=6000, test_set_no=100,):
        """

        :param raw_data_path(optional):
                The directory or location of the Raw data to clean and train.
        :param train_set_no: Number of features in training set.
        :param test_set_no: Number of features in testing set.
        :return: None.
        """

        self.__current_algorithm.train(
            raw_data_path,
            train_set_no, test_set_no,)
    #end train


    def get_accuracy(self):
        """
            Gets the accuracy of the currently used algorithm.
        :return: The currently used algorithm accuracy
        """
        return self.__current_algorithm.get_accuracy()
    #end get_accuracy


    def classify(self, statement):
        """
            Responsible for classifing the input string.
            calls the currently used algorithm predict function.
            and returns the result (label or category).
        :param statement: String to classify.
        :return: Label(category) of the statement.
        """
        return self.__current_algorithm.predict(statement)
    #end predict

    def __del__(self):
        """
            Destructor
        :return: None
        """
        pass