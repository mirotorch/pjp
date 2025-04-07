grammar lab8;

/** The start rule; begin parsing here. */
program: statement+ ;

statement
    : primitiveType IDENTIFIER (',' IDENTIFIER)* ';' # declaration
    | expr ';'                                       # printExpr
    ;

expr: expr op=(MUL|DIV) expr                # mulDiv
    | expr op=(ADD|SUB) expr                # addSub
    | INT                                   # int
    | IDENTIFIER                            # id
    | FLOAT                                 # float
    | BOOL                                  # boolean
    | CHAR                                  # char
    | STRING                                # string
    | '(' expr ')'                          # parens
    | <assoc=right> IDENTIFIER '=' expr     # assignment
    ;

primitiveType
    : type=INT_KEYWORD
    | type=FLOAT_KEYWORD
    | type=BOOL_KEYWORD
    | type=CHAR_KEYWORD
    | type=STRING_KEYWORD
    ;


INT_KEYWORD : 'int';
FLOAT_KEYWORD : 'float';
BOOL_KEYWORD: 'bool';
CHAR_KEYWORD: 'char';
STRING_KEYWORD: 'string';
SEMI:               ';';
COMMA:              ',';
MUL : '*' ; 
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
BOOL: 'true' | 'false';
CHAR: '\'' ( ~['\\\r\n] | '\\' . ) '\''  ;
STRING: '"' ( ~["\\\r\n] | '\\' . )* '"'  ;
FLOAT : [0-9]+'.'[0-9]+ ;
INT : [0-9]+ ; 
IDENTIFIER : [a-zA-Z]+ ; 
WS : [ \t\r\n]+ -> skip ; // toss out whitespace