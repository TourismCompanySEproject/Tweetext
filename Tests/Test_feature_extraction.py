import unittest
import os
from Classifiers import feature_extraction
from collections import Counter

class Test_feature_extraction(unittest.TestCase):
    # Process_word func need 5 test case to achieve 100% Statement coverage
    #Test case :
    #       01  -One string that has all the mentioned stop words
    #       02  -Empty string
    #       03  -One word string

    def test_process_word_01 (self):

        #arrange
        word = "Hi   @manara My link is www.google.com and https://www.youtube.com and my #nickname is 'Manaraa' Weather is perfect "
        fe= feature_extraction
        #act
        result = fe.process_word(word)
        expected = ["hi","link","nickname","manaraa","weather","perfect"]
        #assert
        self.assertCountEqual(expected,result)


    def test_process_word_02 (self):

        #arrange
        word = ""
        fe= feature_extraction
        #act
        result = fe.process_word(word)
        expected = []
        #assert
        self.assertCountEqual(expected,result)


    def test_process_word_03 (self):
        #arrange
        word = "Hi"
        fe= feature_extraction
        #act
        result = fe.process_word(word)
        expected = ["hi"]
        #assert
        self.assertCountEqual(expected,result)

    # clean_data func need 3 test cases to achieve 100% Statement coverage
    #Test cases :
    #       01  - 1 valid text file ( 1 item in list)
    #       02  - 1 invalid empty text file
    #       03  - 1 valid csv file (list of files and csv file) and empty feature extraction
    #NOTE : if file no file with mentioned name existing in directory .. exception is handling it

    def test_clean_data_01 (self):
        #arrange
        filetxt=["test_doc.txt"]
        fe= feature_extraction
        expected_features = [(['president', 'trump', 'praised', 'australias', 'universal',
                 'health', 'care', 'right', 'house', 'repealed', 'obamacare'], filetxt[0][0:-4])]

        expected_words = ['president', 'trump', 'praised', 'australias', 'universal',
                 'health', 'care', 'right', 'house', 'repealed', 'obamacare']
        #act
        features, words = fe.clean_data(txt_files=filetxt)

        #assert
        self.assertEqual(len(expected_features),len(features))
        self.assertCountEqual(set(expected_words),set(words))


    def test_clean_data_02(self):
        # arrange
        file = ["emptyText.txt"]
        fe = feature_extraction
        expected1 = [([],file[0][0:-4])]
        expected2 = []
        # act
        result1,result2  = fe.clean_data(txt_files=file)
        # assert
        self.assertCountEqual(result1, expected1)
        self.assertCountEqual(result2, expected2)


    def test_clean_data_03 (self):
        # arrange
        filecsv=["test_doc.csv"]
        fe = feature_extraction
        # act
        expected_features = [(['president', 'trump', 'praised', 'australias', 'universal',
                               'health', 'care', 'right', 'house', 'repealed', 'obamacare'], 'test_doc')]

        expected_words = ['president', 'trump', 'praised', 'australias', 'universal',
                          'health', 'care', 'right', 'house', 'repealed', 'obamacare']
        # act
        features, words = fe.clean_data(csv_files=filecsv)

        # assert
        self.assertEqual(len(expected_features), len(features))
        self.assertCountEqual(set(expected_words), set(words))

    #Extract_feature need 3 test cases to achieve 100% statement coverage
    #Test cases :
    #       01  - 2 valid inputs ( lists)
    #       02  - 1 valid inputs ( list) and empty document
    #       03  - 1 valid inputs ( list) and empty feature extraction

    def test_extract_features_01 (self):
        fe = feature_extraction
        expected = {'contains(health)':False ,'contains(vote)':True, 'contains(plan)':True,
                    'contains(passes)':False,'contains(megthread)':True, 'contains(house)':False,
                    'contains(care)':False, 'contains(republican)':False, 'contains(bill)':False,
                    'contains(didnt)':False,'contains(congressman)':True,'contains(discussion)':True,
                    'contains(serve)':False, 'contains(fitness)':False, 'contains(trumps)':True}
        # act
        document=['vote','plan','megthread','trumps','congressman','discussion']
        word_features=['health', 'vote', 'plan', 'passes', 'megthread', 'house', 'care', 'republican',
                       'bill', 'didnt','congressman',
                       'discussion','serve', 'fitness', 'trumps']
        result = fe.extract_features(document,word_features)

        # assert
        self.assertCountEqual(result, expected)


    def test_extract_features_02 (self):
        fe = feature_extraction
        # expected = {'contains(health)': False, 'contains(vote)': False, 'contains(plan)': False,
        #             'contains(passes)': False, 'contains(megthread)': False,
        #             'contains(house)': False, 'contains(care)': False, 'contains(republican)': False,
        #             'contains(bill)': False, 'contains(didnt)': False, 'contains(congressman)': False,
        #             'contains(discussion)': False, 'contains(serve)': False, 'contains(fitness)': False,
        #             'contains(trumps)': False}
        expected = {}
        # act
        document=[]
        word_features = ['health', 'vote', 'plan', 'passes', 'megthread', 'house', 'care', 'republican',
                         'bill', 'didnt', 'congressman',
                         'discussion', 'serve', 'fitness', 'trumps']
        result = fe.extract_features(document,word_features)

        # assert
        self.assertCountEqual(result, expected)


    def test_extract_features_03 (self):
        fe = feature_extraction
        expected={}
        # act
        document = ['vote', 'plan', 'megthread', 'trumps', 'congressman', 'discussion']
        word_features = []
        result = fe.extract_features(document,word_features)
        # assert
        self.assertCountEqual(result, expected)

if __name__ == '__main__':
    unittest.main()