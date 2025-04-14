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
        4,1,41,140,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,1,1,1,1,1,1,1,
        1,1,1,1,5,1,29,8,1,10,1,12,1,32,9,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,
        40,8,1,10,1,12,1,43,9,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,51,8,1,10,1,
        12,1,54,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,64,8,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,4,1,74,8,1,11,1,12,1,75,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,84,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,104,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,127,
        8,2,10,2,12,2,130,9,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,138,8,3,1,3,0,
        1,4,4,0,2,4,6,0,3,1,0,25,30,1,0,20,21,1,0,22,23,171,0,9,1,0,0,0,
        2,83,1,0,0,0,4,103,1,0,0,0,6,137,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,
        0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,0,13,14,3,
        6,3,0,14,19,5,40,0,0,15,16,5,19,0,0,16,18,5,40,0,0,17,15,1,0,0,0,
        18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,19,1,
        0,0,0,22,23,5,18,0,0,23,84,1,0,0,0,24,25,5,1,0,0,25,30,3,4,2,0,26,
        27,5,19,0,0,27,29,3,4,2,0,28,26,1,0,0,0,29,32,1,0,0,0,30,28,1,0,
        0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,30,1,0,0,0,33,34,5,18,0,0,34,
        84,1,0,0,0,35,36,5,2,0,0,36,41,3,4,2,0,37,38,5,19,0,0,38,40,3,4,
        2,0,39,37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,
        1,0,0,0,43,41,1,0,0,0,44,45,5,18,0,0,45,84,1,0,0,0,46,47,5,3,0,0,
        47,52,5,40,0,0,48,49,5,19,0,0,49,51,3,4,2,0,50,48,1,0,0,0,51,54,
        1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,
        55,84,5,18,0,0,56,57,5,4,0,0,57,58,5,5,0,0,58,59,3,4,2,0,59,60,5,
        6,0,0,60,63,3,2,1,0,61,62,5,7,0,0,62,64,3,2,1,0,63,61,1,0,0,0,63,
        64,1,0,0,0,64,84,1,0,0,0,65,66,5,8,0,0,66,67,5,5,0,0,67,68,3,4,2,
        0,68,69,5,6,0,0,69,70,3,2,1,0,70,84,1,0,0,0,71,73,5,9,0,0,72,74,
        3,2,1,0,73,72,1,0,0,0,74,75,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,
        76,77,1,0,0,0,77,78,5,10,0,0,78,84,1,0,0,0,79,80,3,4,2,0,80,81,5,
        18,0,0,81,84,1,0,0,0,82,84,5,18,0,0,83,13,1,0,0,0,83,24,1,0,0,0,
        83,35,1,0,0,0,83,46,1,0,0,0,83,56,1,0,0,0,83,65,1,0,0,0,83,71,1,
        0,0,0,83,79,1,0,0,0,83,82,1,0,0,0,84,3,1,0,0,0,85,86,6,2,-1,0,86,
        87,5,40,0,0,87,88,5,11,0,0,88,104,3,4,2,17,89,90,5,33,0,0,90,104,
        3,4,2,14,91,92,5,23,0,0,92,104,3,4,2,9,93,94,5,5,0,0,94,95,3,4,2,
        0,95,96,5,6,0,0,96,104,1,0,0,0,97,104,5,39,0,0,98,104,5,38,0,0,99,
        104,5,35,0,0,100,104,5,36,0,0,101,104,5,37,0,0,102,104,5,40,0,0,
        103,85,1,0,0,0,103,89,1,0,0,0,103,91,1,0,0,0,103,93,1,0,0,0,103,
        97,1,0,0,0,103,98,1,0,0,0,103,99,1,0,0,0,103,100,1,0,0,0,103,101,
        1,0,0,0,103,102,1,0,0,0,104,128,1,0,0,0,105,106,10,16,0,0,106,107,
        5,32,0,0,107,127,3,4,2,17,108,109,10,15,0,0,109,110,5,31,0,0,110,
        127,3,4,2,16,111,112,10,13,0,0,112,113,7,0,0,0,113,127,3,4,2,14,
        114,115,10,12,0,0,115,116,7,1,0,0,116,127,3,4,2,13,117,118,10,11,
        0,0,118,119,7,2,0,0,119,127,3,4,2,12,120,121,10,10,0,0,121,122,5,
        24,0,0,122,127,3,4,2,11,123,124,10,8,0,0,124,125,5,34,0,0,125,127,
        3,4,2,9,126,105,1,0,0,0,126,108,1,0,0,0,126,111,1,0,0,0,126,114,
        1,0,0,0,126,117,1,0,0,0,126,120,1,0,0,0,126,123,1,0,0,0,127,130,
        1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,5,1,0,0,0,130,128,1,
        0,0,0,131,138,5,12,0,0,132,138,5,13,0,0,133,138,5,14,0,0,134,138,
        5,15,0,0,135,138,5,16,0,0,136,138,5,17,0,0,137,131,1,0,0,0,137,132,
        1,0,0,0,137,133,1,0,0,0,137,134,1,0,0,0,137,135,1,0,0,0,137,136,
        1,0,0,0,138,7,1,0,0,0,12,11,19,30,41,52,63,75,83,103,126,128,137
    ]

class ProjectGrammarParser ( Parser ):

    grammarFileName = "ProjectGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'read'", "'write'", "'fwrite'", "'if'", 
                     "'('", "')'", "'else'", "'while'", "'{'", "'}'", "'='", 
                     "'int'", "'float'", "'bool'", "'char'", "'string'", 
                     "'FILE'", "';'", "','", "'*'", "'/'", "'+'", "'-'", 
                     "'%'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'&&'", "'||'", "'!'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT_KEYWORD", "FLOAT_KEYWORD", "BOOL_KEYWORD", "CHAR_KEYWORD", 
                      "STRING_KEYWORD", "FILE_KEYWORD", "SEMI", "COMMA", 
                      "MUL", "DIV", "ADD", "SUB", "MOD", "EQ", "NEQ", "LT", 
                      "GT", "LTE", "GTE", "AND", "OR", "NOT", "CONCAT", 
                      "BOOL", "CHAR", "STRING", "FLOAT", "INT", "IDENTIFIER", 
                      "WS" ]

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
    INT_KEYWORD=12
    FLOAT_KEYWORD=13
    BOOL_KEYWORD=14
    CHAR_KEYWORD=15
    STRING_KEYWORD=16
    FILE_KEYWORD=17
    SEMI=18
    COMMA=19
    MUL=20
    DIV=21
    ADD=22
    SUB=23
    MOD=24
    EQ=25
    NEQ=26
    LT=27
    GT=28
    LTE=29
    GTE=30
    AND=31
    OR=32
    NOT=33
    CONCAT=34
    BOOL=35
    CHAR=36
    STRING=37
    FLOAT=38
    INT=39
    IDENTIFIER=40
    WS=41

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2173262361406) != 0)):
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


    class WhileLoopsContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectGrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ProjectGrammarParser.ExprContext,0)

        def stat(self):
            return self.getTypedRuleContext(ProjectGrammarParser.StatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoops" ):
                listener.enterWhileLoops(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoops" ):
                listener.exitWhileLoops(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoops" ):
                return visitor.visitWhileLoops(self)
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
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 14, 15, 16, 17]:
                localctx = ProjectGrammarParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.primitiveType()
                self.state = 14
                self.match(ProjectGrammarParser.IDENTIFIER)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==19:
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
                while _la==19:
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
                while _la==19:
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
                localctx = ProjectGrammarParser.FileWriteContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.match(ProjectGrammarParser.T__2)
                self.state = 47
                self.match(ProjectGrammarParser.IDENTIFIER)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==19:
                    self.state = 48
                    self.match(ProjectGrammarParser.COMMA)
                    self.state = 49
                    self.expr(0)
                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 55
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [4]:
                localctx = ProjectGrammarParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.match(ProjectGrammarParser.T__3)
                self.state = 57
                self.match(ProjectGrammarParser.T__4)
                self.state = 58
                self.expr(0)
                self.state = 59
                self.match(ProjectGrammarParser.T__5)
                self.state = 60
                self.stat()
                self.state = 63
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 61
                    self.match(ProjectGrammarParser.T__6)
                    self.state = 62
                    self.stat()


                pass
            elif token in [8]:
                localctx = ProjectGrammarParser.WhileLoopsContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.match(ProjectGrammarParser.T__7)
                self.state = 66
                self.match(ProjectGrammarParser.T__4)
                self.state = 67
                self.expr(0)
                self.state = 68
                self.match(ProjectGrammarParser.T__5)
                self.state = 69
                self.stat()
                pass
            elif token in [9]:
                localctx = ProjectGrammarParser.BlockContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 71
                self.match(ProjectGrammarParser.T__8)
                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 72
                    self.stat()
                    self.state = 75 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2173262361406) != 0)):
                        break

                self.state = 77
                self.match(ProjectGrammarParser.T__9)
                pass
            elif token in [5, 23, 33, 35, 36, 37, 38, 39, 40]:
                localctx = ProjectGrammarParser.SimpleExprContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 79
                self.expr(0)
                self.state = 80
                self.match(ProjectGrammarParser.SEMI)
                pass
            elif token in [18]:
                localctx = ProjectGrammarParser.EmptyStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 82
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
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = ProjectGrammarParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 86
                self.match(ProjectGrammarParser.IDENTIFIER)
                self.state = 87
                self.match(ProjectGrammarParser.T__10)
                self.state = 88
                self.expr(17)
                pass

            elif la_ == 2:
                localctx = ProjectGrammarParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 89
                self.match(ProjectGrammarParser.NOT)
                self.state = 90
                self.expr(14)
                pass

            elif la_ == 3:
                localctx = ProjectGrammarParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 91
                self.match(ProjectGrammarParser.SUB)
                self.state = 92
                self.expr(9)
                pass

            elif la_ == 4:
                localctx = ProjectGrammarParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 93
                self.match(ProjectGrammarParser.T__4)
                self.state = 94
                self.expr(0)
                self.state = 95
                self.match(ProjectGrammarParser.T__5)
                pass

            elif la_ == 5:
                localctx = ProjectGrammarParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 97
                self.match(ProjectGrammarParser.INT)
                pass

            elif la_ == 6:
                localctx = ProjectGrammarParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 98
                self.match(ProjectGrammarParser.FLOAT)
                pass

            elif la_ == 7:
                localctx = ProjectGrammarParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 99
                self.match(ProjectGrammarParser.BOOL)
                pass

            elif la_ == 8:
                localctx = ProjectGrammarParser.CharContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 100
                self.match(ProjectGrammarParser.CHAR)
                pass

            elif la_ == 9:
                localctx = ProjectGrammarParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 101
                self.match(ProjectGrammarParser.STRING)
                pass

            elif la_ == 10:
                localctx = ProjectGrammarParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                self.match(ProjectGrammarParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 126
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = ProjectGrammarParser.OrExprContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 105
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 106
                        self.match(ProjectGrammarParser.OR)
                        self.state = 107
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = ProjectGrammarParser.AndExprContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 108
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 109
                        self.match(ProjectGrammarParser.AND)
                        self.state = 110
                        self.expr(16)
                        pass

                    elif la_ == 3:
                        localctx = ProjectGrammarParser.ComparisonContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 111
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 112
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 113
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = ProjectGrammarParser.MulDivContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 114
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 115
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 116
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = ProjectGrammarParser.AddSubContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 117
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 118
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==23):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 119
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = ProjectGrammarParser.ModExprContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 120
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")

                        self.state = 121
                        self.match(ProjectGrammarParser.MOD)
                        self.state = 122
                        self.expr(11)
                        pass

                    elif la_ == 7:
                        localctx = ProjectGrammarParser.ConcatExprContext(self, ProjectGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 123
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 124
                        self.match(ProjectGrammarParser.CONCAT)
                        self.state = 125
                        self.expr(9)
                        pass

             
                self.state = 130
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
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                localctx.type_ = self.match(ProjectGrammarParser.INT_KEYWORD)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                localctx.type_ = self.match(ProjectGrammarParser.FLOAT_KEYWORD)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                localctx.type_ = self.match(ProjectGrammarParser.BOOL_KEYWORD)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 134
                localctx.type_ = self.match(ProjectGrammarParser.CHAR_KEYWORD)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 135
                localctx.type_ = self.match(ProjectGrammarParser.STRING_KEYWORD)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 136
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
         




