"""
cfile
    : LCOMMENT
    | BCOMMENT
    | MACRO
    | extern_var_declare
    | extern_var_define
    | var_declare
    | var_define
    | function_declare
    | function_define
    ;

extern_var_declare
    : 'extern' type IDENT SEMI
    ;

extern_var_define
    : 'extern' type IDENT ASSIGN constant SEMI
    ;

function_declare
    : type IDENT LP (param_list)? RP SEMI
    ;

var_declare
    : type IDENT SEMI
    | type IDENT LB CONST_INT RB SEMI
    ;

var_define
    : type IDENT ASSIGN constant SEMI
    | type IDENT LB CONST_INT RB ASSIGN LCB (constant (COMMA constant)*) RCB SEMI
    ;

function_define
    : type IDENT LP (param_list)? RP LCB statement* RCB
    ;

call_function
    : IDENT LP (expression (COMMA expression)*)? RP
    ;

param_list
    : param (COMMA param)*
    ;

param
    : type IDENT
    | type IDENT LB RB
    ;

statement
    : LCOMMENT
    | BCOMMENT
    | assignment
    | if_statement
    | if_else_statement
    | while_statement
    | for_statement
    | return_statement
    | break_statement
    | continue_statement
    | function_declare
    | call_function SEMI
    | var_declare
    | var_define
    ;

assignment
    : IDENT ASSIGN expression SEMI
    | IDENT LB expression RB ASSIGN expression SEMI
    | IDENT ASSIGN call_function SEMI
    ;

if_statement
    : IF LP condition RP statement
    | IF LP condition RP LCB statement* RCB
    ;

if_else_statement
    : IF LP condition RP statement ELSE statement
    | IF LP condition RP LCB statement* RCB ELSE LCB statement* RCB
    | IF LP condition RP LCB statement* RCB ELSE if_statement
    ;

while_statement
    : WHILE LP condition RP statement
    | WHILE LP condition RP LCB statement* RCB
    ;

for_statement
    : FOR LP (assignment|var_declare)? SEMI condition? SEMI (assignment)? RP statement
    | FOR LP (assignment|var_declare)? SEMI condition? SEMI (assignment)? RP LCB statement* RCB
    ;

return_statement
    : RETURN SEMI
    | RETURN IDENT SEMI
    | RETURN constant SEMI
    | RETURN expression SEMI
    | RETURN call_function SEMI
    ;

break_statement
    : BREAK SEMI
    ;

continue_statement
    : CONTINUE SEMI
    ;

condition
    : expression
    ;

type
    : INT
    | FLOAT
    | CHAR
    | LONG
    | SHORT
    | VOID
    ;

constant
    : CONST_INT
    | CONST_FLOAT
    | CONST_CHAR
    ;

expression
    : constant
    | IDENT
    | IDENT LB expression RB
    | call_function
    | Lp expression RP
    | expression MUL|DIV|REMAINER expression
    | expression PLUS|SUB expression
    | expression GREATER|LESS|GREATEREQ|LESSEQ expression
    | expression EQ|NEQ expression
    | expression AND expression
    | expression OR expression

"""
