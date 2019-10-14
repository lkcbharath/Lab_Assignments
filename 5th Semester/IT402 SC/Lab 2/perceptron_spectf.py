import random
import math

def predict(row,weights):
    res = weights[0]
    for i in range(1,len(row)):
        res += (row[i]*weights[i])

    if res > 1000:
        return 1
    else:
        return 0

def multilayer_perceptron(train_set,n_attr,test_set):
    weights = [random.uniform(0,1) for i in range(n_attr+1)]
    learning_rate = 0.01
    iterations = 0
    error_count = 0

    # training model
    while (iterations < 10):
        # print(iterations,weights)
        old_error_count = error_count
        error_count = 0
        
        for row in train_set:
            z = int(row[-1])
            y = predict(row,weights)

            error = z-y
            error_count += abs(error)

            if abs(error) > 0:
                weights[-1] += learning_rate*error
                for i in range(1,n_attr):
                    weights[i] += learning_rate*error*weights[i]*row[i]
        
        if (error_count == 0):
            break

        if (old_error_count == error_count):
            iterations += 1
        
    # testing model
    
    acc = 0
    for row in test_set:
        z = row[-1]
        y = predict(row,weights)

        error = abs(z-y)

        if error == 0:
            acc += 1
    
    return (acc/len(test_set))*100


def cross_validation_split(dataset,n_folds):
    dataset_split = []
    dataset_copy = list(dataset)
    fold_size = int(len(dataset)/n_folds)
    for i in range(n_folds):
        fold = []
        while len(fold) < fold_size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split

def main():
    filename = 'SPECTF.csv'
    attributes = []
    rows = []
    with open(filename,'r') as file:
        len_attributes = 0
        i = 0
        for line in file:
            if (i==0):
                i = 1
                continue
            row_ = line.split(',')

            if(len_attributes==0):
                len_attributes = len(row_) - 1
            
            if row_[0]=='Yes':
                row_[0] = '0.0'
            else:
                row_[0] = '1.0'
            row_ = row_[1:] + [row_[0]]
            row = [float(x) for x in row_]
            rows.append(row)
    # Number of folds
    k = 10
    accuracy = []
    avg_acc = 0.0
    folds = cross_validation_split(rows,k)
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set,[])
        test_set = []
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)

        acc = multilayer_perceptron(train_set,len_attributes,test_set)
        accuracy.append(acc)

    print('\n\nThe Accuracy for each fold is as follows : ')
    for i in accuracy:
        print(math.ceil(i), end=',')
        avg_acc = avg_acc + float(math.ceil(i))
    
    avg_acc = avg_acc/10
    print("\n\nAverage accuracy is " + str(avg_acc))

if __name__ == '__main__':
	main()
