import csv
file_rows = csv.reader(open("training_neatfile.csv", 'r',encoding='utf8',), delimiter=',', quotechar='|')
count = 0



for row in file_rows:
    count +=1
    try:
        if count > 4855:
         print(count, row[1])
    except(IndexError):
        continue
