import statistics
import csv

f = open("TempCovid - Sheet1.csv", newline = '')
#opens the csv
reader = csv.reader(f)
next(reader, None)
#skips header

CovidNo = [[float(column[1])] for column in reader]
#Selects the column with covid numbers
f.close()
#closes the csv
  
x = statistics.median(CovidNo)
#gets the median of the numbers

print("The Median Number of Covid Cases is:", x)
#tells you the median
