import tkinter as tk
from logic import CalculatorLogic
from utils import round_button, lighten_color
from finance import FinancialFunctions


class Calculator(CalculatorLogic, FinancialFunctions):
    def __init__(self, root):
        self.root = root
        self.root.title("AI-Powered Calculator 🧮")
        self.root.geometry("480x720")
        self.root.minsize(360, 600)
        self.root.configure(bg="#1E1E1E")

        self.expression = ""
        self.memory = 0.0
        self.input_text = tk.StringVar()

        self.create_ui()
        self.make_responsive()

    # ----------------------------------------------------------
    # 🪟 UI Setup
    # ----------------------------------------------------------
    def create_ui(self):
        self.entry_frame = tk.Frame(self.root, bg="#1E1E1E")
        self.entry_frame.pack(fill="x", pady=(20, 10), padx=10)

        self.entry = tk.Entry(
            self.entry_frame,
            textvariable=self.input_text,
            font=("SF Pro Display", 32, "bold"),
            bg="#2B2B2B",
            fg="white",
            bd=0,
            justify="right",
            relief="flat",
            insertbackground="white"
        )
        self.entry.pack(fill="x", ipady=25)
        self.entry.configure(highlightthickness=2, highlightcolor="#3A3A3A")

        # Button Frame
        self.btn_frame = tk.Frame(self.root, bg="#1E1E1E")
        self.btn_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.buttons = [
            ("AC", "#FF5E57"), ("CE", "#FF9F0A"), ("%", "#FF9F0A"), ("/", "#FF9F0A"),
            ("7", "#505050"), ("8", "#505050"), ("9", "#505050"), ("*", "#FF9F0A"),
            ("4", "#505050"), ("5", "#505050"), ("6", "#505050"), ("-", "#FF9F0A"),
            ("1", "#505050"), ("2", "#505050"), ("3", "#505050"), ("+", "#FF9F0A"),
            ("0", "#505050"), (".", "#505050"), ("√", "#505050"), ("=", "#FF9F0A"),
            ("sin", "#333333"), ("cos", "#333333"), ("tan", "#333333"), ("π", "#333333"),
            ("log", "#333333"), ("ln", "#333333"), ("^", "#333333"), ("x²", "#333333"),
            ("M+", "#333333"), ("M-", "#333333"), ("MR", "#333333"), ("MC", "#333333"),
            ("Interest", "#007AFF"), ("Loan", "#007AFF"), ("ROI", "#007AFF"), ("Exit", "#FF3B30")
        ]

        self.button_widgets = []
        row, col = 0, 0
        for (text, color) in self.buttons:
            btn = tk.Button(
                self.btn_frame,
                text=text,
                bg=color,
                fg="white",
                font=("SF Pro Display", 16, "bold"),
                bd=0,
                relief="flat",
                activebackground="#666",
                activeforeground="white",
                command=lambda x=text: self.click(x)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
            round_button(btn)
            self.button_widgets.append(btn)

            col += 1
            if col > 3:
                col = 0
                row += 1

    # ----------------------------------------------------------
    # 📱 Responsiveness
    # ----------------------------------------------------------
    def make_responsive(self):
        for i in range(10):
            self.btn_frame.rowconfigure(i, weight=1)
        for j in range(4):
            self.btn_frame.columnconfigure(j, weight=1)

        def resize_fonts(event):
            width = self.root.winfo_width()
            size = max(14, int(width / 30))
            for btn in self.button_widgets:
                btn.config(font=("SF Pro Display", size, "bold"))
            self.entry.config(font=("SF Pro Display", int(size * 2), "bold"))

        self.root.bind("<Configure>", resize_fonts)
