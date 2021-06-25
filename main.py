import csv
data = []

with open ("Dataset2.csv", 'r')as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
planetdata = data[1:]
for i in planetdata:
    i[2] = i[2].lower()
planetdata.sort(key = lambda planetdata:planetdata[2])

with open("dataset_2_sorted.csv", "a+")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)