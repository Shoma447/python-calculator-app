def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "ゼロ除算エラー"
    return x / y

def calculator():
    print("関数版電卓 (終了するには q を入力)")
    while True:
        op = input("演算子を入力 (+, -, *, / または q): ")
        if op.lower() == "q":
            print("終了します。")
            break

        try:
            x = float(input("1つ目の数: "))
            y = float(input("2つ目の数: "))

            if op == "+":
                print("結果:", add(x, y))
            elif op == "-":
                print("結果:", sub(x, y))
            elif op == "*":
                print("結果:", mul(x, y))
            elif op == "/":
                print("結果:", div(x, y))
            else:
                print("無効な演算子です")
        except ValueError:
            print("数字を入力してください")

if __name__ == "__main__":
    calculator()
