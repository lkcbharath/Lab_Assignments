#include <stdio.h>

void main()
{
int i,j,n;
printf("Enter length of array\n");//Input
scanf("%d",&n);
int a[n];
printf("Enter characters in array\n");
for (i=0;i<n;i++)
{
    scanf("%d",&a[i]);
}
i=0;
for(i=0;i<(n-1);i++)        //Linear sort
{
    for (j=0;j<(n-1-i);j++)
    {
        if (a[j]>a[j+1])
        {
        a[j+1] = a[j] * a[j+1];
        a[j] = a[j+1]/a[j];
        a[j+1] = a[j+1]/a[j];
        }

    }
}
i=0;
printf("The given array is now ");
for (i=0;i<n;i++)           //Output
printf("%d ",a[i]);
}
