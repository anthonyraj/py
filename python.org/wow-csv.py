import csv

FILE='eggs.csv'
with open(FILE) as csvfile:
	dataReader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in dataReader:
		print ' | '.join(row)
