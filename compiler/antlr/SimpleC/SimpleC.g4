grammar SimpleC;

prog : topElement* EOF ;

topElement
    : BlockComment
    | LineComment
    | MACRO
    | extern_var_declare
    | extern_var_define
    | var_declare
    | var_define
    | function_declare
    | function_define
    ;

extern_var_declare
    : EXTERN type IDENT SEMI
    ;

extern_var_define
    : EXTERN type IDENT ASSIGN constant SEMI
    ;

var_declare
    : type IDENT SEMI
    | type IDENT LB CONST_INT RB SEMI
    ;

var_define
    : type IDENT ASSIGN constant SEMI
    | type IDENT LB CONST_INT RB ASSIGN LCB arrayInitValueList? RCB SEMI
    ;

arrayInitValueList
    : constant (COMMA constant)*
    ;

function_declare
    : retType IDENT LP param_list? RP SEMI
    ;

function_define
    : retType IDENT LP param_list? RP LCB statement* RCB
    ;

retType
    : type
    | VOID
    ;

param_list
    : param (COMMA param)*
    | VOID
    ;

param
    : type IDENT
    | type IDENT LB RB
    ;

type
    : INT
    | FLOAT
    | CHAR
    | LONG
    | SHORT
    ;

constant
    : CONST_INT
    | CONST_FLOAT
    | CONST_CHAR
    | CONST_LONG
    ;

statement
    : var_declare
    | var_define
    | assignment
    | if_statement
    | if_else_statement
    | while_statement
    | for_statement
    | break_statement
    | continue_statement
    | function_statement
    | return_statement
    ;

assignment
    : IDENT ASSIGN expression SEMI
    | IDENT LB expression RB ASSIGN expression SEMI
    ;

if_statement
    : IF LP expression RP statementBlock
    ;

if_else_statement
    : IF LP expression RP statementBlock ELSE statementBlock
    ;

while_statement
    : WHILE LP expression RP statementBlock
    ;

for_statement
    : FOR LP forExpr RP statementBlock
    ;

forExpr
    : (assignment|var_define)? SEMI expression? SEMI assignment?
    ;

break_statement
    : BREAK SEMI
    ;

continue_statement
    : CONTINUE SEMI
    ;

function_statement
    : function_call SEMI
    ;

return_statement
    : RETURN SEMI
    | RETURN expression SEMI
    ;

statementBlock
    : LCB statement* RCB
    | statement
    ;

function_call
    : IDENT LP expressionList? RP
    ;

expressionList
    : expression (COMMA expression)*
    ;

expression
    : LP expression RP
    | IDENT LB expression RB
    | function_call
    | expression MUL|DIV|REMAINDER expression
    | expression ADD|SUB expression
    | expression GREATER|LESS|GREATEREQ|LESSEQ expression
    | expression EQ|NEQ expression
    | expression AND expression
    | expression OR expression
    | constant
    | IDENT
    ;


INT : 'int' ;
FLOAT : 'float' ;
LONG : 'long' ;
SHORT : 'short' ;
CHAR : 'char' ;
IF : 'if' ;
ELSE : 'else' ;
WHILE : 'while' ;
FOR : 'for' ;
VOID : 'void' ;
BREAK : 'break' ;
CONTINUE : 'continue' ;
RETURN : 'return' ;
EXTERN : 'extern' ;
LP : '(' ;
RP : ')' ;
LB : '[' ;
RB : ']' ;
LCB : '{' ;
RCB : '}' ;
SEMI : ';' ;
COMMA : ',' ;
COLON : ':' ;
ADD : '+' ;
SUB : '-' ;
MUL : '*' ;
DIV : '/' ;
REMAINDER : '%' ;
GREATER : '>' ;
LESS : '<' ;
ASSIGN : '=' ;
EQ : '==' ;
GREATEREQ : '>=' ;
LESSEQ : '<=' ;
NEQ : '!=' ;
AND : '&&' ;
OR : '||' ;

IDENT : [_a-zA-Z] [_a-zA-Z0-9]* ;
CONST_INT : [0-9]+ ;
CONST_FLOAT : [0-9]+ '.' [0-9]+ ;
CONST_CHAR : '\'' ~[\\] '\'' ;
CONST_LONG : [0-9]+ [lL] ;

BlockComment : '/*' .*? '*/' -> skip ;
LineComment : '//' ~[\r\n]* -> skip ;
MACRO : '#' ~[\r\n]* -> skip ;