import re, pickle, os, glob, sys
# Abstract Class
from abc import ABC, abstractmethod
#Base Direction
from .Directions import Base_Dir, Trained_Data_Dir
# Feature Extraction Module
from .feature_extraction import *


class Classifier(ABC):
    """
        Abstract base class for all Algoritm classes,
        Applied to empashize the Factory Desgin Pattern
    """
    def train(self, raw_data_path=None,
                 train_set_no=6000, test_set_no=100, ):
        """
            Responsible for gathering the raw dat to train,
            training the classifier,and saving the trained data in pickles,
        :param raw_data_path:
        :param train_set_no:
        :param test_set_no:
        :return: Null
        """
        if not isinstance(raw_data_path, str):
            raise NotADirectoryError("Invalid path format was entered.")

        if (train_set_no or test_set_no) <= 2:
            raise ValueError("Invalid number of features for training and testing set.")


        # Processing raw data: Cleaning, Removing Stopwords, Lowering case.
        self.features, self.word_features = self.process_data(raw_data_path)

        # Saving Feature list.
        self.dump_files(self.word_features, "word_features_file.pickle")

        # Features Extraction, and spliting them into Training and Testing sets.
        self.train_set, self.test_set = \
            self.feature_extraction(
                self.features[:1000], self.word_features[:8000], train_set_no, test_set_no
                                    )

        self.dump_files(self.test_set, "test_set.pickle")

        # Traing the classifier module using the Training and set,
        # and save the trained data into pickles.
        classifier = self.classify(self.train_set, self.classifierDumpFile)

        return(self.get_accuracy())
    #end train

    def predict(self, input):
        """
            Responsible of classifing the user input, and returning the result.
        :param input: Text to be classified
        :return: Category (label)
        """

        if (not isinstance(input, str)) or (len(input) <=2):
            return ("Invalid input.")

        # Head To Trained Data Directory
        os.chdir(Trained_Data_Dir.__getattr__())
        # Load the Saved Trained Data from pickle
        self.classifier = pickle.load(open(self.classifierDumpFile, 'rb'))
        # Load the Saved Feature List from pickle
        word_features = pickle.load(open('word_features_file.pickle', 'rb'))
        # Clean the input, Remove stopwords, puncituation.
        input = process_word(input)
        # Return the Category(label) of the input.
        return self.classifier.classify(extract_features(input, word_features))
    #end predict

    def process_data(self, raw_data_path=None):
        """
        :param raw_data_path: directory of the raw data to be processed
        :return: processed: the features and words after being processed,
        removing the stopwords, symbols, emoticons, and any unnecessary word.
        """

        # Checks for Raw Data Location:

        # Not present:
        if raw_data_path is None:
            raise NotADirectoryError("No Data directory was specified")

        # Ofline path provided:
        elif raw_data_path:
            try:
                # Head to Specified Directory
                os.chdir(raw_data_path)
            except FileNotFoundError:
                raise FileNotFoundError("Invalid Data directory path.")

            # Collect all Files in directory
            raw_txt_files = glob.glob("*.txt")
            raw_csv_files = glob.glob("*.csv")
            raw_json_files = glob.glob("*.json")

            if ((not raw_txt_files) and (not raw_csv_files) and (not raw_json_files)):
                raise FileNotFoundError("No files were found in specified directory.")

        # Process Data, Cleaning, Removing Stopwords, Lowering case.

        self.processsed = clean_data(raw_txt_files, raw_csv_files, raw_json_files)

        # Return Cleaned Data : Return Cleaned Data
        return self.processsed
        # end process_data


    def feature_extraction(self, features, word_features, train_set_no, test_set_no):
        """
            Responsible for
        :param features: Processed Data
        :param word_features:
        :param train_set_no: Number of features in Training set
        :param test_set_no: Number of features in Testing set
        :return: train_set: dictionary of labled features for training the system.
                 test_set:  dictionary of labled features for testing the system.
        """

        #Extract Features:
        #       Creating Dictinary with each Feature as key,
        #       and it's boolean state of existance as value.
        self.featuresets = [(extract_features(doc, word_features), category) for (doc, category) in features]

        #   Divide Features between Training and Testing sets.
        self.train_set, self.test_set = self.featuresets[len(self.featuresets)-train_set_no:], self.featuresets[:test_set_no]

        return self.train_set, self.test_set
    #end feature_extraction

    @abstractmethod
    def classify(self, training_set, classifierDumpFile):
        """
        :param training_set: Features to train the classifier
        :param classifierDumpFile: File name to dump -save- the trained data.
        :return: classifier
        """
        pass
    # end classify

    def get_accuracy(self):
        """
            gets the accurcy value of the classifier
        :return: accuracy : float
        """

        if not self.need_training():
            # Load Trained Data from pickle.
            self.clf = self.get_dump_file(self.classifierDumpFile)
            # Head To Trained Data Path
            os.chdir(Trained_Data_Dir.__getattr__())
            test_set = self.get_dump_file("test_set.pickle")
            # Get Acccuracy value.
            self.accuracy = (nltk.classify.accuracy(self.clf, test_set ))*100

            return self.accuracy
        else:
            return "Module is not trained."
    # end get_accuracy


    def get_dump_file(self, dump_file_name):
        """
            Retrive the trained data saved as pickle
        :param dump_file_name: File name
        :return: data : the saved data
        """
        if not isinstance(dump_file_name, str):
            raise NameError ("Invalid dump file name.")
        if not dump_file_name.endswith("pickle"):
            raise NameError("Invalid dump file format.")

        # Head To Trained Data Path
        os.chdir(Trained_Data_Dir.__getattr__())
        try:
            file = open(dump_file_name, 'rb')
            if (file):
                self.data = pickle.load(file)
                file.close()

        except FileNotFoundError:
            raise FileNotFoundError("Can't find Dump file.")
        except IOError:
            raise IOError("Can't open Dump file.")

        return self.data
    # end get_dump_file


    def dump_files(self, data, dump_file_name):
        """
            Responsible for saving the data in pickle format.
        :param data: Data to be dumped, saved.
        :param dump_file_name: File name
        :return: None
        """
        if not isinstance(dump_file_name, str):
            raise NameError("Invalid dump file name.")
        if not dump_file_name.endswith("pickle"):
            raise NameError("Invalid dump file format.")

        # Head To Trained Data Path
        os.chdir(Trained_Data_Dir.__getattr__())
        # Save Data.
        try:
            outfile = open(dump_file_name, 'wb')
            pickle.dump(data, outfile)

            outfile.close()
        except IOError:
            raise IOError("Can't create Dump file "+ dump_file_name)
    # end dump_files


    def need_training(self):
        """
        Checkes if There's already trained data on not
        :return: Boolean, True if no trained data available
                        False if trained data available
        """
        # Head To Trained Data Path
        try:
            os.chdir(Trained_Data_Dir.__getattr__())

        except NotADirectoryError:
            raise NotADirectoryError("Invalid Data directory path.")

        # Check if there are Trained data for the spicified algorithm saved.
        pickle_file = glob.glob(self.classifierDumpFile)
        if not pickle_file: return True
        else: return False
    # end need_taining


    def factory(algorithm):
        """
            Creation of Classifier.
        :param algorithm: Name The Algorithm to be used for classifier.
        :return: The created Classifier object.
        """
        algorithm = algorithm.lower()

        if algorithm in ["naivebayesalgorithm", "naivebayes", "nb"]:
            from .nb_algorithm import NaiveBayesAlgorithm
            return NaiveBayesAlgorithm()
        if algorithm in ["svm"]:
            from .svm_algorithm import SVMAlgorithm
            return SVMAlgorithm()
        if algorithm in ["multinomial", "multinomial_nb", "mnb"]:
            from .multinomial_nb_algorithm import MultinomailNBAlgorithm
            return MultinomailNBAlgorithm()
            return PassiveAggressiveAlgorithm()
        assert 0, "Wrong input"+algorithm
    factory = staticmethod(factory)
    # end fuctory
