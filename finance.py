import tkinter as tk
from tkinter import messagebox
from utils import create_popup


class FinancialFunctions:
    def compound_interest_ui(self):
        top = create_popup(self.root, "Compound Interest", [("Principal:",), ("Rate (%):",), ("Time (years):",)])
        def calc():
            try:
                P, R, T = map(float, [e.get() for e in top["entries"]])
                A = P * ((1 + R / 100) ** T)
                messagebox.showinfo("Result", f"Compound Amount = {round(A, 2)}")
            except:
                messagebox.showerror("Error", "Invalid input!")
        tk.Button(top["window"], text="Calculate", command=calc, bg="#007AFF", fg="white", font=("SF Pro Display", 12, "bold")).pack(pady=10)

    def loan_ui(self):
        top = create_popup(self.root, "Loan Calculator", [("Principal:",), ("Rate (% per year):",), ("Years:",)])
        def calc():
            try:
                P, R, Y = map(float, [e.get() for e in top["entries"]])
                r = R / 100 / 12
                n = Y * 12
                if r == 0:
                    pay = P / n
                else:
                    pay = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
                messagebox.showinfo("Result", f"Monthly Payment = {round(pay, 2)}")
            except:
                messagebox.showerror("Error", "Invalid input!")
        tk.Button(top["window"], text="Calculate", command=calc, bg="#007AFF", fg="white", font=("SF Pro Display", 12, "bold")).pack(pady=10)

    def roi_ui(self):
        top = create_popup(self.root, "ROI Calculator", [("Gain:",), ("Cost:",)])
        def calc():
            try:
                gain, cost = map(float, [e.get() for e in top["entries"]])
                if cost == 0: raise ZeroDivisionError
                roi = ((gain - cost) / cost) * 100
                messagebox.showinfo("Result", f"ROI = {round(roi, 2)}%")
            except:
                messagebox.showerror("Error", "Invalid input!")
        tk.Button(top["window"], text="Calculate", command=calc, bg="#007AFF", fg="white", font=("SF Pro Display", 12, "bold")).pack(pady=10)
