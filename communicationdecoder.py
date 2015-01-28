import logging
import matplotlib
import time
import csv
import re
import matplotlib.pyplot as plt
import numpy as np

#Quantize numbers into 0, 1, and 2 (1 is start bit, 2 is logic 1)
def classify(number):
        if number <= 4:
            number = 0
        elif 4 < number <= 6:
            number = 1
        elif 6 < number:
            number = 2
        return number

#Creates moving average, in this case with a window of 5
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
bitlist = []

counter0 = 0
counter1 = 0
counter2 = 0

startflag = 0



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
            if 10 == counter0:
                print("------ZERO------")
                if startflag == 1:
                    bitlist.append(0)
            if 30 == counter0:
                print("------ZERO------")
                counter0 = 10
                if startflag == 1:
                    bitlist.append(0)

        elif classifiednum == 1:
            counter0 = 0
            counter1 = counter1 + 1
            counter2 = 0
            if counter1 == 15:
                print("-----START BIT------")
                counter1 = 0
                startflag = 1
        elif classifiednum == 2:
            counter0 = 0
            counter1 = 0
            counter2 = counter2 + 1
            if 8 == counter2:
                print("------ONE------")
                if startflag == 1:
                    bitlist.append(1)
            if 18 == counter2:
                print("------ONE------")
                counter2 = 8
                if startflag == 1:
                    bitlist.append(1)
        if len(bitlist) == 8:
            startflag = 0
        # print("C0:",counter0,"C1",counter1,"C2",counter2)
    # print(list3)


a = np.arange(0,len(list1),1)
plt.plot(a, list1)
plt.plot(a, list2)
plt.plot(a, list3)
print(bitlist)
plt.show()
time.sleep(1)