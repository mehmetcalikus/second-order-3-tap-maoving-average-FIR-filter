#signal and systems hw1 question 3 python code
#student name: mehmet çalıkuş  
#student id : 150150042

import csv
import copy
import matplotlib.pyplot as plt
import datetime


with open('AAPL.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    dictionary = {}
    dictionaryArray = []
    fields = []

    for row in csv_reader:
        
        if line_count == 0:
            fields = row
        else:
            column_count = 0

            for f in fields:

                if f == "Close":
                    dictionary[f] = float(row[column_count])
                elif f != "Date":
                    dictionary[f] = row[column_count]
                else:
                    dictionary[f] = datetime.datetime(int(row[column_count].split('-')[0]), int(row[column_count].split('-')[1]), int(row[column_count].split('-')[2])) 
                
                column_count += 1

            dictionaryArray.append(copy.deepcopy(dictionary))

        line_count += 1

date_1 = input("enter the first date for default(all data) press 'enter': ")
if date_1 == "":
    date_1 = datetime.datetime(2014, 3, 25)
else:
    date_1 = datetime.datetime(int(date_1.split('-')[0]), int(date_1.split('-')[1]), int(date_1.split('-')[2]))

date_2 = input("enter the second date for default(all data) press 'enter': ")
if date_2 == "":
    date_2 = datetime.datetime(2020, 3, 24)
else:
    date_2 = datetime.datetime(int(date_2.split('-')[0]), int(date_2.split('-')[1]), int(date_2.split('-')[2]))

draw_array_close = []
root_mean = 0
average = 0

for dictionary in dictionaryArray:

    if date_1 <= dictionary["Date"] and date_2 >= dictionary["Date"]:

        draw_array_close.append(dictionary["Close"])
        average = average + dictionary["Close"]
        root_mean = root_mean + dictionary["Close"]**2


average = average/len(draw_array_close)
root_mean = root_mean/len(draw_array_close)
root_mean = root_mean**0.5
standard_dev = 0

for close in draw_array_close:    
    standard_dev = standard_dev + (average - close)**2



##this part for second order 3 tap moving average filter
ThreeElementMean = 0
ThreeElementArray = []
index = 0

for close in draw_array_close:
    if index % 3 == 0:
        ThreeElementMean = ThreeElementMean + close
        ThreeElementMean = ThreeElementMean / 3
        ThreeElementArray.append(ThreeElementMean)
        ThreeElementMean = 0
    else:
        ThreeElementMean = ThreeElementMean + close
    index += 1

    
print("\nPart-1")
plt.plot(draw_array_close)
plt.ylabel('some numbers')
plt.show()


print("\n\npart-2")
print("\nmoving average FIR filtered closing price value")
plt.plot(ThreeElementArray)
plt.ylabel('some numbers')
plt.show()


standard_dev = standard_dev/(len(draw_array_close) - 1) 
standard_dev = standard_dev**0.5


print("\n\nPart-3")
print("Average : ", average)
print("Root Mean Square : ",root_mean)
print("Standard Deviation : ", standard_dev)



