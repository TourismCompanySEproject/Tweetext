import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re, sys, random, csv


def process_word(word):
    stop_words = []
    stop_words = stopwords.words('english')
    stop_words.append('AT_USER')
    stop_words.append('URL')


    word = word.lower()

    # Convert www.* or https?://* to URL
    word = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', word)
    # Convert @username to AT_USER
    word = re.sub('@[^\s]+', 'AT_USER', word)
    # Remove #
    word = re.sub(r'#([^\s]+)', r'\1', word)
    # Remove additional white spaces
    word = re.sub('[\s]+', ' ', word)

    word = re.sub(r'[^\w\s]', '', word)
    word = re.sub(" \d+", " ", word)
    # trim
    word = word.strip('\'"')
    processed_word = [i.lower() for i in list(set(nltk.word_tokenize(word)))
            if i not in stop_words]
    return processed_word


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
            try:
                # file_text = open(file, encoding='utf8').read()
                file_text = open(file, encoding="iso-8859-1").read()
            except FileNotFoundError:
                print(file+" was not found.")
                sys.exit(0)
            except UnicodeDecodeError:
                print("From clean_data() at feature_extraction:\n" +
                      file + " causes unicode decode error.")
                continue


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
                    label = row[0]
                    processed_tweet= process_word(tweet)
                    all_tweets.extend(processed_tweet)
                    tweets.append((processed_tweet, label))
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
    if len(document) == 0 :
        return {}
    document_words = set(document)
    features_set = {}
    for word in word_features:
        features_set['contains(%s)' % str(word)] = (word in document_words)
    return features_set
# end extract_features
