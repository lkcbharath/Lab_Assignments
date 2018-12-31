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

for(i=0;i<n;i++)
{

if (i==(n-1))
{
j++;
i=j;
}

if (a[i]>a[i+1])                                                // swapping (bubble sort)
{
t = a[i];
a[i]=a[i+1];
a[i+1] = t;
}

                                                           //increment
}

printf("Sorted Array is:\n");
for(i=0;i<n;i++)                                                //output
printf("%d ",a[i]);
}

