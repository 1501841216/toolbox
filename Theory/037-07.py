# 找出1到1000之间的孪生素数（相差为2的素数对）


# 判断素数
def is_prime(x):
    for i in range(2, x//2):
        if x % i == 0:
            return 0
            break
    else:
        return 1


# 判断y是否为x的倍数(非1)
def is_times(x, y):
    if x % y == 0 & x != y:
        return 1
    else:
        return 0


# 通过埃拉托斯尼筛选法找出某个范围内的所有素数,不包含max_value
def eratosthenes(max_value):
    temp = []
    primes = []
    for i in range(1, max_value):
        temp.append(i)
    print(temp)
    # int 为向下取整
    for i in range(2, int(max_value**0.5)):
        if is_prime(i) == 1:
            for j in temp:
                if is_times(i, j) == 1:
                    temp.remove(j)
                else:
                    continue
        else:
            continue
    print(primes, len(primes))


eratosthenes(100)



