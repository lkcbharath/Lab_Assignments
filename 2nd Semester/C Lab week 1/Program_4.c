#include <stdio.h>

void main()
{
double BP,DA,HRA,GP;
printf("Enter your Basic Pay (BP)\n");
scanf("%lf",&BP);
DA = 0.4*BP;
HRA = 0.2*BP;
GP = BP+DA+HRA;
printf("Your gross pay (GP) is %lf", GP);
}
