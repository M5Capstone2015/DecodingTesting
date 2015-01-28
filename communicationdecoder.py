import logging
import matplotlib
import time
import csv
import re
import matplotlib.pyplot as plt
import numpy as np
import collections


def classify(number):
        if number <= 4:
            number = 0
        elif 4 < number <= 6:
            number = 1
        elif 6 < number:
            number = 2
        return number

def movingaverage(lst,window):
    averagelist=[]
    for i, item in enumerate(lst):
        try:
            sums = 0;
            average = 0;
            for number in range(0,window):
                sums = sums + lst[i+number]
            average = sums / window
            averagelist.append(average)
        except IndexError:
            averagelist.append(list1[i])
    return averagelist

list1 = []
list2 = []
list3 = []

counter0 = 0
counter1 = 0
counter2 = 0
flag0 = 0
flag00 = 0
flag1 = 0
flag2 = 0
flag22 = 0

def resetflags():
    flag0 = 0
    flag00 = 0
    flag2 = 0
    flag22 = 0



print("test")
with open('hijack_dump.csv', 'rt') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        x= (', '.join(row))
        if x is not '':
            list1.append(int(x))

    list2=movingaverage(list1,5)
    print(list2)




    for i, item in enumerate(list2):
        classifiednum = classify(list2[i])
        list3.append(classifiednum)
        if classifiednum == 0:
            # if counter1 > 0 or counter2 > 0:
            #    resetflags()
            counter0 = counter0 + 1
            counter1 = 0
            counter2 = 0
            if 12 == counter0:
                print("------ZERO------")
            elif 21 ==counter0:
                print("------ZERO---")
        elif classifiednum == 1:
            counter0 = 0
            counter1 = counter1 + 1
            counter2 = 0
            if counter1 == 25:
                print("-----START BIT------")
                counter1 = 0
        elif classifiednum == 2:
            if counter0 > 0 or counter1 >0:
               resetflags()
            counter0 = 0
            counter1 = 0
            counter2 = counter2 + 1
            if 12 == counter2:
                print("------ONE------")
            elif 24 == counter2:
                print("------ONE---")
        # print("C0:",counter0,"C1",counter1,"C2",counter2)
    # print(list3)


a = np.arange(0,len(list1),1)
plt.plot(a, list1)
plt.plot(a, list2)
plt.plot(a, list3)
plt.show()
time.sleep(1)