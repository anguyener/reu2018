import os
import csv
from random import shuffle

#compares parameters, returns list of numbers, order of 2 but content is index of 1
def checkParameters(one, two):
    list = []
    n = len(one)
    for p in two:
        try:
            list.append(one.index(p))
        except ValueError:
            list.append(n)
            n=n+1
    print(list)
    return list

path = os.getcwd()

def mergeCSVs(merged, csv1, csv2):
    with open(merged, 'wb') as fw:
        writer = csv.writer(fw, delimiter=',', quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
        with open(csv1, 'rb') as fr:
            reader1 = csv.reader(fr)
            param1 = reader1.next()
            with open(csv2, 'rb') as f:
                reader2 = csv.reader(f)
                param2 = reader2.next()
                paramOrder = checkParameters(param1, param2)
                #Write new parameters in order
                r = []
                for n in range(len(paramOrder)):
                    r.append(param2[paramOrder.index(n)])
                writer.writerow(r)
                for r in reader1:
                    if not (r):
                        continue
                    if int(r[0]) >= 0: #takes care of -1 for non-recognized emotions
                        writer.writerow(r)
                for row in reader2:
                    if not (r):
                        continue
                    r = []
                    for n in range(len(paramOrder)):
                        r.append(row[paramOrder.index(n)])
                    if int(r[0]) >= 0:
                        writer.writerow(r)

def mergeAndShuffle(output, csvs):
    data = []
    header = ['emotion', 'pixels', 'svpos']
    for csv_file in csvs:
        with open(csv_file, newline='') as fr:
            csv_reader = csv.reader(fr, delimiter=',', quotechar='|')
            next(csv_reader)
            for row in csv_reader:
                data.append(row)


    shuffle(data)
    with open (output, 'w', newline='') as out:
        writer = csv.writer(out, delimiter=',', quotechar='|')
        writer.writerow(header)
        for row in data:
            writer.writerow(row)


#csvs = ['RadboundConverted.csv', 'NVIEConverted.csv', 'JAFFEConverted.csv', 'CK+Converted.csv', 'fer2013.csv']
csvs = ['RadboundConverted.csv', 'CK+Converted.csv']
output = 'Merged_RC.csv'
mergeAndShuffle(output, csvs)
#mergeCSVs('Merged.csv', 'CK+Converted.csv', 'RadboundConverted.csv')
