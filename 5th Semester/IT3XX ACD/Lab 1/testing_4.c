#include <stdio.h>
//Program begins
int main()
{
	int a,b,c;
	char d,e,f;
	float g;
	double y;
	// Inputting elements;
	scanf("%d", &a);
	b = 2;
	c = 5;
	a = b + c;
	d = a + 'a';
	g = b/a;

	// Output
	printf("%f %c %lf",g,d,y);
	return 0;
	// Program termination
}