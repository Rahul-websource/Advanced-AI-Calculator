import math
import tkinter as tk
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
            # ✅ dynamically call UI for financial calculators
            getattr(self, f"{key.lower()}_ui")()
        elif key == "Exit":
            self.root.destroy()
        else:
            self.expression += str(key)
            self.input_text.set(self.expression)

    # ----------------------------------------------------------
    # 🧮 Core Math Functions
    # ----------------------------------------------------------
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

    # ----------------------------------------------------------
    # 🧠 Memory Operations
    # ----------------------------------------------------------
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

    # ----------------------------------------------------------
    # 💰 Simple & Compound Interest Calculator
    # ----------------------------------------------------------
    def interest_ui(self):
        top = tk.Toplevel(self.root)
        top.title("Interest Calculator")
        top.geometry("320x280")
        top.config(bg="#222")

        tk.Label(top, text="Principal Amount (₹):", bg="#222", fg="white").pack(pady=5)
        p_entry = tk.Entry(top)
        p_entry.pack(pady=5)

        tk.Label(top, text="Rate of Interest (% per year):", bg="#222", fg="white").pack(pady=5)
        r_entry = tk.Entry(top)
        r_entry.pack(pady=5)

        tk.Label(top, text="Time (in years):", bg="#222", fg="white").pack(pady=5)
        t_entry = tk.Entry(top)
        t_entry.pack(pady=5)

        mode = tk.StringVar(value="Simple")
        tk.Radiobutton(top, text="Simple Interest", variable=mode, value="Simple",
                       bg="#222", fg="white", selectcolor="#333").pack(pady=3)
        tk.Radiobutton(top, text="Compound Interest", variable=mode, value="Compound",
                       bg="#222", fg="white", selectcolor="#333").pack(pady=3)

        def calculate_interest():
            try:
                P = float(p_entry.get())
                R = float(r_entry.get())
                T = float(t_entry.get())

                if mode.get() == "Simple":
                    SI = (P * R * T) / 100
                    total = P + SI
                    messagebox.showinfo("Result", f"Simple Interest = ₹{round(SI, 2)}\nTotal Amount = ₹{round(total, 2)}")
                else:
                    A = P * ((1 + (R / 100)) ** T)
                    CI = A - P
                    messagebox.showinfo("Result", f"Compound Interest = ₹{round(CI, 2)}\nTotal Amount = ₹{round(A, 2)}")
            except Exception:
                messagebox.showerror("Error", "Please enter valid numeric values.")

        tk.Button(top, text="Calculate", bg="#ff9500", fg="white", font=("Arial", 12, "bold"),
                  command=calculate_interest).pack(pady=10)

    # ----------------------------------------------------------
    # 🏦 Loan EMI Calculator
    # ----------------------------------------------------------
    def loan_ui(self):
        top = tk.Toplevel(self.root)
        top.title("Loan EMI Calculator")
        top.geometry("320x260")
        top.config(bg="#222")

        tk.Label(top, text="Loan Amount (₹):", bg="#222", fg="white").pack(pady=5)
        p_entry = tk.Entry(top)
        p_entry.pack(pady=5)

        tk.Label(top, text="Annual Interest Rate (%):", bg="#222", fg="white").pack(pady=5)
        r_entry = tk.Entry(top)
        r_entry.pack(pady=5)

        tk.Label(top, text="Loan Tenure (years):", bg="#222", fg="white").pack(pady=5)
        y_entry = tk.Entry(top)
        y_entry.pack(pady=5)

        def calc_emi():
            try:
                P = float(p_entry.get())
                R = float(r_entry.get())
                Y = float(y_entry.get())

                monthly_rate = R / (12 * 100)
                n = Y * 12
                if monthly_rate == 0:
                    emi = P / n
                else:
                    emi = P * monthly_rate * ((1 + monthly_rate) ** n) / (((1 + monthly_rate) ** n) - 1)

                messagebox.showinfo("Result", f"Monthly EMI = ₹{round(emi, 2)}")
            except Exception:
                messagebox.showerror("Error", "Invalid input values!")

        tk.Button(top, text="Calculate EMI", bg="#28a745", fg="white", font=("Arial", 12, "bold"),
                  command=calc_emi).pack(pady=10)

    # ----------------------------------------------------------
    # 📊 ROI Calculator
    # ----------------------------------------------------------
    def roi_ui(self):
        top = tk.Toplevel(self.root)
        top.title("ROI Calculator")
        top.geometry("320x220")
        top.config(bg="#222")

        tk.Label(top, text="Gain Amount (₹):", bg="#222", fg="white").pack(pady=5)
        gain_entry = tk.Entry(top)
        gain_entry.pack(pady=5)

        tk.Label(top, text="Cost Amount (₹):", bg="#222", fg="white").pack(pady=5)
        cost_entry = tk.Entry(top)
        cost_entry.pack(pady=5)

        def calc_roi():
            try:
                gain = float(gain_entry.get())
                cost = float(cost_entry.get())

                if cost == 0:
                    raise ZeroDivisionError
                roi = ((gain - cost) / cost) * 100
                messagebox.showinfo("Result", f"ROI = {round(roi, 2)}%")
            except Exception:
                messagebox.showerror("Error", "Please enter valid numeric values!")

        tk.Button(top, text="Calculate ROI", bg="#007bff", fg="white", font=("Arial", 12, "bold"),
                  command=calc_roi).pack(pady=10)
