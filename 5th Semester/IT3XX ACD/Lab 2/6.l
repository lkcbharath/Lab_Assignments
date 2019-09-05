%{
	#include<stdio.h>
	int flag=0;
%}

%%
(and)|(or)|(thus)|(but)|(yet)|(so)|(because) {flag=1;}
[\n] {if(flag==1) printf("\nCompound sentence\n");
	else printf("\nSimple sentence\n");}
%%

int yywrap(void){} 

int main()
{
	printf("Enter the sentence: ");
	yylex();
	return 0;
}