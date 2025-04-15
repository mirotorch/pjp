from antlr_gen.ProjectGrammarVisitor import ProjectGrammarVisitor
from antlr_gen.ProjectGrammarParser import ProjectGrammarParser

class CodeGenerator(ProjectGrammarVisitor):
    def __init__(self, types):
        self.instructions = []
        self.types = types
        self.label_counter = 0
    
    def visitProgram(self, ctx):
        for stat in ctx.stat():
            self.visit(stat)

    def visitDeclaration(self, ctx):
        declared_type = ctx.primitiveType().getText()
        for ident in ctx.IDENTIFIER():
            var_name = ident.getText()
            self.types[var_name] = declared_type

    def visitAssignment(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        expr_ctx = ctx.expr()

        if isinstance(expr_ctx, ProjectGrammarParser.AssignmentContext):
            self.visit(expr_ctx)
            self.emit(f"load {expr_ctx.IDENTIFIER().getText()}")
            self.emit(f"save {var_name}")
        else:
            expr_type = self.visit(expr_ctx)
            self.emit(f"save {var_name}")
            return expr_type
    
    def visitBlock(self, ctx):
        for stat in ctx.stat():
            self.visit(stat)
    
    def visitId(self, ctx):
        self.emit(f"load {ctx.getText()}")
        var_type = self.types.get(ctx.getText())
        if not var_type:
            raise Exception('unknown variable')
        return var_type
    
    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitSimpleExpr(self, ctx):
        return self.visit(ctx.expr())
    
    def visitEmptyStatement(self, ctx):
        pass


    # simple types
    def visitInt(self, ctx):
        value = ctx.getText()
        self.emit(f"push I {value}")
        return 'int'

    def visitChar(self, ctx):
        value = ctx.getText()
        self.emit(f"push C {value}")
        return 'char'

    def visitString(self, ctx):
        value = ctx.getText()
        self.emit(f"push S {value}")
        return 'string'

    def visitFloat(self, ctx):
        value = ctx.getText()
        self.emit(f"push F {value}")
        return 'float'
    
    def visitBool(self, ctx):
        value = ctx.getText()
        self.emit(f"push B {value}")
        return 'bool'

    def visitFile(self, ctx):
        value = ctx.getText()
        self.emit(f"push L {value}")
        return 'FILE'

    # operators
    def visitAddSub(self, ctx):
        t1, t2 = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        t = self.to_code_type(self.promote(t1, t2))
        if op == '+':
            self.emit(f"add {t}")
        else:
            self.emit(f"sub {t}")
        return self.promote(t1, t2)

    def visitMulDiv(self, ctx):
        t1, t2 = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        t = self.to_code_type(self.promote(t1,t2))
        if op == '*':
            self.emit(f"mul {t}")
        else:
            self.emit(f"div {t}")
        return self.promote(t1, t2)
        
    def visitModExpr(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.emit("mod")
        return 'int'

    def visitUnaryMinus(self, ctx):
        type = self.visit(ctx.expr())
        self.emit(f"uminus {type}")
        return type

    def visitConcatExpr(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.emit("concat")
        return 'string'

    def visitAndExpr(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.emit("and")
        return 'bool'

    def visitOrExpr(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.emit("or")
        return 'bool'

    def visitNotExpr(self, ctx):
        self.visit(ctx.expr())
        self.emit("not")
        return 'bool'

    # comparison
    def visitComparison(self, ctx):
        left, right = ctx.expr(0),  ctx.expr(1)
        t1, t2 = self.visit(left), self.visit(right)
        t = self.promote(t1, t2)

        op = ctx.getChild(1).getText()
        if op == '==':
            if t == 'int':
                self.emit("eq I")
            elif t == 'float':
                self.emit("eq F")
            elif t == 'string':
                self.emit("eq S")
            elif t == 'char':
                self.emit("eq C")
            elif t == 'bool':
                self.emit("eq B")
            else:
                raise Exception(f"Unsupported type for eq: {t}")
        elif op == '!=':
            if t == 'int':
                self.emit("eq I")
            elif t == 'float':
                self.emit("eq F")
            elif t == 'string':
                self.emit("eq S")
            elif t == 'char':
                self.emit("eq C")
            elif t == 'bool':
                self.emit("eq B")
            else:
                raise Exception(f"Unsupported type for neq: {t}")
            self.emit("not")
        elif op == '<':
            self.emit(f"lt {self.to_numeric(t)}")
        elif op == '>':
            self.emit(f"gt {self.to_numeric(t)}")
        elif op == '<=':
            self.emit(f"gt {self.to_numeric(t)}")
            self.emit("not")
        elif op == '>=':
            self.emit(f"lt {self.to_numeric(t)}")
            self.emit("not")
        else:
            raise Exception(f"Unknown comparison operator: {op}")
        return 'bool'

    # IO operators
    def visitRead(self, ctx):
        targets = [ctx.expr(0)] + list(ctx.expr()[1:])
        for target in targets:
            var_name = target.getText()
            var_type = self.types.get(var_name)
            if not var_type:
                raise Exception(f"Unknown variable in read: {var_name}")
            
            code_type = self.to_code_type(var_type)
            self.emit(f"read {code_type}")
            self.emit(f"save {var_name}")
    
    def visitWrite(self, ctx):
        count = len(ctx.expr())
        for expr in ctx.expr():
            self.visit(expr)
        self.emit(f"print {count}")

    def visitFileOpen(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        self.visit(ctx.expr())
        self.emit(f"save {var_name}")

    def visitFileWrite(self, ctx):
        self.emit(f"load {ctx.IDENTIFIER().getText()}")
        count = len(ctx.expr())
        for expr in ctx.expr():
            self.visit(expr)
        self.emit(f"fwrite {count}")

    # jumps and labels
    def visitIfElse(self, ctx):
        else_label = self.new_label()
        end_label = self.new_label() if ctx.stat(1) else else_label

        self.visit(ctx.expr())
        self.emit(f"fjmp {else_label}")
        self.visit(ctx.stat(0))

        if ctx.stat(1):  # else exists
            self.emit(f"jmp {end_label}")
            self.emit(f"label {else_label}")
            self.visit(ctx.stat(1))
            self.emit(f"label {end_label}")
        else:
            self.emit(f"label {else_label}")

    def visitWhileLoop(self, ctx):
        start_label = self.new_label()
        end_label = self.new_label()

        self.emit(f"label {start_label}")
        self.visit(ctx.expr())
        self.emit(f"fjmp {end_label}")
        self.visit(ctx.stat())
        self.emit(f"jmp {start_label}")
        self.emit(f"label {end_label}")

    # utilities
    def emit(self, code):
        self.instructions.append(code)

    def new_label(self):
        self.label_counter += 1
        return self.label_counter

    def to_numeric(self, t):
        match t:
            case 'int': return 'I'
            case 'float': return 'F'
            case _: raise Exception(f"Unsupported type for comparison: {t}")
    
    def to_code_type(self, t):
        match t:
            case 'int': return 'I'
            case 'float': return 'F'
            case 'string': return 'S'
            case 'char': return 'C'
            case 'bool': return 'B'
            case 'FILE': return 'L'

    def infer_type(self, expr):
        if hasattr(expr, "getText"):
            text = expr.getText()
            if text in self.types:
                return self.types[text]
            elif text.isdigit():
                return "I"
            elif text.replace('.', '', 1).isdigit():
                return "F"
            elif text in ("true", "false"):
                return "B"
            elif text.startswith('"'):
                return "S"
            elif text.startswith("'"):
                return "C"
        return "I"  # default value
    
    def promote(self, t1, t2):
        if (t1 == 'float' and t2 == 'int') or (t2 == 'float' and t1 == 'int'):
            return 'float'
        if t1 == t2:
            return t1
        raise Exception(f"Incompatible types: {t1} and {t2}")

    def get_code(self):
        return self.instructions
