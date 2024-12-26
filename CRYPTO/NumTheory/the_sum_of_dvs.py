# 070-14
# 对某个数a进行素因数分解后，得到其有可能的所有约数，这些约数的和称作d(a)

# 对a进行素因数分解，得到ri和ni，根据r^n + r^n-1 + r^n-2 + ... r^0 = (r^n+1 - 1)/r-1 计算出p，各个p相乘而得.d(a)= Πpi

import sympy as sp


def p_factorization(n):
    i = 2
    lst = []
    dic = dict()
    # 矮找n范围内的素数
    while i*i<=n:
        # 不能整除则下一个
        if n%i:
            i += 1
        else:
            n //= i
            lst.append(i)
            dic.setdefault(i, 0)
            dic[i] += 1

    if n>1:
        # 把最后一个除不尽的也带上
        lst.append(n)
        dic.setdefault(n, 0)
        dic[n] += 1

    # print(dic)
    # print(lst)

    return dic

def cal_p(r, n):
    if type(r) == int:
        p = (r**(n+1) - 1)/(r-1)

# 化简式子
    elif type(r) == str or type(n) == str:
        r, n = sp.symbols('r n')
        expr = (r**(n+1) - 1)/(r-1)
        p = sp.simplify(expr)

    return p


# 判断一个数是完满数与否
def perfect_or_not(num):
    divisors = p_factorization(num)
    sum_of_dvs = 1
    for r, n in divisors.items():
        sum_of_dvs *= cal_p(r,n)
    # print(sum_of_dvs)
    if sum_of_dvs > 2*num:
        print(num,'is abundant')
    elif sum_of_dvs == 2*num:
        print(num, 'is perfect')
    else:
        print(num, 'is deficient')


# print(cal_p(2, 2))
# print(cal_p(2, 'n'))
print(perfect_or_not(18))
# print(p_factorization(24))
for i in range(0, 101):
    perfect_or_not(i)
