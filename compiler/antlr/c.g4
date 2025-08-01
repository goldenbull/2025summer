grammar C;

cfile
    : LineComment
    | BlockComment
    | macro
    | extern_var_declare
    | var_declare
    | var_define
    | function_declare
    | function_define
    ;

macro
    : '#' 'define' IDENT constant
    | '#' 'include' '<' .* '>'
    ;

function_define
    : type IDENT '(' parameterList ')' '{' statement* '}'
    ;

type
    : intType
    | floatType
    ;

intType
    : baseIntType
    | 'unsigned' baseIntType
    ;

baseIntType
    : 'char'
    | 'short'
    | 'int'
    | 'long'
    ;

floatType
    : 'float'
    | 'double'
    ;

parameterList
    : param (',' param)*
    ;

param
    : type IDENT
    ;

statement
    : var_declare
    | var_define
    | assginment
    | ifStatement
    | whileStatement
    | forStatement
    | returnStatement
    | functionCallStatement
    ;

var_declare
    : type IDENT ';'
    | type IDENT '[' INT ']' ';'
    ;

var_define
    : type IDENT '=' constant ';'
    | type IDENT '[' INT ']' '=' '{' constant (',' constant)* '}' ';'
    ;

constant
    : INT
    | FLOAT
    ;

IDENT
    : [_a-zA-Z] [_a-zA-Z0-9]*
    ;

INT
    : [0-9]+
    | '0x' [0-9a-fA-F]+
    | 123L 123l
    | 'a' char
    ;

FLOAT
    : 1.23
    | 1.0e-23 1e23
    ;

BlockComment
    : '/*' .*? '*/' -> skip
    ;

LineComment
    : '//' ~[\r\n]* -> skip
    ;
