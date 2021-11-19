from antlr4.error.ErrorListener import ErrorListener

class customErrorListener( ErrorListener ):

    def __init__(self):
        super(customErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e=None):
        raise Exception("ERROR: when parsing line %d column %d: %s\n" % \
                        (line, column, msg))