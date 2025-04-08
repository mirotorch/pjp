grammar ProjectGrammar;

/** The start rule; begin parsing here. */
program: stat+ ;

stat
    : primitiveType IDENTIFIER (',' IDENTIFIER)* ';'    # declaration
    | 'read' expr (',' expr)* ';'                       # read
    | 'write' expr (',' expr)* ';'                      # write
    | 'if' '(' expr ')' stat ('else' stat)?             # ifElse
    | 'while' '(' expr ')' stat                         # whileLoop
    | '{' stat+ '}'                                     # block
    | expr ';'                                          # simpleExpr
    | ';'                                               # emptyStatement
    ;

expr
    : <assoc=right> IDENTIFIER '=' expr      # assignment
    | expr '||' expr                         # orExpr
    | expr '&&' expr                         # andExpr
    | '!' expr                               # notExpr
    | expr ( '==' | '!=' | '<' | '>' | '<=' | '>=' ) expr # comparison
    | expr ( '*' | '/' ) expr                # mulDiv
    | expr ( '+' | '-' ) expr                # addSub
    | '-' expr                               # unaryMinus
    | '(' expr ')'                           # parens
    | INT                                    # int
    | FLOAT                                  # float
    | BOOL                                   # bool
    | CHAR                                   # char
    | STRING                                 # string
    | IDENTIFIER                             # id
    ;

primitiveType
    : type=INT_KEYWORD
    | type=FLOAT_KEYWORD
    | type=BOOL_KEYWORD
    | type=CHAR_KEYWORD
    | type=STRING_KEYWORD
    ;

// keywords
INT_KEYWORD : 'int';
FLOAT_KEYWORD : 'float';
BOOL_KEYWORD: 'bool';
CHAR_KEYWORD: 'char';
STRING_KEYWORD: 'string';
// separators
SEMI:               ';';
COMMA:              ',';
// arithmetic operators
MUL : '*' ; 
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
// comparison operators
EQ : '==' ;
NEQ : '!=' ;
LT : '<' ;
GT : '>' ;
LTE: '<=' ;
GTE: '>=' ;
// logical operators
AND : '&&' ;
OR : '||' ;
NOT : '!' ;
// literals
BOOL: 'true' | 'false';
CHAR: '\'' ( ~['\\\r\n] | '\\' . ) '\''  ;
STRING: '"' ( ~["\\\r\n] | '\\' . )* '"'  ;
FLOAT : [0-9]+'.'[0-9]+ ;
INT : [0-9]+ ; 

IDENTIFIER : [a-zA-Z] [a-zA-Z0-9]* ;
WS : [ \t\r\n]+ -> skip ; // toss out whitespace, tab, and newline