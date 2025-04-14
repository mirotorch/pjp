from antlr4 import *
from antlr_gen.ProjectGrammarLexer import ProjectGrammarLexer
from antlr_gen.ProjectGrammarParser import ProjectGrammarParser
from TypeChecker import TypeChecker


def process_file(filename):
    input_stream = FileStream(filename, encoding="utf-8")
    lexer = ProjectGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ProjectGrammarParser(token_stream)
    tree = parser.program()
    print("type checking")
    print(tree.toStringTree(recog=parser))
    checker = TypeChecker()
    checker.visit(tree)
    print("type checking done")

process_file("input_a.txt")
