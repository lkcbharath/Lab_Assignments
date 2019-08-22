%{ 
    int i,n;
    char c;
%} 
  
%% 
[a-z] {
    for(i=0;yytext[i]!='\0';++i){
        c = yytext[i] + 5;
        printf("%c",c);
    }
}
%% 
  
int yywrap(void){} 

int main() 
{ 
    printf("Enter the string of vowels and consonents:"); 
    yylex(); 
    return 0; 
} 