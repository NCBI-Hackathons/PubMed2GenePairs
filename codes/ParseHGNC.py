#!/usr/bin/python3

import sys, csv

input_file = sys.argv[1]
output_file = sys.argv[2]

csv_f = csv.reader(open(input_file, "r"), delimiter='\t')
csv_w = csv.writer(open(output_file, "w"), delimiter='\t')

header = next(csv_f)

for row in csv_f:
    all_symbols = [row[1]]
    all_names = [row[2]]
    if len(row[8]) > 1:
        all_symbols.extend(row[8].split("|"))
    if len(row[10]) > 1:
        all_symbols.extend(row[10].split("|"))
    if len(row[9]) > 1:
        all_names.extend(row[9].split("|"))
    if len(row[11]) > 1:
        all_names.extend(row[11].split("|"))
    WriteRow = [row[0], all_symbols, all_names]
    csv_w.writerow(WriteRow)
    next(csv_f)
