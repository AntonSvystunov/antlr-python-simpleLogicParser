# Generated from logic.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\37\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\27\n\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\5\2\2\6\2\4\6\b\2\2\2\35\2\26\3\2\2\2\4")
        buf.write("\30\3\2\2\2\6\32\3\2\2\2\b\34\3\2\2\2\n\13\7\3\2\2\13")
        buf.write("\f\5\2\2\2\f\r\5\4\3\2\r\16\5\2\2\2\16\17\7\4\2\2\17\27")
        buf.write("\3\2\2\2\20\21\7\3\2\2\21\22\5\2\2\2\22\23\7\4\2\2\23")
        buf.write("\27\3\2\2\2\24\27\5\6\4\2\25\27\5\b\5\2\26\n\3\2\2\2\26")
        buf.write("\20\3\2\2\2\26\24\3\2\2\2\26\25\3\2\2\2\27\3\3\2\2\2\30")
        buf.write("\31\7\6\2\2\31\5\3\2\2\2\32\33\7\7\2\2\33\7\3\2\2\2\34")
        buf.write("\35\7\5\2\2\35\t\3\2\2\2\3\26")
        return buf.getvalue()


class logicParser ( Parser ):

    grammarFileName = "logic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "BOOLN", "OP", 
                      "ID", "WS" ]

    RULE_expr = 0
    RULE_opsgn = 1
    RULE_sid = 2
    RULE_boolExpr = 3

    ruleNames =  [ "expr", "opsgn", "sid", "boolExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    BOOLN=3
    OP=4
    ID=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExprContext
            self.op = None # OpsgnContext
            self.right = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(logicParser.ExprContext)
            else:
                return self.getTypedRuleContext(logicParser.ExprContext,i)


        def opsgn(self):
            return self.getTypedRuleContext(logicParser.OpsgnContext,0)


        def sid(self):
            return self.getTypedRuleContext(logicParser.SidContext,0)


        def boolExpr(self):
            return self.getTypedRuleContext(logicParser.BoolExprContext,0)


        def getRuleIndex(self):
            return logicParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = logicParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(logicParser.T__0)
                self.state = 9
                localctx.left = self.expr()
                self.state = 10
                localctx.op = self.opsgn()
                self.state = 11
                localctx.right = self.expr()
                self.state = 12
                self.match(logicParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(logicParser.T__0)
                self.state = 15
                self.expr()
                self.state = 16
                self.match(logicParser.T__1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self.sid()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 19
                self.boolExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpsgnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP(self):
            return self.getToken(logicParser.OP, 0)

        def getRuleIndex(self):
            return logicParser.RULE_opsgn

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpsgn" ):
                return visitor.visitOpsgn(self)
            else:
                return visitor.visitChildren(self)




    def opsgn(self):

        localctx = logicParser.OpsgnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_opsgn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(logicParser.OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(logicParser.ID, 0)

        def getRuleIndex(self):
            return logicParser.RULE_sid

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSid" ):
                return visitor.visitSid(self)
            else:
                return visitor.visitChildren(self)




    def sid(self):

        localctx = logicParser.SidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(logicParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLN(self):
            return self.getToken(logicParser.BOOLN, 0)

        def getRuleIndex(self):
            return logicParser.RULE_boolExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)




    def boolExpr(self):

        localctx = logicParser.BoolExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_boolExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(logicParser.BOOLN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





