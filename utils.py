import tkinter as tk


def round_button(button):
    color = button.cget("bg")
    button.configure(highlightthickness=0, borderwidth=0, relief="flat", cursor="hand2")
    button.bind("<Enter>", lambda e: button.config(bg=lighten_color(color, 0.15)))
    button.bind("<Leave>", lambda e: button.config(bg=color))


def lighten_color(color, factor=0.1):
    color = color.lstrip("#")
    r, g, b = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    r = int(r + (255 - r) * factor)
    g = int(g + (255 - g) * factor)
    b = int(b + (255 - b) * factor)
    return f"#{r:02x}{g:02x}{b:02x}"


def create_popup(root, title, labels):
    top = tk.Toplevel(root)
    top.title(title)
    top.geometry("300x250")
    top.configure(bg="#2B2B2B")
    entries = []
    for text, in labels:
        tk.Label(top, text=text, fg="white", bg="#2B2B2B", font=("SF Pro Display", 12)).pack(pady=5)
        e = tk.Entry(top, font=("SF Pro Display", 12), bg="#444", fg="white", relief="flat", insertbackground="white")
        e.pack(pady=5)
        entries.append(e)
    return {"window": top, "entries": entries}
