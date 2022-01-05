import csv
# import numpy as np

#dados.csv

with open('dados.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    # for row in spamreader:
    #     print(', '.join(row))
    bsb =[]
    for row in reader:
        probe = str(reader['PROBE'])
        if probe == 'BRASILIA':
            bsb = bsb + row
