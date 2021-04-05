import random
import csv
import sys
import argparse


def writeData(filename, rows):
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='\n')
        for row in rows:
            spamwriter.writerow(row)


def rand(n):
    return (random.random() * (2 * n)) - n


def addNoise(n, noise):
    return n + rand(noise)


def generateDataSet(size, noise, a, b, wtf):
    rows = [["km", "price"]]
    i = 0
    while i < size:
        x = rand(size) if wtf else addNoise(i * 3, noise)
        y = rand(size) if wtf else addNoise(a * x + b, noise)
        rows.append([x, y])
        i = i + 1
    return rows


def parseArgs():
    args = []
    i = 1
    while i < len(sys.argv):
        args.append(sys.argv[i])
        i = i + 1
    parser = argparse.ArgumentParser(
        description='Generate random dataset for linear regression algorythm')
    parser.add_argument('-file', metavar='filename', default='data.csv')
    parser.add_argument('-wtf', metavar='bool', type=bool, default=False)
    parser.add_argument('-size', metavar='number', type=int, default=100)
    parser.add_argument('-noise', metavar='number', type=int, default=100)
    parser.add_argument('-a', metavar='number', type=int)
    parser.add_argument('-b', metavar='number', type=int)
    return parser.parse_args(args)


def generator():
    args = parseArgs()
    filename = args.file
    wtf = args.wtf
    size = args.size
    noise = args.noise
    a = args.a if args.a else rand(10)
    b = args.b if args.b else rand(1000)
    data = generateDataSet(size, noise, a, b, wtf)
    writeData(filename, data)


generator()
