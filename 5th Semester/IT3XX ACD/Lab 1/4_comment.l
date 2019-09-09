%{ 
    #include <stdio.h>
    int comments_n = 0;
    int identifier_n=0; 
    int i=0;
%} 

%% 
.*\/\/.*    				{comments_n++;printf("(Here is a comment)");}
.*(int\ ).*(\;)				{for (i=0;i<yyleng;i++){if (yytext[i]==',') identifier_n++;} identifier_n++;printf("(Here is an int identifier(s))");}
.*(char\ ).*(\;)			{for (i=0;i<yyleng;i++){if (yytext[i]==',') identifier_n++;} identifier_n++;printf("(Here is an char identifier(s))");}
.*(float\ ).*(\;)			{for (i=0;i<yyleng;i++){if (yytext[i]==',') identifier_n++;} identifier_n++;printf("(Here is an float identifier(s))");}
.*(double\ ).*(\;)			{for (i=0;i<yyleng;i++){if (yytext[i]==',') identifier_n++;} identifier_n++;printf("(Here is an double identifier(s))");}
%% 

int yywrap(void){} 

int main(){ 
    yyin=fopen("testing_4.c","r");
    yylex(); 
    printf("\nNo. of single comment lines: %d\n\n",comments_n);
    printf("\nNo. of identifiers: %d\n\n",identifier_n);
    return 0; 
} 