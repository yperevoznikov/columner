#! python3
import sys
import re
import pdb

# Brief validation
if len(sys.argv) != 2:
    print('Usage: columner.py <comma-separated-columns>')
    sys.exit()

# Get the column widths
lines = sys.stdin.readlines()
lines = [line.rstrip() for line in lines]
lines = [re.split(r'[ ]{3,}', line) for line in lines]
col_widths = []
for line in lines:
    for i, col in enumerate(line):
        if len(col_widths) <= i:
            col_widths.append(len(col))
        elif len(col) > col_widths[i]:
            col_widths[i] = len(col)

# Get the indexes of the columns to show
columns_to_show = [item.lower().strip() for item in sys.argv[1].split(',')]
column_indexes_to_show = []
for index, item in enumerate(lines[0]):
    if item.lower().strip() in columns_to_show:
        column_indexes_to_show.append(index)

# Print the columns
for line in lines:
    for i, col in enumerate(line):
        if i in column_indexes_to_show:
            print(col.ljust(col_widths[i] + 2), end='')
    print('\n', end='')

