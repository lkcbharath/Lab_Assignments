import numpy as np 
import pandas as pd
from collections import defaultdict

class Node:
    
    def __init__(self, item_name, item_count):
        self.item = [item_name, item_count]
        self.children = defaultdict(lambda: None)

class FP_Tree:

    def __init__(self):
        self.root = Node(None,None)

    def insert(self,node,transaction):

        if transaction == []:
            return

        item = transaction[0]
        node_ = node.children[item]

        if node_ != None:
            node_.item[1] += 1
        else:
            node_ = Node(item, 1)
            node.children[item] = node_
        
        self.insert(node_, transaction[1:])


def custom_csv_import(filename, header_):

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

    df = pd.read_csv(data_file, header=header_,
                     delimiter=data_file_delimiter, names=column_names)
    return df.values


def main():

    filename = 'test_dataset_1.csv'
    header = None

    # filename = 'retail_dataset.csv'
    # header = 'infer'

    ds_entries = custom_csv_import(filename, header)

    freq_1_itemset = dict()

    for ds_entry in ds_entries:
        for value in ds_entry:
            if value in freq_1_itemset.keys(): 
                freq_1_itemset[value] += 1
            else:
                freq_1_itemset[value] = 1

    freq_1_itemset.pop(np.nan, None)

    transactions = []


    tree = FP_Tree()


    for ds_entry in ds_entries:
        transaction = [item for item in ds_entry if not (pd.isnull(item))]
        transaction.sort(key=lambda x: freq_1_itemset[x],reverse=True)
        transactions.append(transaction)
        tree.insert(tree.root,transaction)

    # print(transactions)

    # tree.insert(tree.root, transactions[0])
    print(tree.root.children[transaction[0]].children['I1'].item)

    

if __name__ == '__main__':
    main()
