%{
    #include<stdio.h>
	int count = 0;
%}

%%
([0-9]|[a-zA-z])*ab {count++;}
[\n] {printf("Count= %d\n",count);count=0;}
%%

int main()
{
    yylex();
    return 0;
}