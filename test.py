input_str = input("请输入 x y （使用空格分割）")

try:
    num1, num2 = map(int, input_str.split())
except:
    print("输入无效，请重新输入")
