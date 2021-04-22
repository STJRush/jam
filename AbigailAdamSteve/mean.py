import statistics
import csv


f = open("tempcovData.csv", newline='')
reader = csv.reader(f)


dataListedSeriesA = [int(column[1]) for column in reader]
print(dataListedSeriesA)

xValuesMean = statistics.mean(dataListedSeriesA)
print("The mean is ", xValuesMean)







