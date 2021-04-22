import pygal
import csv

f = open("TempCovid - Sheet1.csv", newline = '')
#opens the csv
reader = csv.reader(f)
next(reader, None)
#makes a list from the second and third columns
dataListedSeriesA = [[float(column[1]), float(column[2])] for column in reader]
#makes a list from the second and third columns
f.close()
#closes the csv

disChart = pygal.XY(stroke=False)

disChart.title = 'Correlation'
#graphtitle

#disChart.add('Series Name', [lists of data points])
disChart.add('A', dataListedSeriesA)

#save top a vector graphics file
disChart.render_to_file('chart.svg')

#show in your bcolumnser
disChart.render_in_browser()