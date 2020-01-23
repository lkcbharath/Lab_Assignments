import numpy as np 
import pandas as pd

def self_join():
    pass

def main():
    dataset = pd.read_csv('test_dataset_1.csv')
    ds_values = dataset.values
    print(ds_values.shape)

if __name__ == '__main__':
    main()