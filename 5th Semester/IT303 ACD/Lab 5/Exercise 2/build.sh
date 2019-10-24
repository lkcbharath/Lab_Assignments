#!/bin/sh

lex ex2.l
yacc -d ex2.y
gcc lex.yy.c y.tab.c -ll
./a.out
