import itertools
import numpy as np
from z3 import*

def calculate_total(nums, i):
    total = 0
    power = 1
    for j in range(9):
        total += power * nums[j]
        power *= i
    return total


def find_nums():
    for nums in itertools.product(range(-1000, 1000), repeat=9):  # 这里的范围可能需要根据实际情况进行调整
        nums = list(nums)
        if nums[7] != -80 or nums[6] != -358:  # 第八个和第七个数必须是 -80 和 -358
            continue
        for i in range(-60, 60):
            total = calculate_total(nums, i)
            if (i == 44 or i == 58 or 0 <= i + 37 <= 0x36) and total != 0:
                break
        # if nums[8] != 1 :
        #     for k in range(9):
        #         nums[k] /= nums[8]
        else:  # 如果循环没有被 break，说明找到了正确的九个数
            return nums
    return None

# from scipy.optimize import fsolve
#
# def equations(vars):
#     a, b, c, d, e, f, g = vars
#     eq1 = a*44**8 - 80*44**7 -358*44**6 + b*44**5 + c*44**4 + d*44**3 + e*44**2 + f*44 + g
#     eq2 = a*58**8 - 80*58**7 -358*58**6 + b*58**5 + c*58**4 + d*58**3 + e*58**2 + f*58 + g
#     eq3 = a
#     eq4 = b
#     eq5 = c
#     eq6 = d
#     eq7 = e
#     return [eq1, eq2, eq3, eq4, eq5, eq6, eq7]
#
# # 初始猜测的解
# initial_guess = [1, 1, 1, 1, 1, 1, 1]
# solution = fsolve(equations, initial_guess)
#
# print('a, b, c, d, e, f, g:', solution)

# 创建一个整数向量来表示九个数
# nums = IntVector('nums', 9)
#
# # 创建一个求解器
# s = Solver()
#
# # 添加约束：第八个和第七个数必须是 -80 和 -358
# s.add(nums[7] == -80, nums[6] == -358)
#
# # 添加约束：对于每个 i，如果 i 等于 44 或 58 或 0 <= i + 37 <= 0x36，那么 total 必须等于 0
# # for i in range(-60, 60):
# #     total = sum(nums[j] * i**j for j in range(9))
# #     if i == 44 or i == 58 or 0 <= i + 37 <= 0x36:
# #         s.add(total == 0)
#
# for i in range(-60, 60):
#     s.add(And(nums[0] * i**8 - 80 * i**7 - 358 * i**6 + nums[1] * i**5 + nums[2] * i**4 + nums[3] * i**3 + nums[4] * i**2 + nums[5] * i + nums[6] == 0))
#
# # 求解
# if s.check() == sat:
#     m = s.model()
#     if m is not None:
#         solution = []
#         for i in range(9):
#             if m[nums[i]] is not None:
#                 solution.append(m[nums[i]].as_long())
#             else:
#                 solution.append(None)
#         print('Solution:', solution)
#     else:
#         print('No solution found')
# else:
#     print('No solution found')

# from z3 import *
#
# # 创建一个整数向量来表示九个数
# nums = IntVector('nums', 9)
#
# # 创建一个求解器
# s = Solver()
#
# # 添加约束：第八个和第七个数必须是 -80 和 -358
# s.add(nums[7] == -80, nums[6] == -358)
#
# # 添加约束：两个等式
# s.add(nums[0] * 44**8 - 80 * 44**7 - 358 * 44**6 + nums[1] * 44**5 + nums[2] * 44**4 + nums[3] * 44**3 + nums[4] * 44**2 + nums[5] * 44 + nums[6] == 0)
# s.add(nums[0] * 58**8 - 80 * 58**7 - 358 * 58**6 + nums[1] * 58**5 + nums[2] * 58**4 + nums[3] * 58**3 + nums[4] * 58**2 + nums[5] * 58 + nums[6] == 0)
#
# # 添加约束：i 的范围
# for i in range(-60, 60):
#     s.add(And(nums[0] * i**8 - 80 * i**7 - 358 * i**6 + nums[1] * i**5 + nums[2] * i**4 + nums[3] * i**3 + nums[4] * i**2 + nums[5] * i + nums[6] == 0))
#
# # 求解
# if s.check() == sat:
#     m = s.model()
#     solution = [m[nums[i]].as_long() if m[nums[i]] is not None else None for i in range(9)]
#     print('Solution:', solution)
# else:
#     print('No solution found')

from sympy import symbols, Eq, solve, CRootOf

x = symbols('x')
y = 6*x**8 -80*x**7 -358*x**6 + x**5 + 6*x**4 + 8*x**3 + 5*x**2 + x + 1 - 21
solution = solve(Eq(y, 0), x)

print('Solution:', solution)
for i in range(len(solution)):
    x = symbols('x')
    root = solution[0]

    # 计算根的实际数值
    root_value = root.evalf()

    print('Root value:', root_value)