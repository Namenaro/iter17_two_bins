from nonbinary import *

from random import choice
import random
import matplotlib.pyplot as plt
import numpy as np

def select_random_pic(pics):
    return choice(pics)

def select_random_xoord_on_pic(pic):
    maxX = pic.shape[1]
    maxY = pic.shape[0]
    x = random.randint(0, maxX - 1)
    y = random.randint(0, maxY - 1)
    return x,y

def apply_binary_unit_to_pic(pic, unit):
    ymax = pic.shape[0]
    xmax = pic.shape[1]
    XYs = []

    for y in range(0, ymax):
        for x in range(0, xmax):
            matches = unit.apply(pic, x, y)
            if len(matches) > 0:
                XYs.append([x,y])
    return XYs

def get_hist(values,nbins, maxv=255):
    if isinstance(values[0], NonBinaryMatch):
        values = [values[i].value for i in range(len(values))]
    if not isinstance(values, np.ndarray):
        values = np.array(values)
    (probs, bins, _) = plt.hist(values, bins=nbins,
                                    weights=np.ones_like(values) / len(values), range=(0, maxv))

    return probs, bins

def sample_from_hist(probs, bins, sample_size):
    bin_ids =list(range(0, len(probs)))
    bins_sample = np.random.choice(bin_ids, sample_size, p=probs)
    sample = []
    for bin_id in bins_sample:
        val = np.random.uniform(bins[bin_id],bins[bin_id+1])
        sample.append(val)
    return sample

def count_error_btw_two_samples(ground_true, prediction):
    res = 0
    for i in range(len(ground_true)):
        res+=(ground_true[i].value - prediction[i])**2
    return res/len(ground_true)

def plot_points_on_pic_first_red(pic, X,Y, colors=None):
    if colors is None:
        colors = 'green'
    fig, ax = plt.subplots()
    plt.imshow(pic, cmap='gray_r')
    plt.scatter(X[0], Y[0], s=100, c='red', marker='o', alpha=0.4)
    plt.scatter(X[1:], Y[1:], s=100, c=colors, marker='o', alpha=0.4)
    return fig

def plot_graph(X, Y):
    fig, ax = plt.subplots()
    ax.plot(X,Y, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
    return fig