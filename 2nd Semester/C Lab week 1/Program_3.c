#include <stdio.h>

void main()
{
int roll;
double sub1,sub2,sub3,tot,avg;
printf("Enter your roll no:\n");
scanf("%d",&roll);
printf("Enter marks of Subject 1\n");
scanf("%lf",&sub1);
printf("Enter marks of Subject 2\n");
scanf("%lf",&sub2);
printf("Enter marks of Subject 3\n");
scanf("%lf",&sub3);

tot = sub1+sub2+sub3;
avg = tot/3;

printf("Your roll number is %d",roll);
printf("\nYour total marks are %lf",tot);
printf("\nYour average mark is %lf",avg);
}
