import tkinter as tk

current_expression = ""  # 入力中の数式

def on_click(button_text):
    global current_expression

    if button_text == "=":
        try:
            result = calculate(current_expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            current_expression = str(result)  # 次の計算に使えるように更新
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "エラー")
            current_expression = ""
    elif button_text == "C":
        entry.delete(0, tk.END)
        current_expression = ""
    else:
        current_expression += button_text
        entry.insert(tk.END, button_text)

def calculate(expression):
    """四則演算を処理する関数（evalは使わない）"""
    import re
    tokens = re.findall(r"\d+|\+|\-|\*|\/", expression)  # 数字と演算子に分割

    if not tokens:
        return 0

    # まず掛け算・割り算を処理
    i = 0
    while i < len(tokens):
        if tokens[i] in ("*", "/"):
            left = float(tokens[i-1])
            right = float(tokens[i+1])
            if tokens[i] == "*":
                value = left * right
            else:
                value = left / right
            tokens[i-1:i+2] = [str(value)]
            i -= 1
        i += 1

    # 足し算・引き算を処理
    result = float(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        num = float(tokens[i+1])
        if op == "+":
            result += num
        elif op == "-":
            result -= num
        i += 2

    return result

# --- GUI 部分 ---
root = tk.Tk()
root.title("電卓アプリ（安全版）")

entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"],
]

for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        button = tk.Button(
            root, text=button_text, width=5, height=2,
            font=("Arial", 18),
            command=lambda text=button_text: on_click(text)
        )
        button.grid(row=i+1, column=j)

root.mainloop()
