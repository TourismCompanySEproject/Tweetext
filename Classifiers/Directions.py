import os, sys

class Base_Dir:
    __BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    __instances = None
    def __getattr__():
        return Base_Dir.__BASE_DIR


class Trained_Data_Dir:
    __TRAINED_DATA_DIR = Base_Dir.__getattr__() + "/Classifiers/Data/trained"

    def __getattr__():
        return Trained_Data_Dir.__TRAINED_DATA_DIR


class Raw_Data_Dir:
    __RAW_DATA_DIR = Base_Dir.__getattr__() + "/Classifiers/Data/raw"

    def __getattr__():
        return Raw_Data_Dir.__Raw_DATA_DIR

Trained_Data_Dir.__getattr__()