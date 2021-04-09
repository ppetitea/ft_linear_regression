import matplotlib.pyplot as plt
import numpy as np


def round2(list):
    ret = []
    for n in list:
        ret.append(round(float(n), 2))
    return ret


def linearList(list, a, b):
    ret = []
    for x in list:
        ret.append(float(a * x + b))
    return ret


def showResult(x, prices, filename, a, b, head):
    # plotting points as a scatter plot
    rx = round2(x)
    ry = round2(prices)
    label = head[1] + " / " + head[0]
    plt.scatter(rx, ry, label=label, color="green", marker="*", s=30)
    pX = np.arange(float(min(x)), float(max(x)), 0.1)
    pY = linearList(pX, a, b)
    plt.plot(pX, pY, label="estimation", color="red")
    # x-axis label
    plt.xlabel('x - kilometers')
    # frequency label
    plt.ylabel('y - price')
    # plot title
    plt.suptitle(filename)
    plt.figtext(0, 0, str(round(a, 2)) + "x + " + str(round(b, 2)))
    # showing legendp
    plt.legend()

    # function to show the plot
    plt.show()
