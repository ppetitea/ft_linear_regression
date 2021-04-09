import csv


def writeData(filename, rows):
    try:
        with open(filename, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='\n')
            for row in rows:
                spamwriter.writerow(row)
    except IOError:
        print("Fail to write in file " + filename)


def importData(filename):
    rows = []
    try:
        with open(filename, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                rows.append(row)
        return rows
    except IOError:
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


def getThetas(filename):
    data = importData(filename)
    head = [0, 0]
    if len(data) > 0:
        head = data.pop(0)
    return head
