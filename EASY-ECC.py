def add_points(P, Q, a, p):
    if P is None:
        return Q
    if Q is None:
        return P

    x_p, y_p = P
    x_q, y_q = Q

    if P == Q:
        s = ((3 * x_p**2 + a) * pow(2 * y_p, -1, p)) % p
    else:
        s = ((y_q - y_p) * pow(x_q - x_p, -1, p)) % p

    x_r = (s**2 - x_p - x_q) % p
    y_r = (s * (x_p - x_r) - y_p) % p

    return x_r, y_r


def scalar_multiply(d, P, a, p):
    result = None
    while d:
        if d & 1:
            result = add_points(result, P, a, p)
        P = add_points(P, P, a, p)
        d >>= 1
    return result


# 定义椭圆曲线参数和基点


a = 16546484
b = 4548674875
p = 15424654874903
G = (6478678675, 5636379357093)  # 基点坐标 (x, y)

# ECC 密钥生成


private_key = 546768  # 私钥
public_key = scalar_multiply(private_key, G, a, p)  # 公钥

print("Private Key:", private_key)
print("Public Key:", public_key)
print("flag:", public_key[0] + public_key[1] )
