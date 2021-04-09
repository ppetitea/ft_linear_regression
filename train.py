import argparse
import sys
from data import getData, writeData
from graph import showResult
from quality import quality


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
    return [t0, t1]


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
    parser.add_argument('-r2', metavar='quality indicator',
                        type=bool, default=False)
    return parser.parse_args(args)


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

    t0, t1 = gradientDescent(nx, ny, iterations, learnRate)
    a, b = denormalizeThetas(t0, t1, x, y)
    writeData("thetas.csv", [[b, a]])
    print(a, b)
    if args.r2:
        quality(x, y, a, b)
    if args.graph:
        showResult(x, y, file, a, b, head)


train()
