import csv
import numpy as np
import matplotlib.pyplot as plt

categories = dict()

with open('outputfile.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if row[0] not in categories:
            categories[row[0]] = [row[1]]
        else:
            categories[row[0]].append(row[1])

for key, values in categories.iteritems():
    star_1_count = 0
    star_2_count = 0
    star_3_count = 0
    star_4_count = 0
    star_5_count = 0
    for value in values:
        if int(value[1]) == 1:
            star_1_count += 1
        elif int(value[1]) == 2:
            star_2_count += 1
        elif int(value[1]) == 3:
            star_3_count += 1
        elif int(value[1]) == 4:
            star_4_count += 1
        elif int(value[1]) == 5:
            star_5_count += 1
            
    alphab = ['1', '2', '3', '4', '5']
    frequencies = [star_1_count, star_2_count, star_3_count, star_4_count, star_5_count]

    pos = np.arange(len(alphab))
    width = 1.0     # gives histogram aspect to the bar diagram

    ax = plt.axes()
    ax.set_xticks(pos)
    ax.set_xticklabels(alphab)

    plt.bar(pos, frequencies, width, color='r')
    plt.ylabel(key);
    plt.show()
    
