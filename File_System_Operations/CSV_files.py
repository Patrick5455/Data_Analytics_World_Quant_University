# CSV files are among the simplest and most common widespread format for saving tabular data
# CSV stands for comma separated values
# each new line ina csv file is a row and each value after a comma is a column

with open('../Data/csv_sample.txt', 'r+') as f:
    csv = f.read()
# print(csv)

# we can parse this file into a table by making a list of list

list_table = []

with open('../Data/csv_sample.txt', 'r') as f:
    for line in f.readlines():
        list_table.append(line.strip().split(','))
        # .strip() strips out newline characters (\n) or extra white spaces
        # .split() split apart the strings using comma which turns each line to a list appended into the main list
        # List of lists
# print("List of Lists")
# print(list_table, end='\n\n')


import pandas as pd
import numpy as np

print("Pandas Data Frame")
print(pd.DataFrame(list_table), end='\n\n')

# print("Numpy Array")
# print(np.array(list_table))




# change numbers to int
from collections import namedtuple

Row = namedtuple('row', ['index', 'name', 'age'])


def parse_row(row):
    row = row.strip().split(',')
    for i in row:
        if i == 'index':
            return row
    return Row([int(row[0])], row[1], int(row[2]))


#    print(row)

lis = []

with open('../Data/csv_sample.txt') as f:
    for line in f:
        line = parse_row(line)
        lis.append(line)

print(lis)
#print(pd.DataFrame(lis))
#print(np.array(lis))


# reading CSV files directly with pandas
df = pd.read_csv('../Data/csv_sample.txt')
print(df)

# a major concern when working with csv file is if the file is well structured or not
# a bad csv file (not strucutred well) can lead to incorrect analysis of data
# below is an example of a bad csv

with open('../Data/bad_csv.csv') as f:
    bad = f.read()
print(bad)

badDF = pd.read_csv('../Data/bad_csv.csv')
print(badDF) # notice the NaN value