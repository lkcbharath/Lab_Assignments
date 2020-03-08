import numpy as np
import pandas as pd
from collections import defaultdict
from itertools import permutations, combinations


def custom_csv_import(filename, header_):

    data_file = filename
    data_file_delimiter = ','

    df = pd.read_csv(data_file, delimiter=data_file_delimiter)
    return df


def main():
    filename = 'Test.csv'
    header = 'infer'

    dataset_frame = custom_csv_import(filename, header)

    print('Original Bit Vector:')
    print(dataset_frame)

    min_sup = 2
    min_card = 2

    print('\nMinimum Support: ', min_sup)
    print('Minimum Cardinality: ', min_card)

    min_sup_card_satisfied = False

    while not min_sup_card_satisfied:

        min_sup_card_satisfied = True

        remove_indices = []
        for index, row in dataset_frame.iterrows():
            card = row.sum()
            if card < min_card:
                min_sup_card_satisfied = False
                remove_indices.append(index)

        dataset_frame = dataset_frame.drop(remove_indices, axis=0)
        
        remove_indices = []
        for index, column in dataset_frame.iteritems():
            sup = column.sum()
            if sup < min_sup:
                min_sup_card_satisfied = False
                remove_indices.append(index)
        
        dataset_frame = dataset_frame.drop(remove_indices, axis=1)

    print('\nPreprocessed Bit Vector:')
    print(dataset_frame)
    print()

    column_indices = list(dataset_frame.index)
    column_indices_combinations = []

    for i in range(1, column_indices[-1]+1):
        column_indices_combinations += list(combinations(column_indices,i))

    for indices in column_indices_combinations:
        selected_dataset_frame = dataset_frame.iloc[list(indices)]

        len_rows = len(selected_dataset_frame)
        selected_indices = []
        bit_vector = ""
        for index, column in selected_dataset_frame.iteritems():
            if sum(column) == len_rows:
                selected_indices.append(index)
                bit_vector += '1'
            else:
                bit_vector += '0'
                
        card = len(selected_indices)
        if card > min_card:
            indices_string = ', '.join([str(i) for i in indices])
            feature_string = ', '.join(selected_indices)
            print('Enumerated rows: (' + indices_string + '); Features: ' + feature_string + '; Bit Vector: ' + bit_vector)

if __name__ == '__main__':
    main()
