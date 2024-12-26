# competition:2024ichunqiu_nota_wiener
# filename: signature
import os
import sys
import time
from pwn import *
from ctypes import *
import hashlib
import itertools
from tqdm import *
from Crypto.Util.number import *

p = os.remote('8.147.128.163', 36962)

s = lambda data: p.send(data)
ss = lambda data: p.send(str(data))
sa = lambda delim, data: p.sendafter(str(delim), str(data))
sl = lambda data: p.sendline(data)
sls = lambda data: p.sendline(str(data))
sla = lambda delim, data: p.sendlineafter(str(delim), str(data))
r = lambda num: p.recv(num)
ru = lambda delims, drop=True: p.recvuntil(delims, drop)
itr = lambda: p.interactive()


def main():
    def pass_proof(head):
        password = 'happytheyearofloong'
        table = itertools.product([0, 1], repeat=19)
        for i in tqdm(table):
            getin = ""
            for j in range(len(i)):
                if i[j] == 0:
                    getin += password[j].lower()
                else:
                    getin += password[j].upper()
            msg = getin[:5] + "_" + getin[5:8] + "_" + getin[8:12] + "_" + getin[12:14] + "_" + getin[14:]
            h = hashlib.sha256(msg.encode()).hexdigest()
            if h[:6] == head:
                print(msg)
                return msg

    head = p.recvline().strip().decode().split(" ")[-1]
    msg = pass_proof(head)
    p.recvuntil(b"Plz input your token")
    p.sendlineafter(b">", msg.encode())
    p.recvuntil(b"3.get my key\n")
    p.sendlineafter(b">", b"3")
    (p, q, g) = eval(p.recvline().strip().decode().split("Oh,your key is ")[-1])

    H = []
    R = []
    S = []

    for i in range(8):
        name = b"a" * (i + 1)
        p.recvuntil(b"3.get my key\n")
        p.sendlineafter(b">", b"1")
        p.sendlineafter(b"Username:", name)
        data = p.recvline().strip().decode()
        print(data)
        r = int(data.split(" ")[-1].split(',')[0])
        s = int(data.split(" ")[-1].split(',')[1])
        h = int(halib.sha256(name).hexdigest(), 16)
        R.append(r)
        S.append(s)
        H.append(h)

    def get_k():
        n = len(R)
        r0 = R[0]
        h0 = H[0]
        s0 = S[0]
        A = []
        B = []

        for i in range(n):
            a = inverse((r0 * S[i]), q) * (R[i] * s0) % q
            b = inverse((r0 * S[i]), q) * (H[i] * r0 - h0 * R[i])
            A.append(a)
            B.append(b)

        Ge = Matrix(ZZ, n + 2, n + 2)
        for i in range(n):
            Ge[i, i] = q
            Ge[-2, i] = A[i]
            Ge[-1, i] = B[i]
        K = 2 ** 128
        Ge[-2, -2] = 1
        Ge[-1, -1] = K

        for line in Ge.LLL():
            if abs(line[-1]) == K:
                return line[-2]

    k0 = get_k()
    print(f"k0 = {k0}")
    p.recvuntil(b"3.get my key\n")
    p.sendlineafter(b">", b"2")
    p.recvline()
    x = int(p.recvline().strip().decode())
    r = pow(g, k0, p) % q
    hh = int(hashlib.sha256(b"admin").hexdigest(), 16)
    s = pow(k0, -1, q) * (hh + x * r) % q
    sla(b"r:", str(r).encode())
    sla(b"s:", str(s).encode())
    print(p.recvline().strip().decode())
    print(p.recvline().strip().decode())


if __name__ == "__main__":
    main()