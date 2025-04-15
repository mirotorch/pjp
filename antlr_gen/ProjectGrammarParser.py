# Generated from ProjectGrammar.g4 by ANTLR 4.13.2
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
        4,1,43,145,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,1,1,1,1,1,1,1,
        1,1,1,1,5,1,29,8,1,10,1,12,1,32,9,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,
        40,8,1,10,1,12,1,43,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,5,1,56,8,1,10,1,12,1,59,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,69,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,79,8,1,11,1,12,1,
        80,1,1,1,1,1,1,1,1,1,1,1,1,3,1,89,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,109,8,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,5,2,132,8,2,10,2,12,2,135,9,2,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,143,8,3,1,3,0,1,4,4,0,2,4,6,0,3,1,0,26,31,1,0,21,22,1,0,
        23,24,177,0,9,1,0,0,0,2,88,1,0,0,0,4,108,1,0,0,0,6,142,1,0,0,0,8,
        10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,
        12,1,1,0,0,0,13,14,3,6,3,0,14,19,5,41,0,0,15,16,5,20,0,0,16,18,5,
        41,0,0,17,15,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,
        22,1,0,0,0,21,19,1,0,0,0,22,23,5,19,0,0,23,89,1,0,0,0,24,25,5,1,
        0,0,25,30,3,4,2,0,26,27,5,20,0,0,27,29,3,4,2,0,28,26,1,0,0,0,29,
        32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,30,1,0,0,
        0,33,34,5,19,0,0,34,89,1,0,0,0,35,36,5,2,0,0,36,41,3,4,2,0,37,38,
        5,20,0,0,38,40,3,4,2,0,39,37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,
        41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,19,0,0,45,89,1,
        0,0,0,46,47,5,3,0,0,47,48,5,41,0,0,48,49,3,4,2,0,49,50,5,19,0,0,
        50,89,1,0,0,0,51,52,5,4,0,0,52,57,5,41,0,0,53,54,5,20,0,0,54,56,
        3,4,2,0,55,53,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,
        58,60,1,0,0,0,59,57,1,0,0,0,60,89,5,19,0,0,61,62,5,5,0,0,62,63,5,
        6,0,0,63,64,3,4,2,0,64,65,5,7,0,0,65,68,3,2,1,0,66,67,5,8,0,0,67,
        69,3,2,1,0,68,66,1,0,0,0,68,69,1,0,0,0,69,89,1,0,0,0,70,71,5,9,0,
        0,71,72,5,6,0,0,72,73,3,4,2,0,73,74,5,7,0,0,74,75,3,2,1,0,75,89,
        1,0,0,0,76,78,5,10,0,0,77,79,3,2,1,0,78,77,1,0,0,0,79,80,1,0,0,0,
        80,78,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,83,5,11,0,0,83,89,1,
        0,0,0,84,85,3,4,2,0,85,86,5,19,0,0,86,89,1,0,0,0,87,89,5,19,0,0,
        88,13,1,0,0,0,88,24,1,0,0,0,88,35,1,0,0,0,88,46,1,0,0,0,88,51,1,
        0,0,0,88,61,1,0,0,0,88,70,1,0,0,0,88,76,1,0,0,0,88,84,1,0,0,0,88,
        87,1,0,0,0,89,3,1,0,0,0,90,91,6,2,-1,0,91,92,5,41,0,0,92,93,5,12,
        0,0,93,109,3,4,2,17,94,95,5,34,0,0,95,109,3,4,2,14,96,97,5,24,0,
        0,97,109,3,4,2,9,98,99,5,6,0,0,99,100,3,4,2,0,100,101,5,7,0,0,101,
        109,1,0,0,0,102,109,5,40,0,0,103,109,5,39,0,0,104,109,5,36,0,0,105,
        109,5,37,0,0,106,109,5,38,0,0,107,109,5,41,0,0,108,90,1,0,0,0,108,
        94,1,0,0,0,108,96,1,0,0,0,108,98,1,0,0,0,108,102,1,0,0,0,108,103,
        1,0,0,0,108,104,1,0,0,0,108,105,1,0,0,0,108,106,1,0,0,0,108,107,
        1,0,0,0,109,133,1,0,0,0,110,111,10,16,0,0,111,112,5,33,0,0,112,132,
        3,4,2,17,113,114,10,15,0,0,114,115,5,32,0,0,115,132,3,4,2,16,116,
        117,10,13,0,0,117,118,7,0,0,0,118,132,3,4,2,14,119,120,10,12,0,0,
        120,121,7,1,0,0,121,132,3,4,2,13,122,123,10,11,0,0,123,124,7,2,0,
        0,124,132,3,4,2,12,125,126,10,10,0,0,126,127,5,25,0,0,127,132,3,
        4,2,11,128,129,10,8,0,0,129,130,5,35,0,0,130,132,3,4,2,9,131,110,
        1,0,0,0,131,113,1,0,0,0,131,116,1,0,0,0,131,119,1,0,0,0,131,122,
        1,0,0,0,131,125,1,0,0,0,131,128,1,0,0,0,132,135,1,0,0,0,133,131,
        1,0,0,0,133,134,1,0,0,0,134,5,1,0,0,0,135,133,1,0,0,0,136,143,5,
        13,0,0,137,143,5,14,0,0,138,143,5,15,0,0,139,143,5,16,0,0,140,143,
        5,17,0,0,141,143,5,18,0,0,142,136,1,0,0,0,142,137,1,0,0,0,142,138,
        1,0,0,0,142,139,1,0,0,0,142,140,1,0,0,0,142,141,1,0,0,0,143,7,1,
        0,0,0,12,11,19,30,41,57,68,80,88,108,131,133,142
    ]

class ProjectGrammarParser ( Parser ):

    grammarFileName = "ProjectGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'read'", "'write'", "'fopen'", "'fwrite'", 
                     "'if'", "'('", "')'", "'else'", "'while'", "'{'", "'}'", 
                     "'='", "'int'", "'float'", "'bool'", "'char'", "'string'", 
                     "'FILE'", "';'", "','", "'*'", "'/'", "'+'", "'-'", 
                     "'%'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'&&'", "'||'", "'!'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT_KEYWORD", "FLOAT_KEYWORD", "BOOL_KEYWORD", 
                      "CHAR_KEYWORD", "STRING_KEYWORD", "FILE_KEYWORD", 
                      "SEMI", "COMMA", "MUL", "DIV", "ADD", "SUB", "MOD", 
                      "EQ", "NEQ", "LT", "GT", "LTE", "GTE", "AND", "OR", 
                      "NOT", "CONCAT", "BOOL", "CHAR", "STRING", "FLOAT", 
                      "INT", "IDENTIFIER", "WS", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_primitiveType = 3

    ruleNames =  [ "program", "stat", "expr", "primitiveType" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    INT_KEYWORD=13
    FLOAT_KEYWORD=14
    BOOL_KEYWORD=15
    CHAR_KEYWORD=16
    STRING_KEYWORD=17
    FILE_KEYWORD=18
    SEMI=19
    COMMA=20
    MUL=21
    DIV=22
    ADD=23
    SUB=24
    MOD=25
    EQ=26
    NEQ=27
    LT=28
    GT=29
    LTE=30
    GTE=31
    AND=32
    OR=33
    NOT=34
    CONCAT=35
    BOOL=36
    CHAR=37
    STRING=38
    FLOAT=39
    INT=40
    IDENTIFIER=41
    WS=42
    LINE_COMMENT=43

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

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.StatContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.StatContext,i)


        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_program

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

        localctx = ProjectGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4346524722814) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FileOpenContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ProjectGrammarParser.IDENTIFIER, 0)
        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)

        def SEMI(self):
            return self.getToken(ProjectGrammarParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFileOpen" ):
                listener.enterFileOpen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFileOpen" ):
                listener.exitFileOpen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFileOpen" ):
                return visitor.visitFileOpen(self)
            else:
                return visitor.visitChildren(self)


    class EmptyStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(ProjectGrammarParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStatement" ):
                return visitor.visitEmptyStatement(self)
            else:
                return visitor.visitChildren(self)


    class WhileLoopContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)

        def stat(self):
            return self.getTypedRuleContext(ProjectGrammarParser.StatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)


    class SimpleExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)

        def SEMI(self):
            return self.getToken(ProjectGrammarParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpr" ):
                listener.enterSimpleExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpr" ):
                listener.exitSimpleExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpr" ):
                return visitor.visitSimpleExpr(self)
            else:
                return visitor.visitChildren(self)


    class ReadContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def SEMI(self):
            return self.getToken(ProjectGrammarParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectGrammarParser.COMMA)
            else:
                return self.getToken(ProjectGrammarParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)


    class FileWriteContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ProjectGrammarParser.IDENTIFIER, 0)
        def SEMI(self):
            return self.getToken(ProjectGrammarParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectGrammarParser.COMMA)
            else:
                return self.getToken(ProjectGrammarParser.COMMA, i)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFileWrite" ):
                listener.enterFileWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFileWrite" ):
                listener.exitFileWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFileWrite" ):
                return visitor.visitFileWrite(self)
            else:
                return visitor.visitChildren(self)


    class BlockContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.StatContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.StatContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primitiveType(self):
            return self.getTypedRuleContext(ProjectGrammarParser.PrimitiveTypeContext,0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectGrammarParser.IDENTIFIER)
            else:
                return self.getToken(ProjectGrammarParser.IDENTIFIER, i)
        def SEMI(self):
            return self.getToken(ProjectGrammarParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectGrammarParser.COMMA)
            else:
                return self.getToken(ProjectGrammarParser.COMMA, i)

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


    class WriteContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def SEMI(self):
            return self.getToken(ProjectGrammarParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectGrammarParser.COMMA)
            else:
                return self.getToken(ProjectGrammarParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


    class IfElseContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.StatContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.StatContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse" ):
                listener.enterIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse" ):
                listener.exitIfElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = ProjectGrammarParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16, 17, 18]:
                localctx = ProjectGrammarParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.primitiveType()
                self.state = 14
                self.match(ProjectGrammarParser.IDENTIFIER)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 15
                    self.match(ProjectGrammarParser.COMMA)
                    self.state = 16
                    self.match(ProjectGrammarParser.IDENTIFIER)
                    self.state = 21
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 22
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [1]:
                localctx = ProjectGrammarParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(ProjectGrammarParser.T__0)
                self.state = 25
                self.expr(0)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 26
                    self.match(ProjectGrammarParser.COMMA)
                    self.state = 27
                    self.expr(0)
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 33
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [2]:
                localctx = ProjectGrammarParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(ProjectGrammarParser.T__1)
                self.state = 36
                self.expr(0)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 37
                    self.match(ProjectGrammarParser.COMMA)
                    self.state = 38
                    self.expr(0)
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 44
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [3]:
                localctx = ProjectGrammarParser.FileOpenContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.match(ProjectGrammarParser.T__2)
                self.state = 47
                self.match(ProjectGrammarParser.IDENTIFIER)
                self.state = 48
                self.expr(0)
                self.state = 49
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [4]:
                localctx = ProjectGrammarParser.FileWriteContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.match(ProjectGrammarParser.T__3)
                self.state = 52
                self.match(ProjectGrammarParser.IDENTIFIER)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 53
                    self.match(ProjectGrammarParser.COMMA)
                    self.state = 54
                    self.expr(0)
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 60
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [5]:
                localctx = ProjectGrammarParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 61
                self.match(ProjectGrammarParser.T__4)
                self.state = 62
                self.match(ProjectGrammarParser.T__5)
                self.state = 63
                self.expr(0)
                self.state = 64
                self.match(ProjectGrammarParser.T__6)
                self.state = 65
                self.stat()
                self.state = 68
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 66
                    self.match(ProjectGrammarParser.T__7)
                    self.state = 67
                    self.stat()


                pass
            elif token in [9]:
                localctx = ProjectGrammarParser.WhileLoopContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 70
                self.match(ProjectGrammarParser.T__8)
                self.state = 71
                self.match(ProjectGrammarParser.T__5)
                self.state = 72
                self.expr(0)
                self.state = 73
                self.match(ProjectGrammarParser.T__6)
                self.state = 74
                self.stat()
                pass
            elif token in [10]:
                localctx = ProjectGrammarParser.BlockContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 76
                self.match(ProjectGrammarParser.T__9)
                self.state = 78 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 77
                    self.stat()
                    self.state = 80 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4346524722814) != 0)):
                        break

                self.state = 82
                self.match(ProjectGrammarParser.T__10)
                pass
            elif token in [6, 24, 34, 36, 37, 38, 39, 40, 41]:
                localctx = ProjectGrammarParser.SimpleExprContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 84
                self.expr(0)
                self.state = 85
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [19]:
                localctx = ProjectGrammarParser.EmptyStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 87
                self.match(ProjectGrammarParser.SEMI)
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
            return ProjectGrammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


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


    class ComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def EQ(self):
            return self.getToken(ProjectGrammarParser.EQ, 0)
        def NEQ(self):
            return self.getToken(ProjectGrammarParser.NEQ, 0)
        def LT(self):
            return self.getToken(ProjectGrammarParser.LT, 0)
        def GT(self):
            return self.getToken(ProjectGrammarParser.GT, 0)
        def LTE(self):
            return self.getToken(ProjectGrammarParser.LTE, 0)
        def GTE(self):
            return self.getToken(ProjectGrammarParser.GTE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(ProjectGrammarParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ProjectGrammarParser.STRING, 0)

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


    class ModExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def MOD(self):
            return self.getToken(ProjectGrammarParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModExpr" ):
                listener.enterModExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModExpr" ):
                listener.exitModExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModExpr" ):
                return visitor.visitModExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ProjectGrammarParser.IDENTIFIER, 0)
        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


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


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def OR(self):
            return self.getToken(ProjectGrammarParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def ADD(self):
            return self.getToken(ProjectGrammarParser.ADD, 0)
        def SUB(self):
            return self.getToken(ProjectGrammarParser.SUB, 0)

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


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(ProjectGrammarParser.FLOAT, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ProjectGrammarParser.INT, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def MUL(self):
            return self.getToken(ProjectGrammarParser.MUL, 0)
        def DIV(self):
            return self.getToken(ProjectGrammarParser.DIV, 0)

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


    class ConcatExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def CONCAT(self):
            return self.getToken(ProjectGrammarParser.CONCAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatExpr" ):
                listener.enterConcatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatExpr" ):
                listener.exitConcatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatExpr" ):
                return visitor.visitConcatExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(ProjectGrammarParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(ProjectGrammarParser.SUB, 0)
        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class CharContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(ProjectGrammarParser.CHAR, 0)

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


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ProjectGrammarParser.IDENTIFIER, 0)

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


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,i)

        def AND(self):
            return self.getToken(ProjectGrammarParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ProjectGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = ProjectGrammarParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 91
                self.match(ProjectGrammarParser.IDENTIFIER)
                self.state = 92
                self.match(ProjectGrammarParser.T__11)
                self.state = 93
                self.expr(17)
                pass

            elif la_ == 2:
                localctx = ProjectGrammarParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 94
                self.match(ProjectGrammarParser.NOT)
                self.state = 95
                self.expr(14)
                pass

            elif la_ == 3:
                localctx = ProjectGrammarParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 96
                self.match(ProjectGrammarParser.SUB)
                self.state = 97
                self.expr(9)
                pass

            elif la_ == 4:
                localctx = ProjectGrammarParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 98
                self.match(ProjectGrammarParser.T__5)
                self.state = 99
                self.expr(0)
                self.state = 100
                self.match(ProjectGrammarParser.T__6)
                pass

            elif la_ == 5:
                localctx = ProjectGrammarParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                self.match(ProjectGrammarParser.INT)
                pass

            elif la_ == 6:
                localctx = ProjectGrammarParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 103
                self.match(ProjectGrammarParser.FLOAT)
                pass

            elif la_ == 7:
                localctx = ProjectGrammarParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 104
                self.match(ProjectGrammarParser.BOOL)
                pass

            elif la_ == 8:
                localctx = ProjectGrammarParser.CharContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 105
                self.match(ProjectGrammarParser.CHAR)
                pass

            elif la_ == 9:
                localctx = ProjectGrammarParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(ProjectGrammarParser.STRING)
                pass

            elif la_ == 10:
                localctx = ProjectGrammarParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(ProjectGrammarParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 131
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = ProjectGrammarParser.OrExprContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 111
                        self.match(ProjectGrammarParser.OR)
                        self.state = 112
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = ProjectGrammarParser.AndExprContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 113
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 114
                        self.match(ProjectGrammarParser.AND)
                        self.state = 115
                        self.expr(16)
                        pass

                    elif la_ == 3:
                        localctx = ProjectGrammarParser.ComparisonContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 116
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 117
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 118
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = ProjectGrammarParser.MulDivContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 119
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 120
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 121
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = ProjectGrammarParser.AddSubContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 122
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 123
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 124
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = ProjectGrammarParser.ModExprContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 125
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")

                        self.state = 126
                        self.match(ProjectGrammarParser.MOD)
                        self.state = 127
                        self.expr(11)
                        pass

                    elif la_ == 7:
                        localctx = ProjectGrammarParser.ConcatExprContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 128
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 129
                        self.match(ProjectGrammarParser.CONCAT)
                        self.state = 130
                        self.expr(9)
                        pass

             
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
            return self.getToken(ProjectGrammarParser.INT_KEYWORD, 0)

        def FLOAT_KEYWORD(self):
            return self.getToken(ProjectGrammarParser.FLOAT_KEYWORD, 0)

        def BOOL_KEYWORD(self):
            return self.getToken(ProjectGrammarParser.BOOL_KEYWORD, 0)

        def CHAR_KEYWORD(self):
            return self.getToken(ProjectGrammarParser.CHAR_KEYWORD, 0)

        def STRING_KEYWORD(self):
            return self.getToken(ProjectGrammarParser.STRING_KEYWORD, 0)

        def FILE_KEYWORD(self):
            return self.getToken(ProjectGrammarParser.FILE_KEYWORD, 0)

        def getRuleIndex(self):
            return ProjectGrammarParser.RULE_primitiveType

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

        localctx = ProjectGrammarParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primitiveType)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                localctx.type_ = self.match(ProjectGrammarParser.INT_KEYWORD)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                localctx.type_ = self.match(ProjectGrammarParser.FLOAT_KEYWORD)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                localctx.type_ = self.match(ProjectGrammarParser.BOOL_KEYWORD)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                localctx.type_ = self.match(ProjectGrammarParser.CHAR_KEYWORD)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 140
                localctx.type_ = self.match(ProjectGrammarParser.STRING_KEYWORD)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 141
                localctx.type_ = self.match(ProjectGrammarParser.FILE_KEYWORD)
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
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         




