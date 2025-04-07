grammar ProjectGrammar;

/** The start rule; begin parsing here. */
program: stat+ ;

stat
    : ';'                                               # emptyStatement
    | primitiveType IDENTIFIER (',' IDENTIFIER)* ';'    # declaration
    | 'read' expr (',' expr)* ';'                       # read
    | 'write' expr (',' expr)* ';'                      # write
    | 'if' '(' cond ')' stat ('else' stat)?             # ifElse
    | 'while' '(' cond ')' stat                         # whileLoop
    | '{' stat+ '}'                                     # block
    ;

cond
    : cond OR cond1       # orExpr
    | cond1               # passCond
    ;

cond1
    : cond1 AND cond2     # andExpr
    | cond2               # passCond1
    ;

cond2
    : NOT cond2           # notExpr
    | '(' cond ')'        # parensCond
    | expr relOp expr     # compare
    ;

relOp : EQ | NEQ | LT | GT | LTE | GTE ;

expr: expr op=(MUL|DIV) expr                # mulDiv
    | expr op=(ADD|SUB) expr                # addSub
    | op=SUB expr                           # unaryMinus
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