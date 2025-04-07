# Generated from lab8.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .lab8Parser import lab8Parser
else:
    from lab8Parser import lab8Parser

# This class defines a complete listener for a parse tree produced by lab8Parser.
class lab8Listener(ParseTreeListener):

    # Enter a parse tree produced by lab8Parser#program.
    def enterProgram(self, ctx:lab8Parser.ProgramContext):
        pass

    # Exit a parse tree produced by lab8Parser#program.
    def exitProgram(self, ctx:lab8Parser.ProgramContext):
        pass


    # Enter a parse tree produced by lab8Parser#declaration.
    def enterDeclaration(self, ctx:lab8Parser.DeclarationContext):
        pass

    # Exit a parse tree produced by lab8Parser#declaration.
    def exitDeclaration(self, ctx:lab8Parser.DeclarationContext):
        pass


    # Enter a parse tree produced by lab8Parser#printExpr.
    def enterPrintExpr(self, ctx:lab8Parser.PrintExprContext):
        pass

    # Exit a parse tree produced by lab8Parser#printExpr.
    def exitPrintExpr(self, ctx:lab8Parser.PrintExprContext):
        pass


    # Enter a parse tree produced by lab8Parser#parens.
    def enterParens(self, ctx:lab8Parser.ParensContext):
        pass

    # Exit a parse tree produced by lab8Parser#parens.
    def exitParens(self, ctx:lab8Parser.ParensContext):
        pass


    # Enter a parse tree produced by lab8Parser#boolean.
    def enterBoolean(self, ctx:lab8Parser.BooleanContext):
        pass

    # Exit a parse tree produced by lab8Parser#boolean.
    def exitBoolean(self, ctx:lab8Parser.BooleanContext):
        pass


    # Enter a parse tree produced by lab8Parser#string.
    def enterString(self, ctx:lab8Parser.StringContext):
        pass

    # Exit a parse tree produced by lab8Parser#string.
    def exitString(self, ctx:lab8Parser.StringContext):
        pass


    # Enter a parse tree produced by lab8Parser#assignment.
    def enterAssignment(self, ctx:lab8Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by lab8Parser#assignment.
    def exitAssignment(self, ctx:lab8Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by lab8Parser#char.
    def enterChar(self, ctx:lab8Parser.CharContext):
        pass

    # Exit a parse tree produced by lab8Parser#char.
    def exitChar(self, ctx:lab8Parser.CharContext):
        pass


    # Enter a parse tree produced by lab8Parser#addSub.
    def enterAddSub(self, ctx:lab8Parser.AddSubContext):
        pass

    # Exit a parse tree produced by lab8Parser#addSub.
    def exitAddSub(self, ctx:lab8Parser.AddSubContext):
        pass


    # Enter a parse tree produced by lab8Parser#id.
    def enterId(self, ctx:lab8Parser.IdContext):
        pass

    # Exit a parse tree produced by lab8Parser#id.
    def exitId(self, ctx:lab8Parser.IdContext):
        pass


    # Enter a parse tree produced by lab8Parser#float.
    def enterFloat(self, ctx:lab8Parser.FloatContext):
        pass

    # Exit a parse tree produced by lab8Parser#float.
    def exitFloat(self, ctx:lab8Parser.FloatContext):
        pass


    # Enter a parse tree produced by lab8Parser#int.
    def enterInt(self, ctx:lab8Parser.IntContext):
        pass

    # Exit a parse tree produced by lab8Parser#int.
    def exitInt(self, ctx:lab8Parser.IntContext):
        pass


    # Enter a parse tree produced by lab8Parser#mulDiv.
    def enterMulDiv(self, ctx:lab8Parser.MulDivContext):
        pass

    # Exit a parse tree produced by lab8Parser#mulDiv.
    def exitMulDiv(self, ctx:lab8Parser.MulDivContext):
        pass


    # Enter a parse tree produced by lab8Parser#primitiveType.
    def enterPrimitiveType(self, ctx:lab8Parser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by lab8Parser#primitiveType.
    def exitPrimitiveType(self, ctx:lab8Parser.PrimitiveTypeContext):
        pass



del lab8Parser