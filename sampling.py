from utils import *
from binary import *
from nonbinary import *

def make_sample_of_appliable(appliable, sample_size, pics, condition=None):
    results = []
    while True:
        if len(results) >= sample_size:
            return results
        pic = select_random_pic(pics)
        x, y = select_random_xoord_on_pic(pic)
        if condition is None or condition(pic, x, y)>0:
            res = appliable.apply2(pic, x, y)
            results.append(res)
    return results