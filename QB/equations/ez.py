from sympy import symbols, Eq, solve

# 定义x为一个符号
x = symbols('x')

# 创建等式
equation = Eq(2*15**2 - 1/x + 15 - 6, 458.875)

# 求解x的值
solution = solve(equation, x)

# 打印结果
print(solution)