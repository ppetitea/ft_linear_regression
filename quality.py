from data import getData


def average(array):
    sum = 0
    for n in array:
        sum += n
    return sum / len(array)


def estim(a, b, x):
    return a * x + b


def variance(x, y, a, b, yAverage):
    varianceEstim = 0
    varianceReal = 0
    i = 0
    while i < len(x):
        varianceEstim += (y[i] - estim(a, b, x[i])) ** 2
        varianceReal += (y[i] - yAverage) ** 2
        i += 1
        return (1 - (varianceEstim / varianceReal))


def quality(x, y, a, b):
    yAverage = average(y)
    print(variance(x, y, a, b, yAverage))
