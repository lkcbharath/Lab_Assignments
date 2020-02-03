import numpy as np 
import pandas as pd
from collections import defaultdict
from itertools import combinations, product

def custom_csv_import(filename,header_):
    
    data_file = filename
    data_file_delimiter = ','
    largest_column_count = 0

    with open(data_file, 'r') as temp_f:
        lines = temp_f.readlines()
        for l in lines:
            column_count = len(l.split(data_file_delimiter)) + 1
            largest_column_count = column_count if largest_column_count < column_count else largest_column_count

    temp_f.close()

    column_names = [i for i in range(0, largest_column_count)]

    df = pd.read_csv(data_file, header=header_, delimiter=data_file_delimiter, names=column_names)
    return df.values

def main():

    filename = 'Test.csv'
    header = None

    ds_entries = custom_csv_import(filename, header)
    print(ds_entries)


if __name__ == '__main__':
    main()
