grammar logic;

expr:  
    '(' left=expr op=opsgn right=expr ')'
    | '(' expr ')'
    | sid
    | boolExpr
    ;

opsgn:
    OP
    ;

sid:
    ID
    ;

boolExpr:
    BOOLN
    ;

BOOLN: 
    ('TRUE' | 'FALSE')
    ;

OP: 
    ('AND' | 'OR')
    ;

ID: 
    [a-z]
    ;

WS: 
    [ \r\n\t] + -> channel (HIDDEN)
   ;