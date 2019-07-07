import csv

def writetocsv(values, filename):
    csvfile = open(filename, "a", newline="")
    writer = csv.writer(csvfile)
    writer.writerow(values)
    csvfile.close