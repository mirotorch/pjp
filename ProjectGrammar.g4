grammar ProjectGrammar;

/** The start rule; begin parsing here. */
program: stat+ ;

stat
    : primitiveType IDENTIFIER (',' IDENTIFIER)* ';'    # declaration
    | 'read' expr (',' expr)* ';'                       # read
    | 'write' expr (',' expr)* ';'                      # write
    | 'fwrite' IDENTIFIER (',' expr)* ';'               # fileWrite
    | 'if' '(' expr ')' stat ('else' stat)?             # ifElse
    | 'while' '(' expr ')' stat                         # whileLoops
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
    | expr ('%') expr                        # modExpr
    | '-' expr                               # unaryMinus
    | expr '.' expr                          # concatExpr
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
    | type=FILE_KEYWORD
    ;

// keywords
INT_KEYWORD : 'int';
FLOAT_KEYWORD : 'float';
BOOL_KEYWORD: 'bool';
CHAR_KEYWORD: 'char';
STRING_KEYWORD: 'string';
FILE_KEYWORD: 'FILE';
// separators
SEMI:               ';';
COMMA:              ',';
// arithmetic operators
MUL : '*' ; 
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
MOD: '%' ;
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
// other operators
CONCAT: '.' ;
// literals
BOOL: 'true' | 'false';
CHAR: '\'' ( ~['\\\r\n] | '\\' . ) '\''  ;
STRING: '"' ( ~["\\\r\n] | '\\' . )* '"'  ;
FLOAT : [0-9]+'.'[0-9]+ ;
INT : [0-9]+ ; 

IDENTIFIER : [a-zA-Z] [a-zA-Z0-9]* ;
WS : [ \t\r\n]+ -> skip ; // toss out whitespace, tab, and newline