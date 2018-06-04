import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import random
import csv


def process_word(word):
    stop_words = []
    stop_words = stopwords.words('english')
    stop_words.append('AT_USER')
    stop_words.append('URL')


    word = word.lower()
    word = re.sub(r'[^\w\s]', '', word)
    word = re.sub(" \d+", " ", word)
    # Convert www.* or https?://* to URL
    word = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', word)
    # Convert @username to AT_USER
    word = re.sub('@[^\s]+', 'AT_USER', word)
    # Remove additional white spaces
    word = re.sub('[\s]+', ' ', word)
    # Remove #
    word = re.sub(r'#([^\s]+)', r'\1', word)
    # trim
    word = word.strip('\'"')
    word = [i.lower() for i in list(set(nltk.word_tokenize(word)))
            if i not in stop_words]
    return word


def clean_data(txt_files=None, csv_files=None,json_files=None):
    """

    :param txt_files: list of the raw text files to be processed
    :param csv_file: list of the raw csv files to be processed
    :return:
    """

    features = []
    words = []

    #process txt files:
    if txt_files:
        #
        documents = []
        #
        all_words = []
        for file in txt_files:

            file_text = open(file, encoding='utf8').read()
            for word in file_text.split('\n'):
                procesed_word = process_word(word)
                all_words+= procesed_word
                documents.append((procesed_word, file[:-4]))
            #end for word in file_text
        #end for file in txt_files
        features.extend(documents)
        words.extend(all_words)
    #end if txt_files

    if csv_files:
        all_tweets= []
        tweets = []
        for file in csv_files:
            file_rows = csv.reader(open(file, 'r',encoding='utf8',), delimiter=',', quotechar='|')
            count = 0

            for row in file_rows:
                try:
                    count +=1
                    tweet = row[1]
                    sentiment = row[0]
                    processed_tweet= process_word(tweet)
                    all_tweets.extend(processed_tweet)
                    tweets.append((processed_tweet, sentiment))
                except(IndexError):
                    continue
            #end for row
        #end for file
        features.extend(tweets)
        words.extend(all_tweets)
    #end if csv_file

    if json_files:
        pass


    random.shuffle(features)
    word_features = list(words)

    return features, word_features
# end clean_data


def extract_features(document, word_features):
    """
    :param document: Bag of words with the randomly chosen data-set
    :return: features: dictionary that states the availablity of words,
            with the word as key, and Boolean value stats if it exists or not as its value,
            '[mode]:False,
             [egypt]:True, '
    """
    print(3)
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % str(word)] = (word in document_words)
    print(4)
    return features
# end extract_features
