import os
import csv

AN = 0
DI = 0
FE = 0
HA = 0
SA = 0
SU = 0
NE = 0

csv1 = 'RadboundConverted.csv'

print(csv1)

#with open(csv1, 'rb') as fr:
with open(csv1, newline='') as fr: #python3
    reader1 = csv.reader(fr)
    #param1 = reader1.next()
    next(reader1) #python3
    for row in reader1:
        if row[0] == '0':
            AN = AN+1
        elif row[0] == '1':
            DI = DI+1
        elif row[0] == '2':
            FE = FE+1
        elif row[0] == '3':
            HA = HA+1
        elif row[0] == '4':
            SA = SA+1
        elif row[0] == '5':
            SU = SU+1
        elif row[0] == '6':
            NE = NE+1

print('Angry: '+str(AN)+'\nDisgusted: '+str(DI)+'\nFearful: '+str(FE)+'\nHappy: '+str(HA)+'\nSad: '+str(SA)+'\nSurprised: '+str(SU)+'\nNeutral: '+str(NE))
