# Generated from lab8.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .lab8Parser import lab8Parser
else:
    from lab8Parser import lab8Parser

# This class defines a complete generic visitor for a parse tree produced by lab8Parser.

class lab8Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by lab8Parser#program.
    def visitProgram(self, ctx:lab8Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lab8Parser#declaration.
    def visitDeclaration(self, ctx:lab8Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lab8Parser#printExpr.
    def visitPrintExpr(self, ctx:lab8Parser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lab8Parser#parens.
    def visitParens(self, ctx:lab8Parser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lab8Parser#boolean.
    def visitBoolean(self, ctx:lab8Parser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lab8Parser#string.
    def visitString(self, ctx:lab8Parser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lab8Parser#assignment.
    def visitAssignment(self, ctx:lab8Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lab8Parser#char.
    def visitChar(self, ctx:lab8Parser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lab8Parser#addSub.
    def visitAddSub(self, ctx:lab8Parser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lab8Parser#id.
    def visitId(self, ctx:lab8Parser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lab8Parser#float.
    def visitFloat(self, ctx:lab8Parser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lab8Parser#int.
    def visitInt(self, ctx:lab8Parser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lab8Parser#mulDiv.
    def visitMulDiv(self, ctx:lab8Parser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lab8Parser#primitiveType.
    def visitPrimitiveType(self, ctx:lab8Parser.PrimitiveTypeContext):
        return self.visitChildren(ctx)



del lab8Parser