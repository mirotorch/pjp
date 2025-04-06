grammar ProjectGrammar;

/** The start rule; begin parsing here. */
prog: stat+;

stat: ';'                                   // empty statement
    | TYPE ID (',' ID)*                     // variable declaration
    | expr ';'                              // evaluate expression
    | 'read' expr (',' expr)* '\r\n'        // read statement
    | 'write' expr (',' expr)* '\r\n'       // write statement
    | '{' stat+ '}'                         // block statement
    | 'if' '(' cond ')' stat ('else' stat)? // if-else statement
    | 'while' '(' cond ')' stat             // while loop
    ;

cond: expr ('==' | '!=' | '<' | '>' | '<=' | '>=') expr ; // condition expression

expr: expr ('+'|'-'|'*'|'/'|'%') expr  
    ;


TYPE: 'int' | 'float' | 'bool' | 'string' ; // match types
ID: [a-zA-Z_][a-zA-Z0-9_]* ;                // match variable names

// literals
STRING : "[a-zA-Z]+" ;      // match strings TODO
INT : [0-9]+ ;              // match integers
FLOAT: [0-9]+ '.' [0-9]+ ;  // match floats
BOOLEAN: 'true' | 'false' ; // match booleans

// skip newlines, whitespaces, tabs and comments
DELIMITER: [ \r\n]+ | [' ']+ | [\t]+ | '//' ~[\r\n]* -> skip ; 