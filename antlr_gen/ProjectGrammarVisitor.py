# Generated from ProjectGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ProjectGrammarParser import ProjectGrammarParser
else:
    from ProjectGrammarParser import ProjectGrammarParser

# This class defines a complete generic visitor for a parse tree produced by ProjectGrammarParser.

class ProjectGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ProjectGrammarParser#program.
    def visitProgram(self, ctx:ProjectGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#declaration.
    def visitDeclaration(self, ctx:ProjectGrammarParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#read.
    def visitRead(self, ctx:ProjectGrammarParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#write.
    def visitWrite(self, ctx:ProjectGrammarParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#fileOpen.
    def visitFileOpen(self, ctx:ProjectGrammarParser.FileOpenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#fileWrite.
    def visitFileWrite(self, ctx:ProjectGrammarParser.FileWriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#ifElse.
    def visitIfElse(self, ctx:ProjectGrammarParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#whileLoop.
    def visitWhileLoop(self, ctx:ProjectGrammarParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#block.
    def visitBlock(self, ctx:ProjectGrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#simpleExpr.
    def visitSimpleExpr(self, ctx:ProjectGrammarParser.SimpleExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#emptyStatement.
    def visitEmptyStatement(self, ctx:ProjectGrammarParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#parens.
    def visitParens(self, ctx:ProjectGrammarParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#comparison.
    def visitComparison(self, ctx:ProjectGrammarParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#bool.
    def visitBool(self, ctx:ProjectGrammarParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#string.
    def visitString(self, ctx:ProjectGrammarParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#modExpr.
    def visitModExpr(self, ctx:ProjectGrammarParser.ModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#assignment.
    def visitAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#orExpr.
    def visitOrExpr(self, ctx:ProjectGrammarParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#addSub.
    def visitAddSub(self, ctx:ProjectGrammarParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#float.
    def visitFloat(self, ctx:ProjectGrammarParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#int.
    def visitInt(self, ctx:ProjectGrammarParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#mulDiv.
    def visitMulDiv(self, ctx:ProjectGrammarParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#concatExpr.
    def visitConcatExpr(self, ctx:ProjectGrammarParser.ConcatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#notExpr.
    def visitNotExpr(self, ctx:ProjectGrammarParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#unaryMinus.
    def visitUnaryMinus(self, ctx:ProjectGrammarParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#char.
    def visitChar(self, ctx:ProjectGrammarParser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#id.
    def visitId(self, ctx:ProjectGrammarParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#andExpr.
    def visitAndExpr(self, ctx:ProjectGrammarParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectGrammarParser#primitiveType.
    def visitPrimitiveType(self, ctx:ProjectGrammarParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)



del ProjectGrammarParser