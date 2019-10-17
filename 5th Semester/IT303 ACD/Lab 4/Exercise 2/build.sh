#!/bin/sh

lex ex2.l
yacc ex2.y
cc y.tab.c -ly -ll -lm
./a.out