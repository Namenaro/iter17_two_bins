"""
Щелкаем по эталонной тройке в 3 местах.
0)A, 1)B, 2)h

"""
from data import *
from sampling import *
from clicker import *
from chain import *
from measure_prediction_error import *
from logger import *
from utils import *
from binary import *
from nonbinary import *

import matplotlib.pyplot as plt

def exp0(etalon_pic, X, Y,logger, B_u_rad, h_u_rad):
    A_sens_rad = 0
    B_sens_rad = 0
    h_sens_rad = 0

    A_u_rad = 0


    A_event_diam = 80
    step = 20
    B_event_diam_grid = range(0, 700, step)


    A_etalon = make_measurement(etalon_pic, X[0], Y[0], A_sens_rad)
    h_etalon = make_measurement(etalon_pic, X[2], Y[2], h_sens_rad)
    B_etalon = make_measurement(etalon_pic, X[1], Y[1], B_sens_rad)

    A = BinaryUnit(A_u_rad, A_sens_rad, A_etalon, A_event_diam, dx=0, dy=0)
    ha = NonBinaryUnit(h_u_rad, h_sens_rad, h_etalon, dx=X[2] - X[0], dy=Y[2] - Y[0])
    hb = NonBinaryUnit(h_u_rad, h_sens_rad, h_etalon, dx=X[2] - X[1], dy=Y[2] - Y[1])

    hA_err = []
    hB_err = []
    hAB_err = []

    dataset = get_numbers_of_type(3)
    n = len(dataset)
    trainset_len = int(n / 2)
    pics_train = get_numbers_of_type(3)[0:trainset_len]
    pics_test = get_numbers_of_type(3)[trainset_len + 1:n - 1]
    sample_size_train = 50
    sample_size_test = 150
    nbins = 10

    logger.add_text("A:")
    logger.add_text(str(vars(A)))
    logger.add_text("ha:")
    logger.add_text(str(vars(ha)))
    logger.add_text(str(vars(BinaryUnit(B_u_rad, B_sens_rad, B_etalon,0, dx=X[1] - X[0], dy=Y[1] - Y[0]))))

    for B_diam in B_event_diam_grid:
        B = BinaryUnit(B_u_rad, B_sens_rad, B_etalon, B_diam, dx=X[1] - X[0], dy=Y[1] - Y[0])
        AB = Chain(A, B)
        reality_test_sample = make_sample_of_appliable(appliable=ha, sample_size=sample_size_test, pics=pics_test,
                                           condition=AB.apply2)

        A_err = eval_error_of_prediction(reality_test_sample, pics_train,sample_size_train,A,ha, nbins )
        hA_err.append(A_err)

        B_err = eval_error_of_prediction(reality_test_sample, pics_train,sample_size_train,B,hb, nbins )
        hB_err.append(B_err)

        AB_err = eval_error_of_prediction(reality_test_sample, pics_train,sample_size_train,AB,ha, nbins )
        hAB_err.append(AB_err)

    h_err = eval_error_of_prediction(reality_test_sample, pics_train, sample_size_train,None, ha, nbins )
    logger.add_fig(plot_points_on_pic_first_red(etalon_pic, X, Y))
    draw(B_event_diam_grid,  hA_err, hB_err, hAB_err, logger, h_err)

def draw(grid, hA_err, hB_err, hAB_err, logger, h_err):
    fig, ax = plt.subplots()
    ax.plot(grid, hA_err,  markerfacecolor='blue', markersize=12, color='#00bfff', linewidth=4, label='by A')
    ax.plot(grid,hB_err,  markerfacecolor='blue', markersize=12, color='#0080ff', linewidth=4, label='by B')
    ax.plot(grid,hAB_err, markerfacecolor='blue', markersize=12, color='#40ff00', linewidth=4, label='by AB')
    plt.axhline(y=h_err, color='black', linestyle='-', label='no binaries')
    ax.legend()
    logger.add_fig(fig)

if __name__ == "__main__":
    logger = HtmlLogger("17exp0-vary event diam")
    etalon_pic = etalons_of3()[0]  # эталон
    X, Y = select_coord_on_pic(etalon_pic)  # click - 0)A, 1)B, 2)h
    B_u_rad = 0
    h_u_rad = 0
    exp0(etalon_pic, X, Y, logger, B_u_rad, h_u_rad)

    B_u_rad = 0
    h_u_rad = 1
    exp0(etalon_pic, X, Y, logger, B_u_rad, h_u_rad)


    logger.close()
