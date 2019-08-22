%{ 
    int i,n;
    char c;
%} 
  
%% 
scanf {
    printf("readf");
}
printf {
    printf("writef");
}
%% 
  
int yywrap(void){} 

int main(int argc, char **argv[]) 
{ 
    yylex(); 
    return 0; 
} 