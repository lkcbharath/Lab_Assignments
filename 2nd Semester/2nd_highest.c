# include <stdio.h>
void main()
{
int n,x1,x2,i,input;
printf("Enter number of inputs\n");
scanf("%d",&n);
printf("Enter the inputs\n");
scanf("%d",&x1);
x2=x1;
for(i=1;i<n;i++)
{
scanf("%d",&input);
if (x2<input && x1>input)
    x2 = input;
else if (x1<input)
    x1 = input;
}
printf("Highest and second highest are %d %d",x1,x2);
}
