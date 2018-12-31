#include <stdio.h>

void main()
{
double x1,x2,y1,y2,d;
printf("Enter x coordinate of position 1\n");
scanf("%lf",&x1);
printf("Enter y coordinate of position 1\n");
scanf("%lf",&y1);
printf("Enter x coordinate of position 2\n");
scanf("%lf",&x2);
printf("Enter y coordinate of position 2\n");
scanf("%lf",&y2);

d = sqrt(pow((x2-x1),2) + pow((y2-y1),2));
printf("Distance between coordinates is %lf", d);
}



