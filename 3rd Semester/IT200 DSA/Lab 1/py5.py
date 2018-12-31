print("Enter 10 numbers")
a=[]

for i in range(0,10):
    d = int(input())
    a.append(d)

for i in range(0,9):
    for j in range(0,9-i):
        if a[j]>a[j+1]:
            b = a[j]
            a[j] = a[j+1]
            a[j+1] = b

print("The new set of numbers after sorting is:",a)




