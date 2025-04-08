from antlr4 import *
from antlr_gen.ProjectGrammarLexer import ProjectGrammarLexer
from antlr_gen.ProjectGrammarParser import ProjectGrammarParser
from TypeChecker import TypeChecker

input_stream = FileStream("input.txt", encoding="utf-8")
lexer = ProjectGrammarLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ProjectGrammarParser(token_stream)

tree = parser.program()
print(tree.toStringTree(recog=parser))
checker = TypeChecker()
checker.visit(tree)