# Generated from ProjectGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ProjectGrammarParser import ProjectGrammarParser
else:
    from ProjectGrammarParser import ProjectGrammarParser

# This class defines a complete listener for a parse tree produced by ProjectGrammarParser.
class ProjectGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ProjectGrammarParser#program.
    def enterProgram(self, ctx:ProjectGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#program.
    def exitProgram(self, ctx:ProjectGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#declaration.
    def enterDeclaration(self, ctx:ProjectGrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#declaration.
    def exitDeclaration(self, ctx:ProjectGrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#read.
    def enterRead(self, ctx:ProjectGrammarParser.ReadContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#read.
    def exitRead(self, ctx:ProjectGrammarParser.ReadContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#write.
    def enterWrite(self, ctx:ProjectGrammarParser.WriteContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#write.
    def exitWrite(self, ctx:ProjectGrammarParser.WriteContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#fileWrite.
    def enterFileWrite(self, ctx:ProjectGrammarParser.FileWriteContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#fileWrite.
    def exitFileWrite(self, ctx:ProjectGrammarParser.FileWriteContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#ifElse.
    def enterIfElse(self, ctx:ProjectGrammarParser.IfElseContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#ifElse.
    def exitIfElse(self, ctx:ProjectGrammarParser.IfElseContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#whileLoops.
    def enterWhileLoops(self, ctx:ProjectGrammarParser.WhileLoopsContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#whileLoops.
    def exitWhileLoops(self, ctx:ProjectGrammarParser.WhileLoopsContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#block.
    def enterBlock(self, ctx:ProjectGrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#block.
    def exitBlock(self, ctx:ProjectGrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#simpleExpr.
    def enterSimpleExpr(self, ctx:ProjectGrammarParser.SimpleExprContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#simpleExpr.
    def exitSimpleExpr(self, ctx:ProjectGrammarParser.SimpleExprContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#emptyStatement.
    def enterEmptyStatement(self, ctx:ProjectGrammarParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#emptyStatement.
    def exitEmptyStatement(self, ctx:ProjectGrammarParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#parens.
    def enterParens(self, ctx:ProjectGrammarParser.ParensContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#parens.
    def exitParens(self, ctx:ProjectGrammarParser.ParensContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#comparison.
    def enterComparison(self, ctx:ProjectGrammarParser.ComparisonContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#comparison.
    def exitComparison(self, ctx:ProjectGrammarParser.ComparisonContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#bool.
    def enterBool(self, ctx:ProjectGrammarParser.BoolContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#bool.
    def exitBool(self, ctx:ProjectGrammarParser.BoolContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#string.
    def enterString(self, ctx:ProjectGrammarParser.StringContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#string.
    def exitString(self, ctx:ProjectGrammarParser.StringContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#modExpr.
    def enterModExpr(self, ctx:ProjectGrammarParser.ModExprContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#modExpr.
    def exitModExpr(self, ctx:ProjectGrammarParser.ModExprContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#assignment.
    def enterAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#assignment.
    def exitAssignment(self, ctx:ProjectGrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#orExpr.
    def enterOrExpr(self, ctx:ProjectGrammarParser.OrExprContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#orExpr.
    def exitOrExpr(self, ctx:ProjectGrammarParser.OrExprContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#addSub.
    def enterAddSub(self, ctx:ProjectGrammarParser.AddSubContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#addSub.
    def exitAddSub(self, ctx:ProjectGrammarParser.AddSubContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#float.
    def enterFloat(self, ctx:ProjectGrammarParser.FloatContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#float.
    def exitFloat(self, ctx:ProjectGrammarParser.FloatContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#int.
    def enterInt(self, ctx:ProjectGrammarParser.IntContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#int.
    def exitInt(self, ctx:ProjectGrammarParser.IntContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#mulDiv.
    def enterMulDiv(self, ctx:ProjectGrammarParser.MulDivContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#mulDiv.
    def exitMulDiv(self, ctx:ProjectGrammarParser.MulDivContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#concatExpr.
    def enterConcatExpr(self, ctx:ProjectGrammarParser.ConcatExprContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#concatExpr.
    def exitConcatExpr(self, ctx:ProjectGrammarParser.ConcatExprContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#notExpr.
    def enterNotExpr(self, ctx:ProjectGrammarParser.NotExprContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#notExpr.
    def exitNotExpr(self, ctx:ProjectGrammarParser.NotExprContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#unaryMinus.
    def enterUnaryMinus(self, ctx:ProjectGrammarParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#unaryMinus.
    def exitUnaryMinus(self, ctx:ProjectGrammarParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#char.
    def enterChar(self, ctx:ProjectGrammarParser.CharContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#char.
    def exitChar(self, ctx:ProjectGrammarParser.CharContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#id.
    def enterId(self, ctx:ProjectGrammarParser.IdContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#id.
    def exitId(self, ctx:ProjectGrammarParser.IdContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#andExpr.
    def enterAndExpr(self, ctx:ProjectGrammarParser.AndExprContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#andExpr.
    def exitAndExpr(self, ctx:ProjectGrammarParser.AndExprContext):
        pass


    # Enter a parse tree produced by ProjectGrammarParser#primitiveType.
    def enterPrimitiveType(self, ctx:ProjectGrammarParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by ProjectGrammarParser#primitiveType.
    def exitPrimitiveType(self, ctx:ProjectGrammarParser.PrimitiveTypeContext):
        pass



del ProjectGrammarParser