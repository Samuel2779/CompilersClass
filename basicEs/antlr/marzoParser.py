# Generated from d:\Escuela\Semestre_8\Compiladores\GitHubClass\CompilersClass\basicEs\antlr\marzo.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("m\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2\7\2\32")
        buf.write("\n\2\f\2\16\2\35\13\2\3\2\7\2 \n\2\f\2\16\2#\13\2\3\2")
        buf.write("\7\2&\n\2\f\2\16\2)\13\2\5\2+\n\2\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5:\n\5\f\5\16\5=\13")
        buf.write("\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7F\n\7\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\7\tP\n\t\f\t\16\tS\13\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\7\t[\n\t\f\t\16\t^\13\t\3\t\3\t\3\t\3\t\7")
        buf.write("\td\n\t\f\t\16\tg\13\t\3\t\3\t\5\tk\n\t\3\t\2\3\b\n\2")
        buf.write("\4\6\b\n\f\16\20\2\2\2q\2*\3\2\2\2\4,\3\2\2\2\6/\3\2\2")
        buf.write("\2\b\63\3\2\2\2\n>\3\2\2\2\fE\3\2\2\2\16G\3\2\2\2\20j")
        buf.write("\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2\2\24\27\3\2\2\2\25")
        buf.write("\23\3\2\2\2\25\26\3\2\2\2\26\33\3\2\2\2\27\25\3\2\2\2")
        buf.write("\30\32\5\f\7\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2")
        buf.write("\2\33\34\3\2\2\2\34+\3\2\2\2\35\33\3\2\2\2\36 \5\f\7\2")
        buf.write("\37\36\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\'\3")
        buf.write("\2\2\2#!\3\2\2\2$&\5\4\3\2%$\3\2\2\2&)\3\2\2\2\'%\3\2")
        buf.write("\2\2\'(\3\2\2\2(+\3\2\2\2)\'\3\2\2\2*\25\3\2\2\2*!\3\2")
        buf.write("\2\2+\3\3\2\2\2,-\7\3\2\2-.\7\f\2\2.\5\3\2\2\2/\60\7\f")
        buf.write("\2\2\60\61\7\4\2\2\61\62\7\r\2\2\62\7\3\2\2\2\63\64\b")
        buf.write("\5\1\2\64\65\7\r\2\2\65;\3\2\2\2\66\67\f\4\2\2\678\7\5")
        buf.write("\2\28:\5\b\5\59\66\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2")
        buf.write("\2<\t\3\2\2\2=;\3\2\2\2>?\7\6\2\2?@\7\r\2\2@\13\3\2\2")
        buf.write("\2AF\5\20\t\2BF\5\b\5\2CF\5\n\6\2DF\5\6\4\2EA\3\2\2\2")
        buf.write("EB\3\2\2\2EC\3\2\2\2ED\3\2\2\2F\r\3\2\2\2GH\7\f\2\2HI")
        buf.write("\7\7\2\2IJ\7\r\2\2J\17\3\2\2\2KL\7\b\2\2LM\5\16\b\2MQ")
        buf.write("\7\t\2\2NP\5\f\7\2ON\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2")
        buf.write("\2\2RT\3\2\2\2SQ\3\2\2\2TU\7\n\2\2Uk\3\2\2\2VW\7\b\2\2")
        buf.write("WX\5\16\b\2X\\\7\t\2\2Y[\5\f\7\2ZY\3\2\2\2[^\3\2\2\2\\")
        buf.write("Z\3\2\2\2\\]\3\2\2\2]_\3\2\2\2^\\\3\2\2\2_`\7\n\2\2`a")
        buf.write("\7\13\2\2ae\7\t\2\2bd\5\f\7\2cb\3\2\2\2dg\3\2\2\2ec\3")
        buf.write("\2\2\2ef\3\2\2\2fh\3\2\2\2ge\3\2\2\2hi\7\n\2\2ik\3\2\2")
        buf.write("\2jK\3\2\2\2jV\3\2\2\2k\21\3\2\2\2\r\25\33!\'*;EQ\\ej")
        return buf.getvalue()


class marzoParser ( Parser ):

    grammarFileName = "marzo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'='", "'+'", "'print'", "'=='", 
                     "'if'", "'{'", "'}'", "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Name", "Numero", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_assignacion = 2
    RULE_expression = 3
    RULE_printstmt = 4
    RULE_statements = 5
    RULE_comparation = 6
    RULE_ifstatement = 7

    ruleNames =  [ "program", "declaration", "assignacion", "expression", 
                   "printstmt", "statements", "comparation", "ifstatement" ]

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
    Name=10
    Numero=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(marzoParser.DeclarationContext,i)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.StatementsContext)
            else:
                return self.getTypedRuleContext(marzoParser.StatementsContext,i)


        def getRuleIndex(self):
            return marzoParser.RULE_program

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

        localctx = marzoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==marzoParser.T__0:
                    self.state = 16
                    self.declaration()
                    self.state = 21
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << marzoParser.T__3) | (1 << marzoParser.T__5) | (1 << marzoParser.Name) | (1 << marzoParser.Numero))) != 0):
                    self.state = 22
                    self.statements()
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << marzoParser.T__3) | (1 << marzoParser.T__5) | (1 << marzoParser.Name) | (1 << marzoParser.Numero))) != 0):
                    self.state = 28
                    self.statements()
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==marzoParser.T__0:
                    self.state = 34
                    self.declaration()
                    self.state = 39
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclaracionContext(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Name(self):
            return self.getToken(marzoParser.Name, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)



    def declaration(self):

        localctx = marzoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            localctx = marzoParser.DeclaracionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(marzoParser.T__0)
            self.state = 43
            self.match(marzoParser.Name)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_assignacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignContext(AssignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.AssignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Name(self):
            return self.getToken(marzoParser.Name, 0)
        def Numero(self):
            return self.getToken(marzoParser.Numero, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def assignacion(self):

        localctx = marzoParser.AssignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignacion)
        try:
            localctx = marzoParser.AssignContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(marzoParser.Name)
            self.state = 46
            self.match(marzoParser.T__1)
            self.state = 47
            self.match(marzoParser.Numero)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class PrimariaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Numero(self):
            return self.getToken(marzoParser.Numero, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaria" ):
                listener.enterPrimaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaria" ):
                listener.exitPrimaria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaria" ):
                return visitor.visitPrimaria(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = marzoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = marzoParser.PrimariaContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 50
            self.match(marzoParser.Numero)
            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = marzoParser.SumaContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 52
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 53
                    self.match(marzoParser.T__2)
                    self.state = 54
                    self.expression(3) 
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrintstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Numero(self):
            return self.getToken(marzoParser.Numero, 0)

        def getRuleIndex(self):
            return marzoParser.RULE_printstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintstmt" ):
                listener.enterPrintstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintstmt" ):
                listener.exitPrintstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintstmt" ):
                return visitor.visitPrintstmt(self)
            else:
                return visitor.visitChildren(self)




    def printstmt(self):

        localctx = marzoParser.PrintstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(marzoParser.T__3)
            self.state = 61
            self.match(marzoParser.Numero)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifstatement(self):
            return self.getTypedRuleContext(marzoParser.IfstatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)


        def printstmt(self):
            return self.getTypedRuleContext(marzoParser.PrintstmtContext,0)


        def assignacion(self):
            return self.getTypedRuleContext(marzoParser.AssignacionContext,0)


        def getRuleIndex(self):
            return marzoParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = marzoParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statements)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [marzoParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.ifstatement()
                pass
            elif token in [marzoParser.Numero]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.expression(0)
                pass
            elif token in [marzoParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.printstmt()
                pass
            elif token in [marzoParser.Name]:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.assignacion()
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


    class ComparationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(marzoParser.Name, 0)

        def Numero(self):
            return self.getToken(marzoParser.Numero, 0)

        def getRuleIndex(self):
            return marzoParser.RULE_comparation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparation" ):
                listener.enterComparation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparation" ):
                listener.exitComparation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparation" ):
                return visitor.visitComparation(self)
            else:
                return visitor.visitChildren(self)




    def comparation(self):

        localctx = marzoParser.ComparationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comparation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(marzoParser.Name)
            self.state = 70
            self.match(marzoParser.T__4)
            self.state = 71
            self.match(marzoParser.Numero)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_ifstatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfConElseContext(IfstatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.IfstatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comparation(self):
            return self.getTypedRuleContext(marzoParser.ComparationContext,0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.StatementsContext)
            else:
                return self.getTypedRuleContext(marzoParser.StatementsContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfConElse" ):
                listener.enterIfConElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfConElse" ):
                listener.exitIfConElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfConElse" ):
                return visitor.visitIfConElse(self)
            else:
                return visitor.visitChildren(self)


    class IfSinElseContext(IfstatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.IfstatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comparation(self):
            return self.getTypedRuleContext(marzoParser.ComparationContext,0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.StatementsContext)
            else:
                return self.getTypedRuleContext(marzoParser.StatementsContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfSinElse" ):
                listener.enterIfSinElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfSinElse" ):
                listener.exitIfSinElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfSinElse" ):
                return visitor.visitIfSinElse(self)
            else:
                return visitor.visitChildren(self)



    def ifstatement(self):

        localctx = marzoParser.IfstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifstatement)
        self._la = 0 # Token type
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = marzoParser.IfSinElseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(marzoParser.T__5)
                self.state = 74
                self.comparation()
                self.state = 75
                self.match(marzoParser.T__6)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << marzoParser.T__3) | (1 << marzoParser.T__5) | (1 << marzoParser.Name) | (1 << marzoParser.Numero))) != 0):
                    self.state = 76
                    self.statements()
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 82
                self.match(marzoParser.T__7)
                pass

            elif la_ == 2:
                localctx = marzoParser.IfConElseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(marzoParser.T__5)
                self.state = 85
                self.comparation()
                self.state = 86
                self.match(marzoParser.T__6)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << marzoParser.T__3) | (1 << marzoParser.T__5) | (1 << marzoParser.Name) | (1 << marzoParser.Numero))) != 0):
                    self.state = 87
                    self.statements()
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 93
                self.match(marzoParser.T__7)
                self.state = 94
                self.match(marzoParser.T__8)
                self.state = 95
                self.match(marzoParser.T__6)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << marzoParser.T__3) | (1 << marzoParser.T__5) | (1 << marzoParser.Name) | (1 << marzoParser.Numero))) != 0):
                    self.state = 96
                    self.statements()
                    self.state = 101
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 102
                self.match(marzoParser.T__7)
                pass


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
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




