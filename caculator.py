# 计算器程序 - 团队协作项目

def add(a, b):
    """加法函数"""
    return a + b

def subtract(a, b):
    """减法函数"""
    return a - b

def multiply(a, b):
    """乘法函数"""
    return a * b

def main():
    print("欢迎使用计算器")
    result = add(5, 3)
    print(f"5 + 3 = {result}")

    result = multiply(4, 6)
    print(f"4 * 6 = {result}")

if __name__ == "__main__":
    main()