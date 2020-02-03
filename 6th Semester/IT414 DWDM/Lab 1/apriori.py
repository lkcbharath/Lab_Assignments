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

def self_join(keys,k):
    if k > 2:
        # c_comb = [tuple(set(key).union(key)) for key in keys]
        c_comb = set()
        for i in range(len(keys)):
            for j in range(i+1,len(keys)):
                c_comb_item = tuple(set(keys[i] + keys[j]))
                
                if len(c_comb_item) == k:
                    c_comb.add(c_comb_item)

        # c_comb = list(product(keys,keys))
        # c_comb = [''.join(x) for x in product(keys, keys)]
        # print(c_comb)
        c_comb = set(tuple(sorted(l)) for l in c_comb if l[0] != l[1])
    else:
        c_comb = list(combinations(keys, k))

    return c_comb


def set_intersect(lst1, lst2):
    final_set = set(lst1).intersection(set(lst2))
    return final_set

def generate_cand_set(ds_entries,c_comb,comb_count):
    cand = defaultdict(lambda: None)

    for ds_entry in ds_entries:
        items = [item for item in ds_entry if not (pd.isnull(item))]
        ds_entry_comb = list(combinations(list(items), comb_count))

        keys = set_intersect(c_comb, ds_entry_comb)

        for key in keys:
            if cand[key] == None:
                cand[key] = 1
            else:
                cand[key] += 1
            
    return cand

def compare_sup_count(freq_set, min_sup_count):
    new_dict = {key: val for key, val in freq_set.items() 
                    if (val >= min_sup_count) }
    return new_dict

def main():

    filename = 'test_dataset_1.csv'
    header = None

    # filename = 'retail_dataset.csv'
    # header = 'infer'
    
    ds_entries = custom_csv_import(filename, header)

    # L1,L2
    item_set = []

    min_sup_count = 2

    c1 = dict()

    for ds_entry in ds_entries:
        for value in ds_entry:
            if value in c1.keys():
                c1[value] += 1
            else:
                c1[value] = 1

    c1.pop(np.nan, None)

    l1 = compare_sup_count(c1, min_sup_count)
    item_set.append(l1)

    no_of_items = len(c1)
    # print(c1)

    for k in range(2,no_of_items):
        c_comb = self_join(list(item_set[-1].keys()), k)
        cand = generate_cand_set(ds_entries, c_comb, k)
        lx = compare_sup_count(cand, min_sup_count)
        if lx != {}:
            item_set.append(lx)
        
    print(item_set)




if __name__ == '__main__':
    main()
