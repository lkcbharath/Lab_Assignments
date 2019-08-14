#Naive Bayes algorithm in python
import csv
def loadfile(fil):
	lines=csv.reader(open(fil, "r"))
	dataset=list(lines)
	#print(dataset)
	#print("\n\n")
	dataset.pop(0)
	for i in range(len(dataset)):
		if dataset[i][0]=="Yes":
			dataset[i][0]=1
		else:
			dataset[i][0]=0
	#print(dataset)
	for i in range(len(dataset)):
		dataset[i]=[int(x) for x in dataset[i]]
	#print(dataset)
	return dataset

def splitlist(li,k):
	n=len(li)
	kl=n//k
	#print(k)
	l=[None]*k
	a=0
	b=kl
	for i in range(k-1):
		#print("a ",a,"b ",b)
		l[i]=li[a:b]
		a=b
		b=b+kl
	l[k-1]=li[a:]

	return l

def calprob(a,li):
	kl=[None]*2
	global cor_count
	global false_count
	#print(li)
	n=len(li[0][0])
	kl[0]=[0,0]#yes list
	kl[0][0]=[0]*n  #list of probablity 0/yes
	kl[0][1]=[0]*n#1/yes
	kl[1]=[0,0]#no list
	kl[1][0]=[0]*n#0/no
	kl[1][1]=[0]*n#1/no
	#print(kl)
	yes=0
	no=0
	for i in range(10):
		if i==a:
			continue
		for j in range(len(li[i])):
			if li[i][j][0]==0:
				no+=1
			else:
				yes+=1
			ar=li[i][j]
			for m in range(len(ar)):
				if m==0:
					continue
				if ar[m]==0 and ar[0]==1:
					kl[0][0][m]+=1
				elif ar[m]==0 and ar[0]==0:
					kl[1][0][m]+=1
				elif ar[m]==1 and ar[0]==1:
					kl[0][1][m]+=1
				else:
					kl[1][1][m]+=1
	cmpli=li[a]
	#print(yes,"   ",no)
	for i in range(len(cmpli)):
		py=yes/(yes+no)
		pn=no/(yes+no)
		for j in range(len(cmpli[i])):
			if j==0:
				continue
			if cmpli[i][j]==0:
				py=py*kl[0][0][j]/yes
				pn=pn*kl[1][0][j]/no
			else:
				py=py*kl[0][1][j]/yes
				pn=pn*kl[1][1][j]/no
		proby=py/(py+pn)
		probn=pn/(py+pn)
		#print(proby," No : ",proby,"pn: ",pn,"py: ",py)
		if proby>=probn:
			cor_count+=1
		else:
			false_count+=1
	#print(kl)
	#print("Correct count: ",cor_count," false_count:",false_count)
	return kl





cor_count=0
false_count=0
def main():
	fil="SPECT.csv"
	li=loadfile(fil)# To store the contents of the file into a list
	#print(li)
	#for i in li:
	#	print(i)
	#print(len(li))
	calli=splitlist(li,10)# To split the existing list into ten folds
	for i in range(10):
		kl=calprob(i,calli)
		#calaccuracy(li,i,kl)
	print("Total Correct count = ",cor_count,"  False count = ",false_count)
main()
