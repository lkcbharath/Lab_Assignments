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
        self.freq_1_itemset = defaultdict(lambda: None)
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
            branches = defaultdict(lambda: None)
            for key, value in self.cond_pattern_base[pb_key].items():
                branch_id = value[1]
                if branches[branch_id] != None:
                    branches[branch_id].add((key,value[0]))
                else:
                    branches[branch_id] = set()
                    branches[branch_id].add((key,value[0]))

            self.cond_fp_tree[pb_key] = set()
            for branch_id, branch in branches.items():
                branch_dict = defaultdict(lambda: None)
                for items in branch:
                    item_value = items[1]
                    for item_key in items[0]:
                        if branch_dict[item_key] != None:
                            branch_dict[item_key] += item_value
                        else:
                            branch_dict[item_key] = item_value
                branch_dict = {k: v for k,v in branch_dict.items() if v >= min_sup}
                self.cond_fp_tree[pb_key].add(tuple(branch_dict.items()))
    
    def gen_freq_item_set(self):
        for node_key, node_cond_fp_tree in self.cond_fp_tree.items():
            items = list(set(chain(*node_cond_fp_tree)))
            dict_items = dict(items)
            item_keys = dict_items.keys()
            self.freq_itemset_gen[node_key] = set()

            for i in range(1,len(item_keys)+1):
                perm_keys = list(combinations(item_keys,i))

                for perm_key in perm_keys:
                    min_dict = {k:v for k,v in dict_items.items() if k in perm_key}
                    min_value = min(min_dict.values())
                    item_to_add = tuple(list(perm_key) + [node_key])
                    tup_to_add = (item_to_add,min_value)

                    self.freq_itemset_gen[node_key].add(tup_to_add)

    def assoc_rule_mining(self,min_conf):
        len_ = 0
        for freq_itemset in self.freq_itemset_gen.values():
            for freq_item in freq_itemset:
                if len(freq_item[0]) > len_:
                    len_ = len(freq_item[0])

        print('Association Rule Mining and Confidence:')
        item_set = [{} for i in range(len_)]
        item_set[0] = self.freq_1_itemset
        for freq_itemset in self.freq_itemset_gen.values():
            for freq_item in freq_itemset:
                index = len(freq_item[0]) - 1
                item_set[index][frozenset(freq_item[0])] = freq_item[1]

        item_set[0] = {frozenset([key]):value for key,value in item_set[0].items()}

        k = len(item_set)
        for i in range(0, k):
            freq_set = item_set[i]
            keys = [list(i) for i in freq_set.keys()]
            for key in keys:
                perm_keys = list(permutations(key, len(key)))

                for perm_key in perm_keys:
                    for i in range(1, len(perm_key)):
                        key_ = frozenset(perm_key)
                        if_1 = frozenset(perm_key[:i])
                        then_1 = frozenset(perm_key[i:])
                        sup_if_1 = item_set[len(if_1)-1][if_1]
                        sup_key = item_set[len(key_)-1][key_]
                        conf_value = sup_key/sup_if_1
                        strong = ''
                        if conf_value > min_conf:
                            strong = ', Strong Rule'
                        rule = 'Rule: ' + '^'.join(if_1) + ' -> ' + '^'.join(
                            then_1) + ', Confidence = ' + str(round(conf_value, 4)*100) + '%' + strong
                        print(rule)


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

    print('freq',freq_1_itemset)

    transactions = []

    tree = FP_Tree()

    tree.freq_1_itemset = freq_1_itemset

    for ds_entry in ds_entries:
        transaction = [item for item in ds_entry if not (pd.isnull(item))]
        transaction.sort(key=lambda x: freq_1_itemset[x],reverse=True)
        transactions.append(transaction)
        tree.insert(tree.root,transaction)

    tree.find_pattern_base(tree.root,list(),0)

    sup = 2
    tree.get_cond_fp_tree(sup)

    tree.gen_freq_item_set()
    
    min_conf = 0.75
    tree.assoc_rule_mining(min_conf)

if __name__ == '__main__':
    main()
