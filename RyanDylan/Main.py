# Install pygal and lxml packages before running this code
import pygal
import csv

# Turning pairs of columns into x,y series for graphing
######################################################

# Series name = [[int(first column of data), int(second column of data)] for column in reader]
# REMEMBER: column[0] is the first column, column[1] is the second etc.

# Opens the csv
f = open("Clean Data.csv", newline = '')
reader = csv.reader(f)
# Makes a list from the first and second columns
dataListedSeriesA = [[int(column[0]), int(column[1])] for column in reader]
f.close()

# Repeat for Series B
f = open("Clean Data.csv", newline = '')
reader = csv.reader(f)
dataListedSeriesB = [[int(column[0]), int(column[2])] for column in reader]
f.close()

# You have to close the file between reading each series, no idea why.

# Graphing the series using pygal

disChart = pygal.XY(stroke=False)

# Chart title
disChart.title = 'Unemployment vs. Covid in Ireland'

# disChart.add('Series Name', [lists of data points])
disChart.add('Covid Cases', dataListedSeriesA)
disChart.add('Total Unemployed', dataListedSeriesB)

# Save top a vector graphics file
disChart.render_to_file('Graphed Data.svg')

# Show in your browser
disChart.render_in_browser()
