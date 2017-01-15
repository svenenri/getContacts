import csv

labels = []

with open("us-500.csv", "rU") as csvfile:
	info = csv.reader(csvfile)

	header = csv.Sniffer().has_header("csvfile")

	if header == True:
		labels = csvfile.next()
		labels = labels.replace("\n", "")
		labels = labels.replace("\"", "")
		labels = labels.split(",", 11)

	for people in info:
		print people[0], people[1]
		for i in range(len(people)):
			print labels[i] + ": " + people[i]
		print "---------------"

"""
To Do List:
1. Parse out "" in lables **COMPLETE**
2. for "web in labels, parse out \n "(the : and URL show on a new line) **COMPLETE**
3. Implement use of dictionaries
3. Create functions:
	- def fileOpen(file)
	- def labelMaker(csvfile)
	_ printInfo(info = csv.reader(csvFile))
"""
