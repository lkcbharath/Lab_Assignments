# Thanks to Rashad Ahmed for this code

import csv
import math
import random


def train(rows, features, test_set):

	yes_string = 'Iris-setosa'
	no_string = 'Iris-versicolor'


	averages = [0 for i in range(len(features)-1)]
	for i in range(0, len(features)-1):
		for j in range(len(test_set)):
			averages[i] += float(test_set[j][i])
		averages[i] = str(averages[i]/len(test_set))

	n_yes = 0
	n_no = 0
	for i in range(len(rows)):
		if rows[i][-1] == yes_string:
			n_yes += 1
		if rows[i][-1] == no_string:
			n_no += 1

	prob_yes = float(n_yes)/(n_yes+n_no)
	prob_no = float(n_no)/(n_yes+n_no)

	f1_yes = [0]*(len(features)-1)
	f1_no = [0]*(len(features)-1)
	f0_no = [0]*(len(features)-1)
	f0_yes = [0]*(len(features)-1)

	for j in range(len(rows)):
		for i in range(0, len(features)-1):
			if rows[j][i] >= averages[i] and rows[j][-1] == yes_string:
				f1_yes[i] += 1
			elif rows[j][i] >= averages[i] and rows[j][-1] == no_string:
				f1_no[i] += 1
			elif rows[j][i] < averages[i] and rows[j][-1] == yes_string:
				f0_yes[i] += 1
			elif rows[j][i] < averages[i] and rows[j][-1] == no_string:
				f0_no[i] += 1

	for i in range(len(f1_yes)):
		f1_no[i] = f1_no[i]/float(n_no)
		f1_yes[i] = f1_yes[i]/float(n_yes)
		f0_no[i] = f0_no[i]/float(n_no)
		f0_yes[i] = f0_yes[i]/float(n_yes)

	accuracy = 0

	for j in range(len(test_set)):
		yes_p = prob_yes
		no_p = prob_no
		for i in range(0, len(features)-1):
			if test_set[j][i] <= averages[i]:
				yes_p *= f0_yes[i]
				no_p *= f0_no[i]
			else:
				yes_p *= f1_yes[i]
				no_p *= f1_no[i]

		if yes_p > no_p:
			max_prob = yes_string
		else:
			max_prob = no_string

		if test_set[j][-1] == max_prob:
			accuracy += 1
	result = float(accuracy)/len(test_set)
	result *= 100
	return result


def fold(dataset, i, k):
	l = len(dataset)
	start_index_test = l*(i-1)//k
	end_index_test = l*i//k
	if start_index_test == 0:
		start_index_train = end_index_test
		end_index_train = l
		return [dataset[start_index_train:end_index_train], dataset[start_index_test:end_index_test]]
	elif end_index_test == l:
		start_index_train = 0
		end_index_train = start_index_test
		return [dataset[start_index_train:end_index_train], dataset[start_index_test:end_index_test]]
	else:
		start_index_train_first = 0
		end_index_train_first = start_index_test
		start_index_train_second = end_index_test
		end_index_train_second = l
		new_dataset = []
		for i in range(start_index_test):
			new_dataset.append(dataset[i])
		for j in range(end_index_test, l):
			new_dataset.append(dataset[j])

		return [new_dataset, dataset[start_index_test:end_index_test]]


def main():
	filename = 'IRIS.csv'
	features = []
	rows = []
	with open(filename, 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		features = csvreader.next()
		for row in csvreader:
			rows.append(row)
	k = 10
	accuracies = []
	avg_acc = 0.0

	random.shuffle(rows)

	for i in range(1, k+1):
		after_fold = fold(rows, i, k)
		train_set = after_fold[0]
		test_set = after_fold[1]
		acc = train(train_set, features, test_set)
		accuracies.append(acc)
		random.shuffle(accuracies)

	j = 0
	for acc in accuracies:
		j += 1
		print('Accuracy of fold ' + str(j) + ': ' + str(math.ceil(acc)))
		avg_acc = avg_acc + float(math.ceil(acc))
	avg_acc = avg_acc/10
	print
	print("Average accuracy is " + str(avg_acc))


if __name__ == '__main__':
	main()
