# install pygal and lxml packages before running this code
# This program takes a 3 column dirty csv (with some &"% symbols etc), cleans it, saves it to a new clean csv and graphs it.

import pygal
import lxml
import csv
import re


############### CLEANING FUNCTION

# "valu" should be a string going into the function to get cleaned
def clean_stuff(valu):
    valu = re.sub('[-.!@#$]', '', valu)  # re sub out symbols
    valu = re.sub('Mr', '', valu)  # re sub out Mr
    valu = re.sub(' points', '', valu)  # re sub out single space
    valu = re.sub(' ', '', valu)  # re sub out single space
    return valu  # send it back all sqeaky clean


############### OPENING FILE AND TURNING COLUMNS INTO A BIG LIST

f = open("cleaned.csv", newline='')  # this is the file we will get dirty data from
reader = csv.reader(f)

# header = next(reader)

dataListed = [row for row in reader]  # turns the data into a bit list

############### COUNTING HOW MANY ROWS TO IN CSV TO SET LIMITS LATER ON

# Counts how many rows in the csv file. We'll need this later to limit loops.
row_count = sum(1 for row in dataListed)
print("number of rows is", row_count)

############### SENDING COLUMNS AWAY TO THE CLEANING FUNCTION BE CLEANED (FOR 3 COLUMNS X,Y and Z)

print("Here is the original list of dirty data..")
print(dataListed, "\n\n")

print("Here is the cleaned up list that will be written to the new csv and/or graphed")

xValuesList = []
## need to get a single x element (single word) from the big list using dataListed[0][0]
## clean it using a function clean_stuff(valu)
## add it to the x list
## make a for loop to do this for all x values in range row_count

for i in range(row_count):  # stop at the end of the last row
    valu = dataListed[i][0]  # [0][0] is the first point. [1][0] is next down etc.
    cleanxVal = clean_stuff(valu)  # send it to the cleaners
    xValuesList.append(cleanxVal)  # take it back and add it to our final xValuesList

print(xValuesList)

yValuesList = []
## need to get a single y element (single word) from the big list using dataListed[0][1]
## clean it using a function clean_stuff(valu)
## add it to the y list
## make a for loop to do this for all x values in range row_count

for i in range(row_count):  # stop at the end of the last row
    valu = dataListed[i][2]  # [0][1] is the first y point. [1][1] is next down etc
    cleanyVal = clean_stuff(valu)  # send it to the cleaners
    yValuesList.append(cleanyVal)  # take it back and add it to our final yValuesList

print(yValuesList)

zValuesList = []
for i in range(row_count):  # stop at the end of the last row
    valu = dataListed[i][2]  # [0][1] is the first y point. [1][1] is next down etc
    cleanyVal = clean_stuff(valu)  # send it to the cleaners
    zValuesList.append(cleanyVal)  # take it back and add it to our final yValuesList

print(zValuesList)

f.close()

################################# WRITE THE CLEANED COLUMNS TO A NEW CLEAN CSV FILE


######################### PREPARE COLUMNS FOR GRAPHING BY ADDING THEM INTO LISTS OF COLUMN 1 vs. COLUMN 2 etc


# series name = [[int(first column of data), int(second column of data)] for column in reader]
# REMEMBER: column[0] is the first column, column[1] is the second etc.

######## FOR COLUMNS 1 and 2


# opens the csv
f = open("cleaned.csv", newline='')
reader = csv.reader(f)
# makes a list from the first and second columns
dataListedSeriesA = [[float(column[0]), float(column[1])] for column in reader]
f.close()

######## FOR COLUMNS 1 and 3

# opens the csv
f = open("cleaned.csv", newline='')
reader = csv.reader(f)
# makes a list from the first and third columns
dataListedSeriesB = [[float(column[0]), float(column[2])] for column in reader]
f.close()

# you have to close the file between reading each series, no idea why.


############################################# GRAPHING IN PYGAL

disChart = pygal.XY(stroke=False)

# chart title
disChart.title = 'Correlation (The large numbers have all been divided by 100,000)\n(Small Decimals have been multiplied by 100,000)'

# disChart.add('Series Name', [lists of data points])
disChart.add('% of World Population', dataListedSeriesA)
disChart.add('Actors in that percentage', dataListedSeriesB)

# save top a vector graphics file
disChart.render_to_file('chart.svg')

# show in your browser
disChart.render_in_browser()

"""
The csv used for this example:

2013,4,5
2014,6,7
2015,8,8
2016,11,9
2017,15,10
"""
