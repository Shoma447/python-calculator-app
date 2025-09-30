import tkinter as tk

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "エラー")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# メインウィンドウ
root = tk.Tk()
root.title("電卓アプリ")

# 入力欄
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# ボタン配置
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

# メインループ
root.mainloop()
