#include <stdio.h>

void main()
{
int i,j,n,min;
printf("Enter length of array\n");//Input
scanf("%d",&n);
int a[n];
printf("Enter characters in array\n");
for (i=0;i<n;i++)
scanf("%d",&a[i]);
i=0;
min = i;
for(i=0;i<n;i++)        //Selection
{
    for (j=i;j<n;j++)
    {
        if (a[min]>a[j])
        min = j;
    }
    j = i;
    for (j=i;j<n;j++)
    {
        if (a[min]!=a[j])
        {
        a[min] = a[j]*a[min];
        a[j] = a[min]/a[j];
        a[min] = a[min]/a[j];
        }

    }

}
i=0;
printf("The given array is now ");
for (i=0;i<n;i++)           //Output
printf("%d ",a[i]);
}
