# Generated from SimpleC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleCParser import SimpleCParser
else:
    from SimpleCParser import SimpleCParser

# This class defines a complete listener for a parse tree produced by SimpleCParser.
class SimpleCListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleCParser#prog.
    def enterProg(self, ctx:SimpleCParser.ProgContext):
        pass

    # Exit a parse tree produced by SimpleCParser#prog.
    def exitProg(self, ctx:SimpleCParser.ProgContext):
        pass


    # Enter a parse tree produced by SimpleCParser#topElement.
    def enterTopElement(self, ctx:SimpleCParser.TopElementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#topElement.
    def exitTopElement(self, ctx:SimpleCParser.TopElementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#extern_var_declare.
    def enterExtern_var_declare(self, ctx:SimpleCParser.Extern_var_declareContext):
        pass

    # Exit a parse tree produced by SimpleCParser#extern_var_declare.
    def exitExtern_var_declare(self, ctx:SimpleCParser.Extern_var_declareContext):
        pass


    # Enter a parse tree produced by SimpleCParser#extern_var_define.
    def enterExtern_var_define(self, ctx:SimpleCParser.Extern_var_defineContext):
        pass

    # Exit a parse tree produced by SimpleCParser#extern_var_define.
    def exitExtern_var_define(self, ctx:SimpleCParser.Extern_var_defineContext):
        pass


    # Enter a parse tree produced by SimpleCParser#var_declare.
    def enterVar_declare(self, ctx:SimpleCParser.Var_declareContext):
        pass

    # Exit a parse tree produced by SimpleCParser#var_declare.
    def exitVar_declare(self, ctx:SimpleCParser.Var_declareContext):
        pass


    # Enter a parse tree produced by SimpleCParser#var_declare_statement.
    def enterVar_declare_statement(self, ctx:SimpleCParser.Var_declare_statementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#var_declare_statement.
    def exitVar_declare_statement(self, ctx:SimpleCParser.Var_declare_statementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#var_define.
    def enterVar_define(self, ctx:SimpleCParser.Var_defineContext):
        pass

    # Exit a parse tree produced by SimpleCParser#var_define.
    def exitVar_define(self, ctx:SimpleCParser.Var_defineContext):
        pass


    # Enter a parse tree produced by SimpleCParser#var_define_statement.
    def enterVar_define_statement(self, ctx:SimpleCParser.Var_define_statementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#var_define_statement.
    def exitVar_define_statement(self, ctx:SimpleCParser.Var_define_statementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#arrayInitValueList.
    def enterArrayInitValueList(self, ctx:SimpleCParser.ArrayInitValueListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#arrayInitValueList.
    def exitArrayInitValueList(self, ctx:SimpleCParser.ArrayInitValueListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#function_declare.
    def enterFunction_declare(self, ctx:SimpleCParser.Function_declareContext):
        pass

    # Exit a parse tree produced by SimpleCParser#function_declare.
    def exitFunction_declare(self, ctx:SimpleCParser.Function_declareContext):
        pass


    # Enter a parse tree produced by SimpleCParser#function_define.
    def enterFunction_define(self, ctx:SimpleCParser.Function_defineContext):
        pass

    # Exit a parse tree produced by SimpleCParser#function_define.
    def exitFunction_define(self, ctx:SimpleCParser.Function_defineContext):
        pass


    # Enter a parse tree produced by SimpleCParser#retType.
    def enterRetType(self, ctx:SimpleCParser.RetTypeContext):
        pass

    # Exit a parse tree produced by SimpleCParser#retType.
    def exitRetType(self, ctx:SimpleCParser.RetTypeContext):
        pass


    # Enter a parse tree produced by SimpleCParser#param_list.
    def enterParam_list(self, ctx:SimpleCParser.Param_listContext):
        pass

    # Exit a parse tree produced by SimpleCParser#param_list.
    def exitParam_list(self, ctx:SimpleCParser.Param_listContext):
        pass


    # Enter a parse tree produced by SimpleCParser#param.
    def enterParam(self, ctx:SimpleCParser.ParamContext):
        pass

    # Exit a parse tree produced by SimpleCParser#param.
    def exitParam(self, ctx:SimpleCParser.ParamContext):
        pass


    # Enter a parse tree produced by SimpleCParser#type.
    def enterType(self, ctx:SimpleCParser.TypeContext):
        pass

    # Exit a parse tree produced by SimpleCParser#type.
    def exitType(self, ctx:SimpleCParser.TypeContext):
        pass


    # Enter a parse tree produced by SimpleCParser#constant.
    def enterConstant(self, ctx:SimpleCParser.ConstantContext):
        pass

    # Exit a parse tree produced by SimpleCParser#constant.
    def exitConstant(self, ctx:SimpleCParser.ConstantContext):
        pass


    # Enter a parse tree produced by SimpleCParser#statement.
    def enterStatement(self, ctx:SimpleCParser.StatementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#statement.
    def exitStatement(self, ctx:SimpleCParser.StatementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#assignment_statement.
    def enterAssignment_statement(self, ctx:SimpleCParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#assignment_statement.
    def exitAssignment_statement(self, ctx:SimpleCParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#assignment.
    def enterAssignment(self, ctx:SimpleCParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SimpleCParser#assignment.
    def exitAssignment(self, ctx:SimpleCParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SimpleCParser#if_statement.
    def enterIf_statement(self, ctx:SimpleCParser.If_statementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#if_statement.
    def exitIf_statement(self, ctx:SimpleCParser.If_statementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#if_else_statement.
    def enterIf_else_statement(self, ctx:SimpleCParser.If_else_statementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#if_else_statement.
    def exitIf_else_statement(self, ctx:SimpleCParser.If_else_statementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#while_statement.
    def enterWhile_statement(self, ctx:SimpleCParser.While_statementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#while_statement.
    def exitWhile_statement(self, ctx:SimpleCParser.While_statementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#for_statement.
    def enterFor_statement(self, ctx:SimpleCParser.For_statementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#for_statement.
    def exitFor_statement(self, ctx:SimpleCParser.For_statementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#forExpr.
    def enterForExpr(self, ctx:SimpleCParser.ForExprContext):
        pass

    # Exit a parse tree produced by SimpleCParser#forExpr.
    def exitForExpr(self, ctx:SimpleCParser.ForExprContext):
        pass


    # Enter a parse tree produced by SimpleCParser#break_statement.
    def enterBreak_statement(self, ctx:SimpleCParser.Break_statementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#break_statement.
    def exitBreak_statement(self, ctx:SimpleCParser.Break_statementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#continue_statement.
    def enterContinue_statement(self, ctx:SimpleCParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#continue_statement.
    def exitContinue_statement(self, ctx:SimpleCParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#function_statement.
    def enterFunction_statement(self, ctx:SimpleCParser.Function_statementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#function_statement.
    def exitFunction_statement(self, ctx:SimpleCParser.Function_statementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#return_statement.
    def enterReturn_statement(self, ctx:SimpleCParser.Return_statementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#return_statement.
    def exitReturn_statement(self, ctx:SimpleCParser.Return_statementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#statementBlock.
    def enterStatementBlock(self, ctx:SimpleCParser.StatementBlockContext):
        pass

    # Exit a parse tree produced by SimpleCParser#statementBlock.
    def exitStatementBlock(self, ctx:SimpleCParser.StatementBlockContext):
        pass


    # Enter a parse tree produced by SimpleCParser#function_call.
    def enterFunction_call(self, ctx:SimpleCParser.Function_callContext):
        pass

    # Exit a parse tree produced by SimpleCParser#function_call.
    def exitFunction_call(self, ctx:SimpleCParser.Function_callContext):
        pass


    # Enter a parse tree produced by SimpleCParser#expressionList.
    def enterExpressionList(self, ctx:SimpleCParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#expressionList.
    def exitExpressionList(self, ctx:SimpleCParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#expression.
    def enterExpression(self, ctx:SimpleCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#expression.
    def exitExpression(self, ctx:SimpleCParser.ExpressionContext):
        pass



del SimpleCParser