%{
#include <stdio.h>
#include <stdlib.h>
%}
%token ID NUM IF THEN LE GE EQ NE OR AND ELSE FOR WHILE INC DEC SWITCH CASE BREAK DEFAULT
%right '='
%left AND OR
%left '<' '>' LE GE EQ NE
%left '+''-'
%left '*''/'
%right UMINUS
%left '!'
%%

S    : ST {printf("Input accepted.\n");exit(0);};
ST   : SWITCH'('ID')''{'B'}'
      ;
B    : C
      | C D
      ;
C    : C C
      | CASE NUM':'ST1 BREAK';'
      ;
D    : DEFAULT':'ST1 BREAK';'
      | DEFAULT':'ST1
      ;
ST1  : WHILE '(' E2 ')' E ';'
      | FOR '(' E ';' E2 ';' E ')' DEF
      | IF '(' E2 ')' THEN E ';'
      | IF '(' E2 ')' THEN E ';' ELSE E ';'
      | ST1 ST1
      | E ';'
      ;
DEF  : '{' BODY '}'
      | E';'
      | ST
      |
      ;
BODY : BODY BODY
      | E ';'       
      | ST
      |            
      ;
E    : ID'='E
      | E'+'E
      | E'-'E
      | E'*'E
      | E'/'E
      | E'<'E
      | E'>'E
      | E LE E
      | E GE E
      | E EQ E
      | E NE E
      | E OR E
      | E AND E
      | INC E
      | DEC E
      | ID
      | NUM
      ;
E2  : E'<'E
      | E'>'E
      | E LE E
      | E GE E
      | E EQ E
      | E NE E
      | E OR E
      | E AND E
      | INC E
      | DEC E 
      | ID
      | NUM
      ;

%%

#include "lex.yy.c"

main()
{
  printf("Enter the exp: ");
  yyparse();
}
       