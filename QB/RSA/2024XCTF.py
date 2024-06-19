from Crypto.Util.number import *

n = 1000
gamma = 0.42
beta = 0.25


N = 0xbe9ccc83003bedf45421b58377b946f87dfd85be82124dc5d732070d77ef68e0231c3f34dc803a8984de0573db6d83ccea0bd53a885059a10cfa3764c658c4d42c5fa90ecad8573fff8f2c41e513278c59121e42ad83310fb22b4d20e7ada42c76f08891f38c92a1b1aac712bfa7d717a4c4802ed023f12c768972ca1b
e = 0x5dc97ed7250e57ce6fac4f57885c0538b1ea540fbaca79730470b6b990f7e861adc4c5fee3acdcd9ae9a2834b606ddfae01ade33edfa96a47a0ffc0036a4497a84c38b7cdac20c38f


def keyGen(n, gamma):
    g = getPrime(round(n * gamma))
    while True:
        a, b = 2, 2
        while GCD(a, b) != 1:
            a = getRandomNBitInteger(round((.5 - gamma) * n - 1))
            b = getRandomNBitInteger(round((.5 - gamma) * n - 1))
        p, q, h = 2 * g * a + 1, 2 * g * b + 1, 2 * g * a * b + a + b
        if isPrime(p) and isPrime(q) and isPrime(h):
            break
    return p, q, g, a, b

p, q, g, a, b = keyGen(n, gamma)
d = getPrime(round(n * beta))
e = inverse(d, 2 * g * a * b)