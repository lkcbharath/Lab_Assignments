import numpy as np 
import pandas as pd
from collections import defaultdict
from itertools import combinations, product, permutations

def custom_csv_import(filename,header_):
    
    data_file = filename
    data_file_delimiter = ','
    largest_column_count = 0

    with open(data_file, 'r') as temp_f:
        lines = temp_f.readlines()
        for l in lines:
            column_count = len(l.split(data_file_delimiter))
            largest_column_count = column_count if largest_column_count < column_count else largest_column_count

    temp_f.close()

    column_names = [int(i) for i in range(0, largest_column_count)]

    df = pd.read_csv(data_file, header=header_, delimiter=data_file_delimiter, names=column_names)
    return df.values

def self_join(keys,k):
    if k > 2:
        c_comb = set()
        for i in range(len(keys)):
            for j in range(i+1,len(keys)):
                c_comb_item = tuple(set(tuple(keys[i]) + tuple(keys[j])))

                
                if len(c_comb_item) == k:
                    c_comb.add(c_comb_item)

        c_comb = set(tuple(sorted(l)) for l in c_comb if l[0] != l[1])
    else:
        keys_ = [min(key) for key in keys]
        c_comb = list(combinations(keys_, k))

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
            key_ = frozenset(key)
            if cand[key_] == None:
                cand[key_] = 1
            else:
                cand[key_] += 1
            
    return cand

def compare_sup_count(freq_set, min_sup_count):
    new_dict = {key: val for key, val in freq_set.items() 
                    if (val >= min_sup_count) }
    return new_dict

def assoc_rule_mining(item_set,min_conf):
    print('Association Rule Mining and Confidence:')
    k = len(item_set)
    for i in range(1,k):
        freq_set = item_set[i]
        keys = [list(i) for i in freq_set.keys()]
        for key in keys:
            perm_keys = list(permutations(key,len(key)))

            for perm_key in perm_keys:
                for i in range(1,len(perm_key)):
                    key_ = frozenset(perm_key)
                    if_1 = frozenset(perm_key[:i])
                    then_1 = frozenset(perm_key[i:])
                    sup_if_1 = item_set[len(if_1)-1][if_1]
                    sup_key = item_set[len(key_)-1][key_]
                    conf_value = sup_key/sup_if_1
                    strong = ''
                    if conf_value > min_conf:
                        strong = ', Strong Rule'
                    rule = 'Rule: ' + '^'.join(if_1) + ' -> ' + '^'.join(then_1) + ', Confidence = ' + str(round(conf_value,4)*100) + '%' + strong
                    print(rule)

def main():

    filename = 'test_dataset_1.csv'
    header = 0

    # filename = 'retail_dataset.csv'
    # header = 'infer'
    
    ds_entries = custom_csv_import(filename, header)
    print(ds_entries)

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
    l1 = dict((frozenset([k]),v) for k,v in l1.items())
    item_set.append(l1)

    no_of_items = len(c1)

    for k in range(2,no_of_items):
        c_comb = self_join(list(item_set[-1].keys()), k)
        cand = generate_cand_set(ds_entries, c_comb, k)
        lx = compare_sup_count(cand, min_sup_count)
        if lx != {}:
            item_set.append(lx)
            
    conf = 0.75

    assoc_rule_mining(item_set,conf)


if __name__ == '__main__':
    main()
