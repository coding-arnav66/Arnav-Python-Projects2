import tkinter as tk
import math

def add(x):
    equation.append(str(x))
    real_eq = "".join(equation)
    screen.delete("1.0", tk.END)
    screen.insert(tk.END, real_eq)

def clear():
    equation.clear()
    screen.delete("1.0", tk.END)

def delete():
    if equation:
        equation.pop()
        real_eq = "".join(equation)
        screen.delete("1.0", tk.END)
        screen.insert(tk.END, real_eq)

def equals():
    try:
        expr = "".join(equation)

        while "!" in expr:
            idx = expr.index("!")
            j = idx - 1
            while j >= 0 and expr[j].isdigit():
                j -= 1
            num_str = expr[j+1:idx]
            num = int(num_str)
            fact_val = str(math.factorial(num))
            expr = expr[:j+1] + fact_val + expr[idx+1:]


        expr = expr.replace("π",  str(math.pi)+ "*1" )

        result = eval(expr)
        screen.delete("1.0", tk.END)
        screen.insert(tk.END, result)
        equation.clear()
    except Exception:
        screen.delete("1.0", tk.END)
        screen.insert(tk.END, "Error")






root = tk.Tk()
root.title("Arnav's Calculator")
root.geometry("700x600")
root.config(bg="black")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame = tk.Frame(root)
frame.grid(row=2, column=0)

frame.rowconfigure(0, weight=3)
frame.columnconfigure(0, weight=3)
frame.columnconfigure(1, weight=3)
frame.columnconfigure(2, weight=3)

screen = tk.Text(root, font=("Helvetica", 32), height=1,  bg="white", fg="black")
screen.grid(row=0, column=0, rowspan=1, columnspan=4)   

equation = []

buttons = [
    ("1", 0, 0, lambda: add(1), "#FFA500"), ("2", 0, 1, lambda: add(2), "#FFA500"), ("3", 0, 2, lambda: add(3), "#FFA500"),
    ("4", 1, 0, lambda: add(4), "#FFA500"), ("5", 1, 1, lambda: add(5), "#FFA500"), ("6", 1, 2, lambda: add(6), "#FFA500"),
    ("7", 2, 0, lambda: add(7), "#FFA500"), ("8", 2, 1, lambda: add(8), "#FFA500"), ("9", 2, 2, lambda: add(9), "#FFA500"),
    ("0", 3, 1, lambda: add(0), "#FFA500"),

    ("AC", 0, 4, clear, "#39FF14"), ("del", 1, 4, delete, "#39FF14"), ("-", 3, 3, lambda: add("-"), "#39FF14"),
    ("+", 2, 3, lambda: add("+"), "#39FF14"), ("/", 1, 3, lambda: add("/"), "#39FF14"), ("*", 0, 3, lambda: add("*"), "#39FF14"),
    ("=", 2, 4, equals, "#39FF14"), (".", 3, 2, lambda: add("."), "#39FF14"), ("!", 3, 4, lambda: add("!"), "#39FF14"),
    ("π", 3, 0, lambda: add("π"), "#39FF14"), ("\u00B2", 0, 5, lambda : add("**2"), "#39FF14"), ("\u00B3", 1, 5, lambda : add("**3"), "#39FF14"),
    ("^", 2, 5, lambda : add("**"), "#39FF14"), ("√", 3, 5, lambda:add("**0.5"),"#39FF14" )
]

for (text, r, c, cmd, color) in buttons:
    tk.Button(frame, text=text, command=cmd,
        bg=color, fg="black", font=("Helvetica", 14, "bold") ).grid(
        row=r, column=c, sticky="nsew", padx=15, pady=15, ipadx=24, ipady=24
    )

root.mainloop()

