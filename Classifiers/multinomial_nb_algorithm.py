import nltk
from sklearn.naive_bayes import MultinomialNB
from Classifiers import classifier_abc


# from .classifier_abc import Classifier
from Classifiers import classifier_abc

class MultinomailNBAlgorithm(classifier_abc.Classifier):

    def __init__(self, training_required = False,
                 raw_data_path =None,
                 train_set_no=6000, test_set_no=1000,):

        # Specific Dump file name for algorithm's Trained data
        self.classifierDumpFile = " MultinomialNB.pickle"

        # Check if algorithm Trained data is not present,
        # or user requests training.
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
        self.MNB_classifier = nltk.SklearnClassifier (MultinomialNB ())
        self.MNB_classifier.train (training_set)

        # Save the trained data in pickle for further use.
        self.dump_files(self.MNB_classifier, classifierDumpFile)

        return self.MNB_classifier
    # end classify

    def __str__(self):
        return "MultinomailNBAlgorithm"
    #end str