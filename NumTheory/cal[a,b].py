#064-13 定理十三

import gmpy2
def cal_gcm(a, b):
    mcd = gmpy2.gcd(a, b)
    gcm = a*b/mcd

    return gcm

if __name__ == '__main__':
    print(cal_gcm(23, 19))

