import statistics
import csv

# opens the csv
f = open("tempcovData.csv", newline='')
reader = csv.reader(f)
next(reader, None)
#skips header

CovidNo = [[float(column[2])] for column in reader]
#Selects the column with covid numbers
f.close()

try:
    Covmode = statistics.mode(CovidNo)
    print("The Mode is ", Covmode)

except:
    print("Spain without the S. -_-")
