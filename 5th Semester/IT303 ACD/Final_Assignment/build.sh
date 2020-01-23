#!/bin/sh

lex ex.l
yacc ex.y
gcc y.tab.c -ll -ly
./a.out