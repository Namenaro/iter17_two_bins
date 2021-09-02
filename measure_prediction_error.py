from sampling import *
from utils import *

def eval_error_of_prediction(reality_test_sample, pics_train, sample_size_train, A, ha, nbins ):
    predictor = Predictor(A,ha, sample_size_train, pics_train, nbins)
    prediction = predictor.predict(len(reality_test_sample))
    return count_error_btw_two_samples(reality_test_sample, prediction)

class Predictor:
    def __init__(self,A,ha, sample_size_train, pics_train, nbins):
        self.A = A
        self.ha = ha
        if A is None:
            condition = None
        else:
            condition = A.apply2
        train_sample = make_sample_of_appliable(ha,sample_size_train,pics_train,condition)
        self.probs, self.bins = get_hist(train_sample, nbins)

    def predict(self, test_sample_size):
        prediction = sample_from_hist(self.probs, self.bins, test_sample_size)
        return prediction


