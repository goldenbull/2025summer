# Generated from SimpleC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleCParser import SimpleCParser
else:
    from SimpleCParser import SimpleCParser

# This class defines a complete generic visitor for a parse tree produced by SimpleCParser.

class SimpleCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleCParser#prog.
    def visitProg(self, ctx:SimpleCParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#topElement.
    def visitTopElement(self, ctx:SimpleCParser.TopElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#extern_var_declare.
    def visitExtern_var_declare(self, ctx:SimpleCParser.Extern_var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#extern_var_define.
    def visitExtern_var_define(self, ctx:SimpleCParser.Extern_var_defineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#var_declare.
    def visitVar_declare(self, ctx:SimpleCParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#var_declare_statement.
    def visitVar_declare_statement(self, ctx:SimpleCParser.Var_declare_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#var_define.
    def visitVar_define(self, ctx:SimpleCParser.Var_defineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#var_define_statement.
    def visitVar_define_statement(self, ctx:SimpleCParser.Var_define_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#arrayInitValueList.
    def visitArrayInitValueList(self, ctx:SimpleCParser.ArrayInitValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#function_declare.
    def visitFunction_declare(self, ctx:SimpleCParser.Function_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#function_define.
    def visitFunction_define(self, ctx:SimpleCParser.Function_defineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#retType.
    def visitRetType(self, ctx:SimpleCParser.RetTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#param_list.
    def visitParam_list(self, ctx:SimpleCParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#param.
    def visitParam(self, ctx:SimpleCParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#type.
    def visitType(self, ctx:SimpleCParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#constant.
    def visitConstant(self, ctx:SimpleCParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#statement.
    def visitStatement(self, ctx:SimpleCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#assignment_statement.
    def visitAssignment_statement(self, ctx:SimpleCParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#assignment.
    def visitAssignment(self, ctx:SimpleCParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#if_statement.
    def visitIf_statement(self, ctx:SimpleCParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#if_else_statement.
    def visitIf_else_statement(self, ctx:SimpleCParser.If_else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#while_statement.
    def visitWhile_statement(self, ctx:SimpleCParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#for_statement.
    def visitFor_statement(self, ctx:SimpleCParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#forExpr.
    def visitForExpr(self, ctx:SimpleCParser.ForExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#break_statement.
    def visitBreak_statement(self, ctx:SimpleCParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#continue_statement.
    def visitContinue_statement(self, ctx:SimpleCParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#function_statement.
    def visitFunction_statement(self, ctx:SimpleCParser.Function_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#return_statement.
    def visitReturn_statement(self, ctx:SimpleCParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#statementBlock.
    def visitStatementBlock(self, ctx:SimpleCParser.StatementBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#function_call.
    def visitFunction_call(self, ctx:SimpleCParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#expressionList.
    def visitExpressionList(self, ctx:SimpleCParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#expression.
    def visitExpression(self, ctx:SimpleCParser.ExpressionContext):
        return self.visitChildren(ctx)



del SimpleCParser