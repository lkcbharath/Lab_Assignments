alpha [A-Za-z]
digit [0-9]
%%


[ \t\n]
[sS][eE][lL][eE][cC][tT]                    return SELECT;
[dD][iI][sS][tT][iI][nN][cC][tT]            return DISTINCT;
[fF][rR][oO][mM]                            return FROM;
[wW][hH][eE][rR][eE]                        return WHERE;
[lL][iI][kK][eE]                            return LIKE;
[dD][eE][sS][cC]                            return DESC;
[aA][sS][cC]                                return ASC;
[gG][rR][oO][uU][pP].[bB][yY]               return GROUP;
[hH][aA][vV][iI][nN][gG]                    return HAVING;
[oO][rR][dD][eE][rR].[bB][yY]               return ORDER;
[oO][rR]                                    return OR;
[aA][nN][dD]                                return AND;
[iI][nN][nN][eE][rR].[jJ][oO][iI][nN]       return INNER;
[oO][uU][tT][eE][rR].[jJ][oO][iI][nN]       return OUTER;
[lL][eE][fF][tT].[jJ][oO][iI][nN]           return LEFT;
[rR][iI][gG][hH][tT].[jJ][oO][iI][nN]       return RIGHT;
[oO][nN]                                    return ON;
{digit}+                                    return NUM;
{alpha}({alpha}|{digit}|\.)*                return ID;
"<="                                        return LE;
">="                                        return GE;
"=="                                        return EQ;
"!="                                        return NE;
.                                           return yytext[0];

%%