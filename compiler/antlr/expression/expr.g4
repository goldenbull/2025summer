grammar expr;

prog
    : stat+ EOF
    ;

stat
    : expr '\n'
    | assignment '\n'
    | '\n'
    ;

expr
    : '(' expr ')'
    | expr ('*'|'/') expr
    | expr ('+'|'-') expr
    | INT
    | ID
    ;

assignment
    : ID '=' expr
    ;

ID
    : [a-zA-Z]+
    ;

INT
    : [0-9]+
    ;

WS
    : [\r\t ]+ -> skip
    ;