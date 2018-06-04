from Tweetext import Tweetext
from time import time
import nltk

# start = time()
# demo = Tweetext()
#
# doc, word_feat = demo.process_data("Classifiers/Data/raw",)
# print('Data Processed', time() - start)
# print(len(doc), len(word_feat))
#
# all_words = nltk.FreqDist(word_feat)
# print(list(all_words.keys())[:30])

# train, test = demo.feature_extraction(doc[:1000], word_feat[:8000], 60, 10)
# print('Features Extracted', time() - start)
# print(train[:10])



demo = Tweetext()
demo.train()