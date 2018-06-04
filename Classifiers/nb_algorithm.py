import nltk
import re, pickle, os

# Abstract Class
from abc import abstractmethod
# from .classifier_abc import Classifier
from . import classifier_abc

# Feature Extraction Module
from . import feature_extraction

class NaiveBayesAlgorithm(classifier_abc.Classifier):

    def __init__(self, training_required = False, ):
       pass


    def classify(self):
        pass


    def get_accuracy(self):
        pass


    def get_dumped_file(self):
        pass


    def dump_files(self):
        pass


    def __str__(self):
        return "NaiveBayes"


    def need_training(self):
        # Trained Data Path
        os.chdir("Data/trained"+self.__str__())

        pickle_files = glob.glob("*.pickle")
        if not pickle_files:
            return True

        else: return False
    # end need_taining
