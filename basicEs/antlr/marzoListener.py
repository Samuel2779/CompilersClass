# Generated from d:\Escuela\Semestre_8\Compiladores\GitHubClass\CompilersClass\basicEs\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete listener for a parse tree produced by marzoParser.
class marzoListener(ParseTreeListener):

    # Enter a parse tree produced by marzoParser#program.
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        pass

    # Exit a parse tree produced by marzoParser#program.
    def exitProgram(self, ctx:marzoParser.ProgramContext):
        pass


    # Enter a parse tree produced by marzoParser#declaracion.
    def enterDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by marzoParser#declaracion.
    def exitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by marzoParser#assign.
    def enterAssign(self, ctx:marzoParser.AssignContext):
        pass

    # Exit a parse tree produced by marzoParser#assign.
    def exitAssign(self, ctx:marzoParser.AssignContext):
        pass


    # Enter a parse tree produced by marzoParser#suma.
    def enterSuma(self, ctx:marzoParser.SumaContext):
        pass

    # Exit a parse tree produced by marzoParser#suma.
    def exitSuma(self, ctx:marzoParser.SumaContext):
        pass


    # Enter a parse tree produced by marzoParser#primaria.
    def enterPrimaria(self, ctx:marzoParser.PrimariaContext):
        pass

    # Exit a parse tree produced by marzoParser#primaria.
    def exitPrimaria(self, ctx:marzoParser.PrimariaContext):
        pass


    # Enter a parse tree produced by marzoParser#printstmt.
    def enterPrintstmt(self, ctx:marzoParser.PrintstmtContext):
        pass

    # Exit a parse tree produced by marzoParser#printstmt.
    def exitPrintstmt(self, ctx:marzoParser.PrintstmtContext):
        pass


    # Enter a parse tree produced by marzoParser#statements.
    def enterStatements(self, ctx:marzoParser.StatementsContext):
        pass

    # Exit a parse tree produced by marzoParser#statements.
    def exitStatements(self, ctx:marzoParser.StatementsContext):
        pass


    # Enter a parse tree produced by marzoParser#comparation.
    def enterComparation(self, ctx:marzoParser.ComparationContext):
        pass

    # Exit a parse tree produced by marzoParser#comparation.
    def exitComparation(self, ctx:marzoParser.ComparationContext):
        pass


    # Enter a parse tree produced by marzoParser#ifSinElse.
    def enterIfSinElse(self, ctx:marzoParser.IfSinElseContext):
        pass

    # Exit a parse tree produced by marzoParser#ifSinElse.
    def exitIfSinElse(self, ctx:marzoParser.IfSinElseContext):
        pass


    # Enter a parse tree produced by marzoParser#ifConElse.
    def enterIfConElse(self, ctx:marzoParser.IfConElseContext):
        pass

    # Exit a parse tree produced by marzoParser#ifConElse.
    def exitIfConElse(self, ctx:marzoParser.IfConElseContext):
        pass



del marzoParser