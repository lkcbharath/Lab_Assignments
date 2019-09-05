%{
	int count = 0;
%}

%%
.*ab" "|.*ab[\n] {count++;}
\n {printf("count= %d\n",count);count=0;}
%%

int main()
{
    yylex();
    
    return 0;
}