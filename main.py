from antlr4 import *
from antlr_gen.lab8Lexer import lab8Lexer
from antlr_gen.lab8Parser import lab8Parser
from TypeChecker import TypeChecker

input_stream = FileStream("input.txt", encoding="utf-8")
lexer = lab8Lexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = lab8Parser(token_stream)

tree = parser.program()
print(tree.toStringTree(recog=parser))
checker = TypeChecker()
checker.visit(tree)