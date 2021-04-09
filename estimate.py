import argparse
import sys
from data import getThetas


def parseArgs():
    args = []
    i = 1
    while i < len(sys.argv):
        args.append(sys.argv[i])
        i = i + 1
    parser = argparse.ArgumentParser(
        description='Estimate y value from x after train algorithm with dataset')
    parser.add_argument('-km', metavar='number', type=float,
                        default=-1, required=True)
    parser.add_argument('-file', metavar='filename', default='thetas.csv')
    return parser.parse_args(args)


def estimate():
    args = parseArgs()
    t0, t1 = getThetas(args.file)
    x = float(args.km)
    a = float(t1)
    b = float(t0)
    res = a * x + b
    print(res)
    return res


estimate()
