#include <stdio.h>
#include <math.h>

void main()
{
double p,r,t,s,c;
printf("Enter Principal\n");
scanf("%lf",&p);
printf("Enter Rate per year\n");
scanf("%lf",&r);
printf("Enter No of years\n");
scanf("%lf",&t);
s = (p*r*t)/100;
c = p*pow((1+(r/100)),t) - p;
printf("Simple interest is %lf\n",s);
printf("Comp interest is %lf",c);
}
