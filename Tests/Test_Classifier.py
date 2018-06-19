import unittest, mock
import os, glob
from Classifiers import classifier_abc
from Classifiers.nb_algorithm import NaiveBayesAlgorithm
from Classifiers.svm_algorithm import SVMAlgorithm
from Classifiers.Directions import Trained_Data_Dir

class Test_Classifier(unittest.TestCase):
    @unittest.skip
    def test_train_01(self):
        pass


    # dump_files() func need 3 test case to achieve 100% Statement coverage
    # Test case :
    #       01  - Valid file name.
    #       02  - invalid file name, number.
    #       03  - invlaid file name, not pickle.
    @unittest.skip
    def test_dump_files_01(self):
        # arrange
        dump_file_name = "test_pickle.pickle"
        data = ["test data"]
        # act
        algoritm = SVMAlgorithm()
        algoritm.dump_files(data, dump_file_name)

        # assert
        os.chdir(Trained_Data_Dir.__getattr__())
        self.assertIsNotNone(glob.glob(dump_file_name))


    @unittest.skip
    def test_dump_files_02(self):
        # arrange
        dump_file_name = 5
        data = ["test data"]
        result = False
        # act
        try:
            algoritm = SVMAlgorithm()
            algoritm.dump_files(data, dump_file_name)
        except NameError:
            result = True

        # assert
        self.assertTrue(result)

    @unittest.skip
    def test_dump_files_03(self):
        # arrange
        dump_file_name = "test_pickle.txt"
        data = ["test data"]
        result = False
        # act
        try:
            algoritm = SVMAlgorithm()
            algoritm.dump_files(data, dump_file_name)
        except NameError:
            result = True
        # assert
        self.assertIsNotNone(result)


    @unittest.skip
    def test_get_dump_file_01(self):
        # arrange
        dump_file_name = "test_pickle.pickle"
        data = ["test data"]

        # act
        algoritm = SVMAlgorithm()
        result = algoritm.get_dump_file(dump_file_name)

        # assert
        self.assertEqual(data, result)

    @unittest.skip
    def test_get_dump_file_02(self):
        # arrange
        dump_file_name = 5
        data = ["test data"]
        result = False
        # act
        try:
            algoritm = SVMAlgorithm()
            result = algoritm.get_dump_file(dump_file_name)
        except NameError:
            result = True
        # assert
        self.assertTrue(result)

    @unittest.skip
    def test_get_dump_file_03(self):
        # arrange
        dump_file_name = "test_pickle.txt"
        data = ["test data"]
        result = False
        # act
        try:
            algoritm = SVMAlgorithm()
            result = algoritm.get_dump_file(dump_file_name)
        except NameError as e:
            result = True
        # assert
        self.assertTrue(result)


    # need_training() func need 2 test case to achieve 100% Statement coverage
    # Test case :
    #       01  -Checking one algorithm that needs training.
    #       02  -Checking one algorithm that doesn't need training.
    @unittest.skip
    def test_need_training_01(self):
        # arrange
        expected = True
        # act
        algorithm =NaiveBayesAlgorithm()
        result = algorithm.need_training()
        # assert
        self.assertEqual(expected, result)


    @unittest.skip
    def test_need_training_02(self):
        # arrange
        expected = False
        # act
        algorithm = SVMAlgorithm()
        result = algorithm.need_training()
        # assert
        self.assertEqual(expected, result)


    # get_accuracy() func need 2 test case to achieve 100% Statement coverage
    # Test case :
    #       01  - Trained module
    #       02  - Not trained module
    @unittest.skip
    def test_get_accuracy_01(self):
        # arrange

        # act
        algorithm = SVMAlgorithm()
        result = algorithm.get_accuracy()
        # assert
        self.assertTrue(result.is_integer())

    @unittest.skip
    def test_get_accuracy_02(self):
        # arrange

        # act
        algorithm = NaiveBayesAlgorithm()
        result = algorithm.get_accuracy()
        print(result)
        # assert
        self.assertTrue(isinstance(result,str))

    # get_accuracy() func need 2 test case to achieve 100% Statement coverage
    # Test case :
    #       01  -   Valid input, string
    #       02  -   Invalid input, number
    #       03  -   Invalid input, emppty string
    @unittest.skip
    def test_predict_01(self):
        # arrange
        input = '@disney Thanks for a fun party!'
        expected = 'thanking'
        # act
        algorithm = SVMAlgorithm()
        result = algorithm.predict(input)

        #assert
        self.assertEqual(result, expected)


    @unittest.skip
    def test_predict_02(self):
        # arrange
        input = ''
        expected = 'Invalid input.'
        # act
        algorithm = SVMAlgorithm()
        result = algorithm.predict(input)

        #assert
        self.assertEqual(result, expected)


    @unittest.skip
    def test_predict_03(self):
        # arrange
        input = 5
        expected = 'Invalid input.'
        # act
        algorithm = SVMAlgorithm()
        result = algorithm.predict(input)

        # assert
        self.assertEqual(result, expected)








if __name__ == '__main__':
    unittest.main()