%{
#include <stdio.h>
#include <string.h>
#ifndef YYSTYPE
#define YYSTYPE char*
#endif
#define INTEGER 288
extern YYSTYPE yylval;
extern FILE* yyin; 
void yyerror (const char *str);
int yylex(void);
%}

%token 
    KEY_INTEGER
    KEY_BEGIN
    KEY_END

    NUMBER 
    IDENTIFIER 
     
    OPERATION 
    SEMICOLON 
    COMMA 
    SIGN
    MINUS
    OBRACKET 
    EBRACKET
    PLUS

%left PLUS MINUS
%left OPERATION
%left UNARY

%%
PROGRAM: 
    VARS OPS;

VARS: 
    VAR
    {
        //printf("%s",$1);
    } |
    VARS VAR
    {
        //printf("%s",$2);
    };

VAR: 
    KEY_INTEGER IDS 
    {
        printf("%s", "Var ");
        printf("%s", $2);
        printf("%s", " : ");
        printf("%s", $1);
        printf("\n");
    };

IDS: 
	IDENTIFIER |
	IDS COMMA IDENTIFIER
    {
        $$ = strcat($1,"; ");
        $$ = strcat($$,$3);
    };

OPS:
    KEY_BEGIN LISTASSIGMENTS KEY_END
    {
        printf("%s", $1);	
        printf("\n%s", $2);	
    	printf("%s", $3);
        printf(".\n");
    };

LISTASSIGMENTS:
	ASSIGMENT
    {
        $$=$1;
    } |
	ASSIGMENT LISTASSIGMENTS
    {   
        $$=strcat($1,$2);
    };

ASSIGMENT:
	IDENTIFIER SIGN EXPRESSION SEMICOLON
    {
        $$ = strcat($1," := ");
        $$ = strcat($$,$3);
        $$ = strcat($$,"\n");
    };

EXPRESSION:
	MINUS SUB %prec UNARY
    {
        $$ = strcat($1,$2);	
    } | 
    SUB;

SUB:	
    OBRACKET EXPRESSION EBRACKET
    {
        $$ = strcat($1,$2);
        $$ = strcat($$,$3);	
    } | 
    OPERAND | 
    SUB OPERATION SUB 
    {   
        $$ = strcat($1,$2);
        $$ = strcat($$,$3);	
    } |
    SUB PLUS SUB
    {
        $$ = strcat($1,$2);
        $$ = strcat($$,$3);	
    } |
    SUB MINUS SUB
    {
        $$ = strcat($1,$2);
        $$ = strcat($$,$3);	    
    };

OPERAND:
	IDENTIFIER |
    NUMBER;
%%

void yyerror (const char *str)
{
	fprintf(stderr,"error: %s\n",str);
}

int main()
{
    yyin = fopen("prog.txt","r"); 
	yyparse();
	fclose(yyin);
	return 0; 
}
