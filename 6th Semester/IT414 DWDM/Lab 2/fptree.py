import numpy as np 
import pandas as pd
from collections import defaultdict
from itertools import permutations,chain,combinations

class Node:
    
    def __init__(self, item_name, item_count, item_id):
        self.item = [item_name, item_count, item_id]
        self.parent = None
        self.children = defaultdict(lambda: None)

class FP_Tree:

    def __init__(self):
        self.global_id_count = 0
        self.root = Node(None,None,0)
        self.cond_pattern_base = defaultdict(lambda: None)
        self.cond_fp_tree = defaultdict(lambda: None)
        self.freq_itemset_gen = defaultdict(lambda: None)

    def insert(self,node,transaction):

        if transaction == []:
            return

        item = transaction[0]
        node_ = node.children[item]

        if node_ != None:
            node_.item[1] += 1
        else:
            self.global_id_count += 1
            node_ = Node(item, 1, self.global_id_count)
            node_.parent = node
            node.children[item] = node_
        
        self.insert(node_, transaction[1:])
    
    def find_pattern_base(self,node,items,branch_no):
        items_ = items[::]

        if node.item[0] != None:
            items_ += [node.item[0]]

        # Non-root entries only
        if node.item[0] != None and len(items) > 0:

            if node.item[0] not in self.cond_pattern_base.keys():
                self.cond_pattern_base[node.item[0]] = defaultdict(lambda: None)
            
            pattern_base_item = self.cond_pattern_base[node.item[0]]

            pattern_base = frozenset(items)

            if pattern_base in pattern_base_item.keys():
                pattern_base_item[pattern_base][0] += node.item[1]
            else:
                pattern_base_item[pattern_base] = [node.item[1], branch_no]

        if node.item[0] == None:
            i = 0
            for node_key, node_ref in node.children.items():
                self.find_pattern_base(node_ref, items_, i)
                i += 1
        else:
            for node_key, node_ref in node.children.items():
                self.find_pattern_base(node_ref,items_, branch_no)
    
    def get_cond_fp_tree(self,min_sup):
        keys = list(self.cond_pattern_base.keys())
        for pb_key in keys:
            # branches = set([value[1] for value in self.cond_pattern_base[key].values()])
            branches = defaultdict(lambda: None)
            # branch_ids = set([value[1] for value in self.cond_pattern_base[key].values()])
            # print(branches)
            for key, value in self.cond_pattern_base[pb_key].items():
                # print(key,value,pb_key)
                branch_id = value[1]
                if branches[branch_id] != None:
                    branches[branch_id].add((key,value[0]))
                else:
                    branches[branch_id] = set()
                    branches[branch_id].add((key,value[0]))
                # branches[value[1]] = []

            # self.cond_fp_tree[min(key)] = branches
            self.cond_fp_tree[pb_key] = set()
            for branch_id, branch in branches.items():
                branch_dict = defaultdict(lambda: None)
                # print(pb_key, branch_id, branch, 'test')
                for items in branch:
                    # print(items)
                    item_value = items[1]
                    for item_key in items[0]:
                        # print(item_key)
                        if branch_dict[item_key] != None:
                            branch_dict[item_key] += item_value
                        else:
                            branch_dict[item_key] = item_value
                # print(branch_dict)
                branch_dict = {k: v for k,v in branch_dict.items() if v >= min_sup}
                # print(pb_key, branch_id, branch_dict)
                # print(pb_key)
                self.cond_fp_tree[pb_key].add(tuple(branch_dict.items()))

    
    def gen_freq_item_set(self):
        for node_key, node_cond_fp_tree in self.cond_fp_tree.items():
            # items = list(node_cond_fp_tree.keys()) + [node_key]
            # items = [' '.join(tups) for tups in node_cond_fp_tree]
            # print(node_cond_fp_tree)
            items = list(set(chain(*node_cond_fp_tree)))
            dict_items = dict(items)
            item_keys = dict_items.keys()
            # print(node_key, item_keys)
            self.freq_itemset_gen[node_key] = set()

            # print(dict_items)

            for i in range(1,len(item_keys)+1):
                # print(item_keys)
                perm_keys = list(combinations(item_keys,i))

                # print(perm_keys)
                for perm_key in perm_keys:
                    min_dict = {k:v for k,v in dict_items.items() if k in perm_key}
                    min_value = min(min_dict.values())
                    # print(perm_key,min_value)
                    item_to_add = tuple(list(perm_key) + [node_key])
                    tup_to_add = (item_to_add,min_value)

                    self.freq_itemset_gen[node_key].add(tup_to_add)

def custom_csv_import(filename, header_):

    data_file = filename
    data_file_delimiter = ','
    largest_column_count = 0

    with open(data_file, 'r') as temp_f:
        lines = temp_f.readlines()
        for l in lines:
            column_count = len(l.split(data_file_delimiter))
            largest_column_count = column_count if largest_column_count < column_count else largest_column_count

    temp_f.close()

    column_names = [i for i in range(0, largest_column_count)]

    df = pd.read_csv(data_file, header=header_,
                     delimiter=data_file_delimiter, names=column_names)
    return df.values


def main():

    filename = 'test_dataset_1.csv'
    header = 0

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

    tree.find_pattern_base(tree.root,list(),0)

    sup = 2
    tree.get_cond_fp_tree(sup)

    tree.gen_freq_item_set()

    for key, value in tree.freq_itemset_gen.items():
        print(key,value)

if __name__ == '__main__':
    main()
