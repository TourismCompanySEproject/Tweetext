import re, pickle, csv, os, nltk
from sklearn.svm import LinearSVC
from . import classifier_abc

class SVMAlgorithm(classifier_abc.Classifier):

    def __init__(self, training_required = False,
                 raw_data_path =None,
                 train_set_no=6000, test_set_no=1000,):

        # Specific Dump file name for algorithm's Trained data
        self.classifierDumpFile = "SVM.pickle"

        # Check if algorithm Trained data is not present,
        # or user requests training.
        # call training model
        # if training_required or self.need_training() :
        #     self.train(raw_data_path,
        #                train_set_no, test_set_no, )

        #end __init__

    def classify(self, training_set, classifierDumpFile):
        """

        :param training_set: Features to train the classifier
        :param classifierDumpFile: File name to dump -save- the trained data.
        :return: classifier
        """
        # Train the module of the specified algorithm using the created training set.
        self.classifier = nltk.SklearnClassifier(LinearSVC())
        self.classifier.train(training_set)
        #self.classifier = nltk.NaiveBayesClassifier.train(training_set)
        # Save the trainied data in pickle for further use.
        self.dump_files(self.classifier, self.classifierDumpFile)

        return self.classifier
    # end classify

    def __str__(self):
        return "SVMAlgorithm"

