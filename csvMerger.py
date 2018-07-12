import os
import csv

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
    print list
    return list
            
path = os.getcwd()
    
csv1 = 'CK+Converted.csv'
csv2 = 'RadboundConverted.csv'
merged = 'Merged.csv'

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
