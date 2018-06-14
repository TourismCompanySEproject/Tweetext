from Tweetext import Tweetext
from time import time
# import sys
# from Classifiers.nb_algorithm import NaiveBayesAlgorithm
# from Classifiers.Directions import Raw_Data_Dir


start = time()
demo_nb = Tweetext("nb")
demo_nb.train(train_set_no=8000)
print('Elapsed time:', time() - start)


start = time()
demo_svm = Tweetext(algorithm="svm")
demo_svm.train(train_set_no=8000)
# print(demo.classify("""Well, that is taxation law of India (other side).In India 52,911
#                             # Profitable Companies Pay 0% Tax in India!"""))
# print(demo.classify('Help us build the best cricket game ever.'))
print('Elapsed time:', time() - start)


start = time()
demo_mnb = Tweetext(algorithm="mnb")
demo_mnb.train(train_set_no=8000)
print('Elapsed time:', time() - start)




#
# test = NaiveBayesAlgorithm()
# test.train(raw_data_path= Raw_Data_Dir.__getattr__(),
#            # train_set_no = -7
#            )