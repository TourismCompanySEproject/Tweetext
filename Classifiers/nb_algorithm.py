import nltk
import re, pickle, os, glob, sys

# Abstract Class
from abc import abstractmethod
# from .classifier_abc import Classifier
from . import classifier_abc

# Feature Extraction Module
from .feature_extraction import *

class NaiveBayesAlgorithm(classifier_abc.Classifier):

    def __init__(self, training_required = False,
                 path =None, url=None,
                 train_set_no=60, test_set_no=10,):

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.trained_data_path = BASE_DIR + "/Classifiers/Data/trained"
        self.classifierDumpFile = "NB.pickle"
        print(1)

        if training_required or self.need_training() :
          self.documents, self.word_features = self. process_data(path, url)
          print(2)

          self.train_set, self.test_set = self.feature_extraction(
              self.documents[:1000], self.word_features[:8000], 60, 10)
          print(3)

          print(4)

          classifier = self.classify(self.train_set, self.classifierDumpFile)
          print(5)

          print(self.get_accuracy())
        #end __init__


    def process_data(self, path=None, url=None):
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
        self.processsed = clean_data(raw_txt_files, raw_csv_files, raw_json_files)

        return self.processsed
        # end process_data


    def feature_extraction(self, documents, word_features, train_set_no, test_set_no):
        """
        :param documents:
        :param word_features:
        :param train_set_no:
        :param test_set_no:
        :return: train_set: dictionary of labled features for training the system.
                 test_set:  dictionary of labled features for testing the system.
        """
        self.featuresets = [(extract_features(doc, word_features), c) for (doc, c) in documents]
        self.train_set, self.test_set = self.featuresets[train_set_no:], self.featuresets[:test_set_no]
        print("Train set length", len(self.train_set),"Test set length", len(self.test_set))
        return self.train_set, self.test_set
    #end feature_extraction


    def classify(self, training_set, classifierDumpFile):
        """

        :param training_set: Features to train the classifier
        :param classifierDumpFile: File name to dump -save- the trained data.
        :return: classifier
        """
        self.classifier = nltk.NaiveBayesClassifier.train(training_set)

        self.dump_files(self.classifier, classifierDumpFile)
        return self.classifier
    # end classify

    def get_accuracy(self):
        """
            gets the accurcy value of the classifier
        :return: accuracy : float
        """
        self.clf = self.get_dump_file(self.classifierDumpFile)
        self.accuracy = (nltk.classify.accuracy(self.clf, self.test_set ))*100
        return self.accuracy
    # end get_accuracy


    def get_dump_file(self, classifierDumpFile):
        """
            Retrive the trained data saved as pickle
        :param classifierDumpFile: File name
        :return: classifier : the saved data
        """
        os.chdir(self.trained_data_path)
        try:
            f1 = open(classifierDumpFile, 'rb')
            if (f1):
                self.classifier = pickle.load(f1)
                f1.close()
        except IOError:
            "Can't open Dump file."

        return self.classifier
    # end get_dump_file


    def dump_files(self, classifier, classifierDumpFile):
        """
        :param classifier: Data to be dumped, saved.
        :param classifierDumpFile: File name
        :return: None
        """
        os.chdir(self.trained_data_path)
        try:
            outfile = open(classifierDumpFile, 'wb')
            pickle.dump(classifier, outfile)
            outfile.close()
        except IOError:
            "Can't create Dump file."
    # end dump_files

    def predict(self, input):
        self.classifier = pickle.load(open('data/trained/MNB.pickle', 'rb'))
        word_features = pickle.load(open('data/trained/word_features.pickle', 'rb'))

        token = nltk.word_tokenize(input.lower())
        return self.classifier.classify(document_features(token))

        pass

    def __str__(self):
        return "NaiveBayes"
    #end str


    def need_training(self):
        """
        Checkes if There's already trained data on not
        :return: Boolean, True if no trained data available
                        False if trained data available
        """
        # Trained Data Path
        os.chdir(self.trained_data_path)

        pickle_files = glob.glob(self.classifierDumpFile)
        if not pickle_files:
            return True

        else: return False
    # end need_taining


