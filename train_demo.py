from Tweetext import Tweetext
from time import time
#
start = time()
demo = Tweetext(algorithm="svm")
demo.train(train_set_no=8000)
# print(demo.classify("the women's march protestors were disrespectful whiners."))
print('Elapsed time:', time() - start)

# nb_demo = NaiveBayesAlgorithm(training_required = True, raw_data_path = "Classifiers/Data/raw" )
# # nb_demo = NaiveBayesAlgorithm()
# print(nb_demo.classify("""Well, that is taxation law of India (other side).In India 52,911
#                           Profitable Companies Pay 0% Tax in India!"""))

