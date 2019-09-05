
%{ 
    #include <stdio.h>
    int count_comm = 0;
    int count_id=0; 
    int i=0;
%} 


%% 
.*\/\/.*    				{count_comm++;printf("\t\b\b\b\b");}
.*(int\ ).*(\;)				{	for (i=0;i<yyleng;i++){if (yytext[i]==',') count_id++;} count_id++;printf("\t\b\b\b\b");}
.*(char\ ).*(\;)			{	for (i=0;i<yyleng;i++){if (yytext[i]==',') count_id++;} count_id++;printf("\t\b\b\b\b");}
.*(float\ ).*(\;)			{	for (i=0;i<yyleng;i++){if (yytext[i]==',') count_id++;} count_id++;printf("\t\b\b\b\b");}
.*(double\ ).*(\;)			{	for (i=0;i<yyleng;i++){if (yytext[i]==',') count_id++;} count_id++;printf("\t\b\b\b\b");}
%% 

int yywrap(){} 

int main(){ 
    yyin=fopen("testing_4.txt","r");

    yylex(); 

    printf("\nNo. of single comment lines: %d\n\n",count_comm);
    printf("\nNo. of identifiers: %d\n\n",count_id);
    
    return 0; 
} 
