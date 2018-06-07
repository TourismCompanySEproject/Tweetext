from Tweetext import Tweetext
from time import time
import nltk

from Classifiers.nb_algorithm import NaiveBayesAlgorithm



# print(len(doc), len(word_feat))
#
# all_words = nltk.FreqDist(word_feat)
# print(list(all_words.keys())[:30])

# train, test = demo.feature_extraction(doc[:1000], word_feat[:8000], 60, 10)
# print('Features Extracted', time() - start)
# print(train[:10])



start = time()
demo = Tweetext()
demo.train(train_set_no=8000)
print(demo.classify("Well, that is taxation law of India (other side).In India 52,911 Profitable Companies Pay 0% Tax in India!"))
print('Elapsed time:', time() - start)

# nb_demo = NaiveBayesAlgorithm(training_required = True, raw_data_path = "Classifiers/Data/raw" )
# # nb_demo = NaiveBayesAlgorithm()
# print(nb_demo.classify("""Well, that is taxation law of India (other side).In India 52,911
#                           Profitable Companies Pay 0% Tax in India!"""))