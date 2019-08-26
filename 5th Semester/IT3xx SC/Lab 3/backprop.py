import pandas
import numpy as np
import random
import math

def loaddata():
	data=pandas.read_csv("SPECT.csv")
	data=data.reindex(np.random.permutation(data.index))
	x=data.iloc[:,1:]
	y=data.iloc[:,0]=='Yes'
	return (x,y)

def backprop(x_train,y_train,x_test):
	l=len(x_train[0])
	hidden=5 #number of hidden layers

	n=0.05
	w1=[[random.uniform(-1,1) for i in range(l)] for j in range(hidden)]
	w2=[random.uniform(-1,1) for i in range(hidden)]

	theta1=[random.uniform(-1,1) for i in range(hidden)]
	theta2=random.uniform(-1,1)

	ip=[0]*(hidden+1)  #as 1 op node
	op=[0]*(hidden+1)

	for i in range(100):
		for j in range(len(x_train)):
			#calculating input for hidden layer
			for k in range(hidden):
				ans=0
				for x in range(len(x_train[0])):
					ans+=(w1[k][x]*x_train[j][x])
				ip[k]=ans+theta1[k]

			#Sigmoid activation function
			for k in range(hidden):
				op[k]=1/(1+math.exp(-1*ip[k]))

			#calculating input for ouput layer
			ch=0
			for k in range(hidden):
				ch+=(w2[k]*op[k])

			ip[hidden]=ch+theta2

			#calculating op for the op layer with sigmoid function
			op[hidden]=1/(1+math.exp(-1*ip[hidden]))

			#error at the op layer
			err=op[hidden]*(1-op[hidden])*(y_train[j]-op[hidden])
			error=[0]*hidden
			for k in range(hidden):
				error[k]=op[k]*(1-op[k])*err*w2[k]

			#update the weights between the hidden layer and the output
			for k in range(hidden):
				w2[k]+=(n*err*op[k])

			#update the weights between the ip layer and the hidden
			for k in range(len(x_train[0])):
				for x in range(hidden):
					w1[x][k]+=(n*error[x]*x_train[j][k])

			for k in range(hidden):
				theta1[k]+=(n*error[k])
			theta2+=(n*err)

		predictions=[0]*len(x_test)
		pin=[0]*(hidden+1)
		pop=[0]*(hidden+1)
		for j in range(len(x_test)):
			for k in range(hidden):
				ans=0
				for x in range(len(x_test[0])):
					ans+=(w1[k][x]*x_test[j][x])
				pin[k]=ans+theta1[k]
			for k in range(hidden):
				pop[k]=1/(1+math.exp(-1*pin[k]))
			ch=0
			for k in range(hidden):
				ch+=(w2[k]*pop[k])

			pin[hidden]=ch+theta2
			pop[hidden]=1/(1+math.exp(-1*pin[hidden]))
			if pop[hidden]>0:
				predictions[j]=1
			else:
				predictions[j]=0

		return predictions

def accuracy(predictions,y_test):
	corr=0
	for i in range(len(y_test)):
		if predictions[i]==y_test[i]:
			corr+=1
	return corr/len(y_test)

def recall(predictions,y_test):
	tp=0
	fn=0
	for i in range(len(y_test)):
		if y_test[i]==predictions[i] and y_test[i]==1:
			tp+=1
		if y_test[i]==0 and predictions[i]==1:
			fn+=1
	re=tp/(tp+fn)
	return re

def precision(predictions,y_test):
	tp=0
	fp=0
	for i in range(len(y_test)):
		if y_test[i]==predictions[i] and y_test[i]==1:
			tp+=1
		if y_test[i]==1 and predictions[i]==0:
			fp+=1
	pre=tp/(tp+fp)
	return pre

def main():
	x,y=loaddata()
	l = len(x) // 10
	res=[0]*10
	for i in range(10):
		x_test = x.iloc[i*l:(i+1)*l].values
		y_test = y.iloc[i*l:(i+1)*l].values
		
		if i==0:
			x_train=x.iloc[(i+1)*l:].values
			y_train=y.iloc[(i+1)*l:].values
		else:
			x_train=x.iloc[0:(i)*l].append(x.iloc[(i+1)*l:]).values
			y_train=y.iloc[0:(i)*l].append(y.iloc[(i+1)*l:]).values
		#print(len(x_train)," ",len(x_test)," ",len(x))
		predictions=backprop(x_train,y_train,x_test)
		res[i]=accuracy(predictions,y_test)


	print("For given dataset and learning rate of 0.05 :")
	print("maximum accuracy = ",max(res))
	print("average accuracy over 10 folds =  ",sum(res)/len(res))
	print("precision = ",precision(predictions,y_test))
	print("recall =  ",recall(predictions,y_test))

if __name__=='__main__':
	main()