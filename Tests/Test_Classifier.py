import unittest
import unittest.mock as mock
import os, glob
from Classifiers import classifier_abc
from Classifiers.nb_algorithm import NaiveBayesAlgorithm
from Classifiers.svm_algorithm import SVMAlgorithm
from Classifiers.Directions import Trained_Data_Dir, Raw_Data_Dir

class Test_Classifier(unittest.TestCase):

    # dump_files() func need 3 test case to achieve 100% Statement coverage
    # Test case :
    #       01  - Valid file name.
    #       02  - invalid file name, number.
    #       03  - invlaid file name, not pickle.
    def test_dump_files_01(self):
        # arrange
        dump_file_name = "test_pickle.pickle"
        data = ["test data"]
        # act
        svm_algorithm = SVMAlgorithm()
        svm_algorithm.dump_files(data, dump_file_name)

        # assert
        os.chdir(Trained_Data_Dir.__getattr__())
        self.assertIsNotNone(glob.glob(dump_file_name))


    def test_dump_files_02(self):
        # arrange
        dump_file_name = 5
        data = ["test data"]
        result = False
        # act
        try:
            svm_algorithm = SVMAlgorithm()
            svm_algorithm.dump_files(data, dump_file_name)
        except NameError:
            result = True

        # assert
        self.assertTrue(result)

    def test_dump_files_03(self):
        # arrange
        dump_file_name = "test_pickle.txt"
        data = ["test data"]
        result = False
        # act
        try:
            svm_algoritm = SVMAlgorithm()
            svm_algorithm.dump_files(data, dump_file_name)
        except NameError:
            result = True
        # assert
        self.assertIsNotNone(result)


    def test_get_dump_file_01(self):
        # arrange
        dump_file_name = "test_pickle.pickle"
        data = ["test data"]
        # act
        svm_algorithm = SVMAlgorithm()
        result = svm_algorithm.get_dump_file(dump_file_name)
        # assert
        self.assertEqual(data, result)

    def test_get_dump_file_02(self):
        # arrange
        dump_file_name = 5
        data = ["test data"]
        result = False
        # act
        try:
            svm_algorithm = SVMAlgorithm()
            result = svm_algorithm.get_dump_file(dump_file_name)
        except NameError:
            result = True
        # assert
        self.assertTrue(result)


    def test_get_dump_file_03(self):
        # arrange
        dump_file_name = "test_pickle.txt"
        data = ["test data"]
        result = False
        # act
        try:
            svm_algorithm = SVMAlgorithm()
            result = svm_algorithm.get_dump_file(dump_file_name)
        except NameError as e:
            result = True
        # assert
        self.assertTrue(result)


    # need_training() func need 2 test case to achieve 100% Statement coverage
    # Test case :
    #       01  -Checking one algorithm that needs training.
    #       02  -Checking one algorithm that doesn't need training.
    def test_need_training_01(self):
        # arrange
        expected = True
        # act
        nb_algorithm = NaiveBayesAlgorithm()
        result = nb_algorithm.need_training()
        # assert
        self.assertEqual(expected, result)

    def test_need_training_02(self):
        # arrange
        expected = False
        # act
        svm_algorithm = SVMAlgorithm()
        result = svm_algorithm.need_training()
        # assert
        self.assertEqual(expected, result)


    # get_accuracy() func need 2 test case to achieve 100% Statement coverage
    # Test case :
    #       01  - Trained module
    #       02  - Not trained module
    def test_get_accuracy_01(self):
        # arrange

        # act
        svm_algorithm = SVMAlgorithm()
        result = svm_algorithm.get_accuracy()
        # assert
        self.assertTrue(isinstance(result, float))

    def test_get_accuracy_02(self):
        # arrange

        # act
        nb_algorithm = NaiveBayesAlgorithm()
        result = nb_algorithm.get_accuracy()
        print(result)
        # assert
        self.assertTrue(isinstance(result,str))

    # get_accuracy() func need 2 test case to achieve 100% Statement coverage
    # Test case :
    #       01  -   Valid input, string
    #       02  -   Invalid input, number
    #       03  -   Invalid input, emppty string
    def test_predict_01(self):
        # arrange
        input = '@disney Thanks for a fun party!'
        expected = 'thanking'
        # act
        svm_algorithm = SVMAlgorithm()
        result = svm_algorithm.predict(input)

        #assert
        self.assertEqual(result, expected)


    def test_predict_02(self):
        # arrange
        input = ''
        expected = 'Invalid input.'
        # act
        svm_algorithm = SVMAlgorithm()
        result = svm_algorithm.predict(input)

        #assert
        self.assertEqual(result, expected)


    def test_predict_03(self):
        # arrange
        input = 5
        expected = 'Invalid input.'
        # act
        svm_algorithm = SVMAlgorithm()
        result = svm_algorithm.predict(input)

        # assert
        self.assertEqual(result, expected)


    @mock.patch('Classifiers.nb_algorithm.NaiveBayesAlgorithm.dump_files', return_value= None)
    @mock.patch('nltk.NaiveBayesClassifier.train', return_value = True)
    def test_classify_01(self, mock_nltk, mock_dump):
        # arrange

        # act
        nb_algorithm = NaiveBayesAlgorithm()
        nb_algorithm.classify(training_set=100, classifierDumpFile = "test_pickle.pickle")
        # assert
        mock_nltk.assert_called_with(100)
        self.assertTrue(mock_nltk)



if __name__ == '__main__':
    unittest.main()