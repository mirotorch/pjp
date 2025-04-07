# Generated from lab8.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,64,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,1,1,1,1,1,1,1,
        1,1,3,1,28,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,3,2,44,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,52,8,2,10,2,12,2,55,
        9,2,1,3,1,3,1,3,1,3,1,3,3,3,62,8,3,1,3,0,1,4,4,0,2,4,6,0,2,1,0,11,
        12,1,0,13,14,75,0,9,1,0,0,0,2,27,1,0,0,0,4,43,1,0,0,0,6,61,1,0,0,
        0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,
        0,0,12,1,1,0,0,0,13,14,3,6,3,0,14,19,5,20,0,0,15,16,5,10,0,0,16,
        18,5,20,0,0,17,15,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,
        0,0,20,22,1,0,0,0,21,19,1,0,0,0,22,23,5,9,0,0,23,28,1,0,0,0,24,25,
        3,4,2,0,25,26,5,9,0,0,26,28,1,0,0,0,27,13,1,0,0,0,27,24,1,0,0,0,
        28,3,1,0,0,0,29,30,6,2,-1,0,30,44,5,19,0,0,31,44,5,20,0,0,32,44,
        5,18,0,0,33,44,5,15,0,0,34,44,5,16,0,0,35,44,5,17,0,0,36,37,5,1,
        0,0,37,38,3,4,2,0,38,39,5,2,0,0,39,44,1,0,0,0,40,41,5,20,0,0,41,
        42,5,3,0,0,42,44,3,4,2,1,43,29,1,0,0,0,43,31,1,0,0,0,43,32,1,0,0,
        0,43,33,1,0,0,0,43,34,1,0,0,0,43,35,1,0,0,0,43,36,1,0,0,0,43,40,
        1,0,0,0,44,53,1,0,0,0,45,46,10,10,0,0,46,47,7,0,0,0,47,52,3,4,2,
        11,48,49,10,9,0,0,49,50,7,1,0,0,50,52,3,4,2,10,51,45,1,0,0,0,51,
        48,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,5,1,0,0,
        0,55,53,1,0,0,0,56,62,5,4,0,0,57,62,5,5,0,0,58,62,5,6,0,0,59,62,
        5,7,0,0,60,62,5,8,0,0,61,56,1,0,0,0,61,57,1,0,0,0,61,58,1,0,0,0,
        61,59,1,0,0,0,61,60,1,0,0,0,62,7,1,0,0,0,7,11,19,27,43,51,53,61
    ]

class lab8Parser ( Parser ):

    grammarFileName = "lab8.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'='", "'int'", "'float'", 
                     "'bool'", "'char'", "'string'", "';'", "','", "'*'", 
                     "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT_KEYWORD", "FLOAT_KEYWORD", "BOOL_KEYWORD", "CHAR_KEYWORD", 
                      "STRING_KEYWORD", "SEMI", "COMMA", "MUL", "DIV", "ADD", 
                      "SUB", "BOOL", "CHAR", "STRING", "FLOAT", "INT", "IDENTIFIER", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_primitiveType = 3

    ruleNames =  [ "program", "statement", "expr", "primitiveType" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    INT_KEYWORD=4
    FLOAT_KEYWORD=5
    BOOL_KEYWORD=6
    CHAR_KEYWORD=7
    STRING_KEYWORD=8
    SEMI=9
    COMMA=10
    MUL=11
    DIV=12
    ADD=13
    SUB=14
    BOOL=15
    CHAR=16
    STRING=17
    FLOAT=18
    INT=19
    IDENTIFIER=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lab8Parser.StatementContext)
            else:
                return self.getTypedRuleContext(lab8Parser.StatementContext,i)


        def getRuleIndex(self):
            return lab8Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = lab8Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.statement()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064882) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lab8Parser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lab8Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primitiveType(self):
            return self.getTypedRuleContext(lab8Parser.PrimitiveTypeContext,0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(lab8Parser.IDENTIFIER)
            else:
                return self.getToken(lab8Parser.IDENTIFIER, i)
        def SEMI(self):
            return self.getToken(lab8Parser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(lab8Parser.COMMA)
            else:
                return self.getToken(lab8Parser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lab8Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(lab8Parser.ExprContext,0)

        def SEMI(self):
            return self.getToken(lab8Parser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = lab8Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7, 8]:
                localctx = lab8Parser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.primitiveType()
                self.state = 14
                self.match(lab8Parser.IDENTIFIER)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 15
                    self.match(lab8Parser.COMMA)
                    self.state = 16
                    self.match(lab8Parser.IDENTIFIER)
                    self.state = 21
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 22
                self.match(lab8Parser.SEMI)
                pass
            elif token in [1, 15, 16, 17, 18, 19, 20]:
                localctx = lab8Parser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.expr(0)
                self.state = 25
                self.match(lab8Parser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lab8Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lab8Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(lab8Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class BooleanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lab8Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(lab8Parser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lab8Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(lab8Parser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lab8Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(lab8Parser.IDENTIFIER, 0)
        def expr(self):
            return self.getTypedRuleContext(lab8Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class CharContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lab8Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(lab8Parser.CHAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar" ):
                listener.enterChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar" ):
                listener.exitChar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChar" ):
                return visitor.visitChar(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lab8Parser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lab8Parser.ExprContext)
            else:
                return self.getTypedRuleContext(lab8Parser.ExprContext,i)

        def ADD(self):
            return self.getToken(lab8Parser.ADD, 0)
        def SUB(self):
            return self.getToken(lab8Parser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lab8Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(lab8Parser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lab8Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(lab8Parser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lab8Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(lab8Parser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lab8Parser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lab8Parser.ExprContext)
            else:
                return self.getTypedRuleContext(lab8Parser.ExprContext,i)

        def MUL(self):
            return self.getToken(lab8Parser.MUL, 0)
        def DIV(self):
            return self.getToken(lab8Parser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = lab8Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = lab8Parser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 30
                self.match(lab8Parser.INT)
                pass

            elif la_ == 2:
                localctx = lab8Parser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.match(lab8Parser.IDENTIFIER)
                pass

            elif la_ == 3:
                localctx = lab8Parser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.match(lab8Parser.FLOAT)
                pass

            elif la_ == 4:
                localctx = lab8Parser.BooleanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self.match(lab8Parser.BOOL)
                pass

            elif la_ == 5:
                localctx = lab8Parser.CharContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.match(lab8Parser.CHAR)
                pass

            elif la_ == 6:
                localctx = lab8Parser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                self.match(lab8Parser.STRING)
                pass

            elif la_ == 7:
                localctx = lab8Parser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(lab8Parser.T__0)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(lab8Parser.T__1)
                pass

            elif la_ == 8:
                localctx = lab8Parser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.match(lab8Parser.IDENTIFIER)
                self.state = 41
                self.match(lab8Parser.T__2)
                self.state = 42
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = lab8Parser.MulDivContext(self, lab8Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 46
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 47
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = lab8Parser.AddSubContext(self, lab8Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 49
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 50
                        self.expr(10)
                        pass

             
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None # Token

        def INT_KEYWORD(self):
            return self.getToken(lab8Parser.INT_KEYWORD, 0)

        def FLOAT_KEYWORD(self):
            return self.getToken(lab8Parser.FLOAT_KEYWORD, 0)

        def BOOL_KEYWORD(self):
            return self.getToken(lab8Parser.BOOL_KEYWORD, 0)

        def CHAR_KEYWORD(self):
            return self.getToken(lab8Parser.CHAR_KEYWORD, 0)

        def STRING_KEYWORD(self):
            return self.getToken(lab8Parser.STRING_KEYWORD, 0)

        def getRuleIndex(self):
            return lab8Parser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = lab8Parser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primitiveType)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                localctx.type_ = self.match(lab8Parser.INT_KEYWORD)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                localctx.type_ = self.match(lab8Parser.FLOAT_KEYWORD)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                localctx.type_ = self.match(lab8Parser.BOOL_KEYWORD)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                localctx.type_ = self.match(lab8Parser.CHAR_KEYWORD)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                localctx.type_ = self.match(lab8Parser.STRING_KEYWORD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         




