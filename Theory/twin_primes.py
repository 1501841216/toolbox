# 找出1到1000之间的孪生素数（相差为2的素数对）
# 037-07

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
    if y % x == 0 and x != y:
        return 1
    else:
        return 0


# 通过埃拉托斯尼筛选法找出某个范围内的所有素数,不包含max_value
def eratosthenes(max_value):
    temp = []
    # 从2开始，因为任何数都是1的倍数
    for i in range(2, max_value + 1):
        temp.append(i)
    # int 为向下取整
    for i in range(2, int(max_value**0.5) + 1):
        # 寻找n**2范围内的素数，i
        if is_prime(i) == 1:
            for j in temp:
                # 寻找该素数的所有倍数j并去除
                if is_times(i, j) == 1:
                    temp.remove(j)
                else:
                    continue
        else:
            continue
    print(temp)
    print(len(temp))


# 布尔运算的埃拉托斯尼筛选法
def eratosthenes2(n):
    primes = []
    bool_list = [True]*(n+1)
    for prime in range(2, n+1):
        if bool_list[prime]:
            primes.append(prime)
            # 第三个参数为步长
            for i in range(prime*2, n+1, prime):
                bool_list[i] = False
    return primes


# 寻找某个素数集合中的孪生素数
def twin_primes(prime_set, step):
    twins = []
    for i in range(len(prime_set)):
        if prime_set[i] + step in prime_set:
            twins.append((prime_set[i], prime_set[i] + step))
    return twins


def quadruplet(prime_set, step1, step2, step3):
    quad_primes = []
    for i in range(len(prime_set)):
        if prime_set[i] + step1 and\
                prime_set[i] + step2 and\
                prime_set[i] + step3 in prime_set:
            quad_primes.append((prime_set[i],
                                prime_set[i] + step1,
                                prime_set[i] + step2,
                                prime_set[i] + step3))
    return quad_primes


# eratosthenes(1000)
primes = eratosthenes2(1000)
print(primes)
print(len(primes))
print(twin_primes(primes, 2))
print(quadruplet(primes, 2, 6, 8))




