import argparse
import csv
import sys
import matplotlib.pyplot as plt
import numpy as np


def importData(filename):
    rows = []
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            rows.append(row)
    return rows


def parseData(data):
    head = data.pop(0)
    x = []
    y = []
    for row in data:
        x.append(float(row[0]))
        y.append(float(row[1]))
    return [x, y, head]


def getData(filename):
    csvData = importData(filename)
    if len(csvData) > 2:
        return parseData(csvData)
    print('fail to import csv data')
    return -1


def linear(a, b, x):
    return a * x + b


def normalize(n, list):
    return (float(n) - float(min(list))) / (float(max(list)) - float(min(list)))


def normalizeList(list):
    mini = float(min(list))
    maxi = float(max(list))
    ret = []
    for item in list:
        ret.append((float(item) - mini) / (maxi - mini))
    return ret


def denormalize(n, list):
    return (float(n) * (float(max(list)) - float(min(list))) + float(min(list)))


def denormalizeThetas(t0, t1, km, prices):
    b = denormalize(linear(t1, t0, normalize(0, km)), prices)
    a = denormalize(linear(t1, t0, normalize(1, km)), prices) - b
    return [a, b]


def gradientDescent(x, y, iterations, learnRate):
    t0 = 0
    t1 = 1
    history = []
    j = 0
    while j < iterations:
        dt0 = 0
        dt1 = 0
        i = 0
        while i < len(x):
            dt0 += linear(t1, t0, x[i]) - y[i]
            dt1 += x[i] * (linear(t1, t0, x[i]) - y[i])
            i += 1
        t0 -= (dt0 / len(x)) * learnRate
        t1 -= (dt1 / len(x)) * learnRate
        j += 1
    return [t0, t1, history]


def parseArgs():
    args = []
    i = 1
    while i < len(sys.argv):
        args.append(sys.argv[i])
        i = i + 1
    parser = argparse.ArgumentParser(
        description='Train algorithm to estimate car price from its kilometer')
    parser.add_argument('-file', metavar='filename', default='data.csv')
    parser.add_argument('-i', metavar='iterations', type=int, default=500)
    parser.add_argument('-a', metavar='alpha', type=float,
                        default=0.5, help="learning rate")
    parser.add_argument('-graph', metavar='graphic', type=bool, default=False)
    return parser.parse_args(args)


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


def showResult(x, prices, filename, a, b):
    # plotting points as a scatter plot
    rx = round2(x)
    ry = round2(prices)
    plt.scatter(rx, ry, label="price / x", color="green", marker="*", s=30)

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


def train():
    args = parseArgs()
    file = args.file
    iterations = args.i
    learnRate = args.a

    data = getData(file)
    if data == -1:
        return -1
    x, y, head = data

    nx = normalizeList(x)
    ny = normalizeList(y)

    t0, t1, history = gradientDescent(nx, ny, iterations, learnRate)
    a, b = denormalizeThetas(t0, t1, x, y)
    print(a, b, history)
    if args.graph:
        showResult(x, y, file, a, b, head)


train()
