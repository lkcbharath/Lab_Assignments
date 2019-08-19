# Thanks to Rashad Ahmed for this code

import random
import math

def perceptron(train_set,n_attr,test_set):
    bias = -0.5
    weights = [random.uniform(0,1) for i in range(n_attr)]
    # delta_weights = [0.0 for i in range(n_attr)]

    learning_rate = 0.2
    iterations = 0
    error_count = -1

    while (iterations < 500) or error_count!=0:
        error_count = 0
        
        for row in train_set:
            z = row[-1]
            res = bias
            for i in range(n_attr):
                res += (row[i]*weights[i])
            
            if res>0:
                y = 1
            else:
                y = 0
            
            error = abs(z-y)
            error_count += error

            if error > 0:
                delta_weight = learning_rate*error
                weight = weight + delta_weight
    
    acc = 0

    for row in test_set:
        z = row[-1]
        res = bias
        for i in range(n_attr):
            res += (row[i]*weights[i])

        if res > 0:
            y = 1
        else:
            y = 0

        error = abs(z-y)

        if error == 0:
            acc += 1
    
    return (acc/len(test_set))*100


def fold(dataset,i,k):
    l = len(dataset)
    start_index_test = l*(i-1)//k
    end_index_test = l*i//k
    if start_index_test==0:
		start_index_train=end_index_test
		end_index_train=l
		return [dataset[start_index_train:end_index_train],dataset[start_index_test:end_index_test]]
	
    elif end_index_test==l:
		start_index_train=0
		end_index_train=start_index_test
		return [dataset[start_index_train:end_index_train],dataset[start_index_test:end_index_test]]
        
    else:
		start_index_train_first=0
		end_index_train_first=start_index_test
		start_index_train_second=end_index_test
		end_index_train_second=l
		new_dataset=[]
		for i in range(start_index_test):
			new_dataset.append(dataset[i])
		for j in range(end_index_test,l):
			new_dataset.append(dataset[j])

		return [new_dataset,dataset[start_index_test:end_index_test]]

def main():
    filename = 'SPECT.csv'
    attributes = []
    rows = []
    with open(filename,'r') as file:
        # csvreader = csv.reader(csvfile)
        # attributes = csvreader.next()
        len_attributes = len(file[0])
        for row in file:
            rows.append(row)
	k = 10
	accuracy = []
	avg_acc = 0.0

	for i in range(1,k+1):
		after_fold = fold(rows,i,k)
		train_set = after_fold[0]
		test_set = after_fold[1]
		acc = perceptron(train_set,len_attributes,test_set)
		accuracy.append(acc)

    print('The Accuracy for each fold is as follows : ')
    for i in accuracy:
		print(math.ceil(i))
		avg_acc = avg_acc + float(math.ceil(i))
    
    avg_acc = avg_acc/10
    print("Average accuracy is " + str(avg_acc))

if __name__ == '__main__':
	main()
