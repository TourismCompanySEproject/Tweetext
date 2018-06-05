from abc import ABC, abstractmethod



class Classifier(ABC):
    """
        Abstract base class for all Algoritm classes,
        Applied to empashize the Factory Desgin Pattern
    """

    # __training_required = False

    # def __init__(self, training_required=False, ):
    #     pass

    @abstractmethod
    def process_data(self, path = None, url = None):
        pass

    @abstractmethod
    def feature_extraction(self, documents, word_features, train_set_no, test_set_no):
        pass

    @abstractmethod
    def classify(self):
        pass

    @abstractmethod
    def get_accuracy(self):
        pass

    @abstractmethod
    def get_dump_file(self):
        pass

    @abstractmethod
    def dump_files(self):
        pass

    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def need_training(self):
        pass


    def factory(self, algorithm = 'NaiveBayesAlgorithm'):
        if algorithm == "NaiveBayesAlgorithm":
            from .nb_algorithm import NaiveBayesAlgorithm
            return NaiveBayesAlgorithm()
        #
        # other algorithms to be added here
        #
        assert 0, "Wrong input"+algorithm
    factory = staticmethod(factory)
    # end fuctory