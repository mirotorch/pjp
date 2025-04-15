from Instruction import Instruction
import shlex

class Interpreter:
    def __init__(self, code):
        self.code = code
        self.stack = []
        self.variables = {}
        self.labels = {}
        for i, line in enumerate(self.code):
            tokens = shlex.split(line)
            if tokens and tokens[0] == str(Instruction.LABEL.value):
                self.labels[tokens[1]] = i
        self.ip = 0  # instruction pointer

        self.dispatch = {
            str(Instruction.PUSH.value): self.do_push,
            str(Instruction.POP.value): self.do_pop,
            str(Instruction.ADD.value): lambda args: self.binary_op(lambda x, y: x + y),
            str(Instruction.SUB.value): lambda args: self.binary_op(lambda x, y: x - y),
            str(Instruction.MUL.value): lambda args: self.binary_op(lambda x, y: x * y),
            str(Instruction.DIV.value): lambda args: self.binary_op(lambda x, y: x / y),
            str(Instruction.MOD.value): lambda args: self.binary_op(lambda x, y: x % y),
            str(Instruction.UMINUS.value): self.do_uminus,
            str(Instruction.CONCAT.value): self.do_concat,
            str(Instruction.AND.value): lambda args: self.binary_op(lambda x, y: x and y),
            str(Instruction.OR.value): lambda args: self.binary_op(lambda x, y: x or y),
            str(Instruction.NOT.value): lambda args: self.stack.append(not self.safe_pop()),
            str(Instruction.GT.value): lambda args: self.binary_op(lambda x, y: x > y),
            str(Instruction.LT.value): lambda args: self.binary_op(lambda x, y: x < y),
            str(Instruction.EQ.value): lambda args: self.binary_op(lambda x, y: x == y),
            str(Instruction.PRINT.value): self.do_print,
            str(Instruction.READ.value): self.do_read,
            str(Instruction.SAVE.value): self.do_save,
            str(Instruction.LOAD.value): self.do_load,
            str(Instruction.LABEL.value): self.do_label,
            str(Instruction.JMP.value): self.do_jmp,
            str(Instruction.FJMP.value): self.do_fjmp,
            str(Instruction.FWRITE.value): self.do_fwrite
        }

    def run(self):
        self.runtime = open("run.txt", 'w+')
        while self.ip < len(self.code):
            self.runtime.write(self.code[self.ip] + '\n')
            self.runtime.flush()
            instr, *args = shlex.split(self.code[self.ip])
            handler = self.dispatch.get(instr)
            if handler:
                handler(args)
            else:
                raise RuntimeError(f"Unknown instruction: {instr}")
            self.ip += 1
        self.runtime.close()

    def do_push(self, args):
        typ, val = args

        if typ == 'B':
            self.stack.append(val == 'true')
        elif typ == 'S':
            self.stack.append(val.strip('"'))
        elif typ == 'C':
            self.stack.append(val.strip("'"))
        elif typ == 'F':
            self.stack.append(float(val))
        elif typ == 'I':
            self.stack.append(int(val))
        else:
            raise RuntimeError(f"Unknown type in push: {typ}")

    def do_pop(self, args):
        self.safe_pop()

    def binary_op(self, op):
        right = self.safe_pop()
        left = self.safe_pop()
        self.stack.append(op(left, right))

    def do_uminus(self, args):
        val = self.safe_pop()
        self.stack.append(-val)

    def do_concat(self, args):
        right = self.safe_pop()
        left = self.safe_pop()
        self.stack.append(str(left) + str(right))

    def do_print(self, args):
        count = int(args[0])
        values = [self.safe_pop() for _ in range(count)]
        print(*reversed(values))

    def do_read(self, args):
        t = args[0]
        print(f'Enter {t} value')
        val = input()
        if t == 'I':
            self.stack.append(int(val))
        elif t == 'F':
            self.stack.append(float(val))
        elif t == 'B':
            self.stack.append(val.lower() == 'true')
        elif t == 'S':
            self.stack.append(val)
        else:
            raise RuntimeError(f"Unsupported read type: {t}")

    def do_save(self, args):
        var_name = args[0]
        self.variables[var_name] = self.safe_pop()

    def do_load(self, args):
        var_name = args[0]
        self.stack.append(self.variables[var_name])

    def do_label(self, args):
        pass

    def do_jmp(self, args):
        self.ip = self.labels[args[0]] - 1

    def do_fjmp(self, args):
        condition = self.safe_pop()
        if not condition:
            self.ip = self.labels[args[0]] - 1
    
    def do_fwrite(self, args):
        count = int(args[0])
        values = [self.safe_pop() for _ in range(count)]
        filename = self.safe_pop()
        file = open(filename, 'w+')
        for val in reversed(values):
            file.write(str(val) + '\n')
        file.close()


    def safe_pop(self):
        if not self.stack:
            self.runtime.close()
            raise RuntimeError("Attempt to pop from empty stack")
        return self.stack.pop()
