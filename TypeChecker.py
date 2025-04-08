from antlr_gen.ProjectGrammarVisitor import ProjectGrammarVisitor

class TypeChecker(ProjectGrammarVisitor):
    def __init__(self):
        self.symbols = {} 

    def visitProgram(self, ctx):
        for stat in ctx.stat():
            self.visit(stat)

    def visitDeclaration(self, ctx):
        declared_type = ctx.primitiveType().getText()
        for ident in [ctx.IDENTIFIER()] + list(ctx.IDENTIFIER()[1:]):
            try:
                var_name = ident[0].getText()
                if var_name in self.symbols:
                    print(f"Error: variable '{var_name}' already declared.")
                else:
                    self.symbols[var_name] = declared_type
            except:
                var_name = ident.getText()
                if var_name in self.symbols:
                    print(f"Error: variable '{var_name}' already declared.")
                else:
                    self.symbols[var_name] = declared_type

    def visitAssignment(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        if var_name not in self.symbols:
            print(f"Error: variable '{var_name}' not declared.")
            return None
        expr_type = self.visit(ctx.expr())
        var_type = self.symbols[var_name]
        if not (var_type == expr_type or var_type == 'float' and expr_type == 'int'):
            print(f"Type error: cannot assign {expr_type} to {var_type}")
        return var_type
    
    def visitRead(self, ctx):
        # TODO
        return None
    
    def visitWrite(self, ctx):
        # TODO
        return None
    
    def visitIfElse(self, ctx):
        condition = self.visit(ctx.expr())
        if condition != 'bool':
            print(f"Error: condition must be of type 'bool', got '{condition}'")
            return None
        self.visit(ctx.stat(0))
        if ctx.stat(1) is not None:
            self.visit(ctx.stat(1))
        return None

    def visitWhileLoop(self, ctx):
        condition = self.visit(ctx.expr())
        if condition != 'bool':
            print(f"Error: condition must be of type 'bool', got '{condition}'")
            return None
        self.visit(ctx.stat())
        return None

    def visitId(self, ctx):
        name = ctx.IDENTIFIER().getText()
        if name not in self.symbols:
            print(f"Error: variable '{name}' not declared.")
            return None
        return self.symbols[name]

    def visitInt(self, ctx):
        return 'int'

    def visitFloat(self, ctx):
        return 'float'
    
    def visitBool(self, ctx):
        return 'bool'

    def visitChar(self, ctx):
        return 'char'

    def visitString(self, ctx):
        return 'string'

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
    
    def visitNotExpr(self, ctx):
        return self.visit(ctx.expr())
    
    def visitOrExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left != 'bool' or right != 'bool':
            print(f"Type error: cannot apply 'or' to {left} and {right}")
            return None
        return 'bool'
    
    def visitAndExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left != 'bool' or right != 'bool':
            print(f"Type error: cannot apply 'and' to {left} and {right}")
            return None
        return 'bool'    
    
    def visitNotExpr(self, ctx):
        expr_type = self.visit(ctx.expr())
        if expr_type != 'bool':
            print(f"Type error: cannot apply 'not' to {expr_type}")
            return None
        return 'bool'

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return self.promoteType(left, right)

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return self.promoteType(left, right)
    
    def visitUnaryMinus(self, ctx):
        return self.visit(ctx.expr())
    
    def visitComparison(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left != right:
            print(f"Type error: cannot compare {left} and {right}")
            return None
        return 'bool'

    def promoteType(self, t1, t2):
        if t1 == 'float' or t2 == 'float':
            return 'float'
        return 'int'

    def visitSimpleExpr(self, ctx):
        self.visit(ctx.expr())
