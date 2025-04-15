from antlr4 import *
from antlr_gen.ProjectGrammarLexer import ProjectGrammarLexer
from antlr_gen.ProjectGrammarParser import ProjectGrammarParser
from TypeChecker import TypeChecker
from CodeGenerator import CodeGenerator
from Interpreter import Interpreter

def process_file(filename):
    input_stream = FileStream(filename, encoding="utf-8")
    lexer = ProjectGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ProjectGrammarParser(token_stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))
    print("type checking")
    checker = TypeChecker()
    checker.visit(tree)
    print("type checking done")
    generator = CodeGenerator(checker.get_types())
    try:
        generator.visit(tree)
    except Exception as e:
        print("Error during code generation:", e)
    code = generator.get_code()
    with open("instructions.txt", "w+") as file:
        file.writelines(map(lambda x: x + '\n', code))
    interpreter = Interpreter(code)
    interpreter.run()

process_file("input_a.txt")
