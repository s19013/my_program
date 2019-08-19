import csv

test_file=open('test.csv')
test_reader=csv.reader(test_file)
test_date=list(test_reader)
print(test_date[0][0])
print(test_date[0][1])
print(test_date[0][2])
print(test_date[1])
print(test_date[2])
