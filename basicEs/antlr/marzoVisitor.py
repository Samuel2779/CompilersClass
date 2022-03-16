# Generated from d:\Escuela\Semestre_8\Compiladores\GitHubClass\CompilersClass\basicEs\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete generic visitor for a parse tree produced by marzoParser.

class marzoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by marzoParser#program.
    def visitProgram(self, ctx:marzoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#declaracion.
    def visitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#assign.
    def visitAssign(self, ctx:marzoParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#suma.
    def visitSuma(self, ctx:marzoParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#primaria.
    def visitPrimaria(self, ctx:marzoParser.PrimariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#printstmt.
    def visitPrintstmt(self, ctx:marzoParser.PrintstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#statements.
    def visitStatements(self, ctx:marzoParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#comparation.
    def visitComparation(self, ctx:marzoParser.ComparationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#ifSinElse.
    def visitIfSinElse(self, ctx:marzoParser.IfSinElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#ifConElse.
    def visitIfConElse(self, ctx:marzoParser.IfConElseContext):
        return self.visitChildren(ctx)



del marzoParser