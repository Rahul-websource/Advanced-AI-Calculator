import math
from tkinter import messagebox


class CalculatorLogic:
    def click(self, key):
        if key == "AC":
            self.expression = ""
            self.input_text.set("")
        elif key == "CE":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif key == "=":
            self.evaluate()
        elif key == "√":
            self.apply_sqrt()
        elif key == "^":
            self.expression += "**"
            self.input_text.set(self.expression)
        elif key == "x²":
            self.apply_square()
        elif key in ("sin", "cos", "tan", "log", "ln"):
            self.apply_scientific(key)
        elif key == "π":
            self.expression += str(math.pi)
            self.input_text.set(self.expression)
        elif key.startswith("M"):
            self.memory_ops(key)
        elif key in ("Interest", "Loan", "ROI"):
            getattr(self, f"{key.lower()}_ui")()
        elif key == "Exit":
            self.root.destroy()
        else:
            self.expression += str(key)
            self.input_text.set(self.expression)

    def apply_sqrt(self):
        try:
            result = math.sqrt(float(self.expression))
            self.input_text.set(result)
            self.expression = str(result)
        except Exception:
            self.input_text.set("Error")

    def apply_square(self):
        try:
            result = math.pow(float(self.expression), 2)
            self.input_text.set(result)
            self.expression = str(result)
        except Exception:
            self.input_text.set("Error")

    def evaluate(self):
        try:
            expr = self.expression.replace("^", "**")
            result = eval(expr, {"__builtins__": None}, math.__dict__)
            self.input_text.set(result)
            self.expression = str(result)
        except Exception:
            self.input_text.set("Error")
            self.expression = ""

    def apply_scientific(self, func):
        try:
            val = float(self.expression)
            result = {
                "sin": math.sin(math.radians(val)),
                "cos": math.cos(math.radians(val)),
                "tan": math.tan(math.radians(val)),
                "log": math.log10(val),
                "ln": math.log(val)
            }.get(func, 0)
            self.input_text.set(result)
            self.expression = str(result)
        except Exception:
            self.input_text.set("Error")

    def memory_ops(self, op):
        try:
            if op == "M+":
                self.memory += float(self.expression)
                messagebox.showinfo("Memory", f"Added to memory: {self.memory}")
            elif op == "M-":
                self.memory -= float(self.expression)
                messagebox.showinfo("Memory", f"Subtracted from memory: {self.memory}")
            elif op == "MR":
                self.input_text.set(str(self.memory))
                self.expression = str(self.memory)
            elif op == "MC":
                self.memory = 0.0
                messagebox.showinfo("Memory", "Memory cleared.")
        except Exception:
            messagebox.showerror("Error", "Invalid memory operation!")
