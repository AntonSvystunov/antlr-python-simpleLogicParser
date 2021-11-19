# Generated from logic.g4 by ANTLR 4.9.3
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .logicParser import logicParser
else:
    from logicParser import logicParser

# This class defines a complete generic visitor for a parse tree produced by logicParser.

class logicVisitor(ParseTreeVisitor):
    def __init__(self, data={}) -> None:
        super().__init__()
        self.data = data

    # Visit a parse tree produced by logicParser#expr.
    def visitExpr(self, ctx:logicParser.ExprContext):
        if ctx.left:
            leftExpr = self.visit(ctx.left)
            rightExpr = self.visit(ctx.right)
            op = self.visit(ctx.op)

            print(f"{ctx.left.getText()} {ctx.op.getText()} {ctx.right.getText()} = {op(leftExpr, rightExpr)}")

            return op(leftExpr, rightExpr)
        else:
            return self.visitChildren(ctx)

    def defaultResult(self):
        return False

    def aggregateResult(self, aggregate, nextResult):
        return aggregate or nextResult

    # Visit a parse tree produced by logicParser#opsgn.
    def visitOpsgn(self, ctx:logicParser.OpsgnContext):
        if ctx.getText() == 'OR':
            return lambda a,b: a or b
        return lambda a,b: a and b

    # Visit a parse tree produced by logicParser#sid.
    def visitSid(self, ctx:logicParser.SidContext):
        key = ctx.getText()
        try:
            return self.data[key]
        except:
            return False


    # Visit a parse tree produced by logicParser#boolExpr.
    def visitBoolExpr(self, ctx:logicParser.BoolExprContext):
        key = ctx.getText()
        return key == 'TRUE'



del logicParser