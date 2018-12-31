# include <stdio.h>
void main()
{
int n,i,t;
int j = 0;
int c = 0;

printf("Enter number of inputs\n");
scanf("%d",&n);
int a[n];                                                       //input
printf("Enter the inputs\n");
for(i=0;i<n;i++)
scanf("%d",&a[i]);

for(i=0;i<(n*n);i++)
{
if (j==(n-1))                                                   //to reset j
j=0;

if (a[j]>a[j+1])                                                // swapping (bubble sort)
{
t = a[j];
a[j]=a[j+1];
a[j+1] = t;
}

j++;                                                            //increment
}

printf("Sorted Array is:\n");
for(i=0;i<n;i++)                                                //output
printf("%d ",a[i]);
}

