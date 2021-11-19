from antlr4 import CommonTokenStream, FileStream, InputStream

from .logicLexer import logicLexer
from .logicParser import logicParser
from .logicVisitor import logicVisitor
from .customErrorListener import customErrorListener


def start(inputFile, trues, expr):
    input_stream = FileStream(inputFile) if inputFile is not None else InputStream(expr)

    variables = dict.fromkeys(trues.split(','), True)

    return evaluate(input_stream, variables)


def evaluate(input_stream, variables={}):
    lexer = logicLexer(input_stream)

    stream = CommonTokenStream(lexer)

    parser = logicParser(stream)

    parser.addErrorListener(customErrorListener)

    tree = parser.expr()

    visitor = logicVisitor(variables)

    return visitor.visitExpr(tree)
