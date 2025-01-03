import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b
from enum import Enum


class Mode(Enum):
    ECB = 0x01
    CBC = 0x02


class Cipher:
    def __init__(self, key, iv=None):
        self.BLOCK_SIZE = 64
        self.KEY = [b2l(key[i:i + self.BLOCK_SIZE // 16]) for i in range(0, len(key), self.BLOCK_SIZE // 16)]
        self.DELTA = 0x9e3779b9
        self.IV = iv
        if self.IV:
            self.mode = Mode.CBC
        else:
            self.mode = Mode.ECB

    def _xor(self, a, b):
        return b''.join(bytes([_a ^ _b]) for _a, _b in zip(a, b))

    def encrypt(self, msg):
        print(len(msg))
        msg = pad(msg, self.BLOCK_SIZE // 8)
        print(len(msg))
        blocks = [msg[i:i + self.BLOCK_SIZE // 8] for i in range(0, len(msg), self.BLOCK_SIZE // 8)]

        ct = b''
        if self.mode == Mode.ECB:
            for pt in blocks:
                ct += self.encrypt_block(pt)
        elif self.mode == Mode.CBC:
            X = self.IV
            for pt in blocks:
                enc_block = self.encrypt_block(self._xor(X, pt))
                ct += enc_block
                X = enc_block
        print(ct)

        return ct

    def decrypt(self, ct):
        blocks = [ct[i:i + self.BLOCK_SIZE // 8] for i in range(0, len(ct), self.BLOCK_SIZE // 8)]

        pt = b''
        if self.mode == Mode.ECB:
            for c in blocks:
                pt += self.decrypt_block(c)
        elif self.mode == Mode.CBC:
            X = self.IV
            for c in blocks:
                dec_block = self.decrypt_block(c)
                pt += self._xor(X, dec_block)
                X = c

        print(pt)
        print(len(pt))

        return pt

    def encrypt_block(self, msg):
        m0 = b2l(msg[:4])
        m1 = b2l(msg[4:])
        K = self.KEY
        # 创建一个掩码，长度为self.BLOCK_SIZE//2，用于限制m0和m1的长度
        msk = (1 << (self.BLOCK_SIZE // 2)) - 1

        s = 0
        for i in range(32):
            s += self.DELTA
            m0 += ((m1 << 4) + K[0]) ^ (m1 + s) ^ ((m1 >> 5) + K[1])
            m0 &= msk
            m1 += ((m0 << 4) + K[2]) ^ (m0 + s) ^ ((m0 >> 5) + K[3])
            m1 &= msk

        c = ((m0 << (self.BLOCK_SIZE // 2)) + m1) & ((1 << self.BLOCK_SIZE) - 1)  # m = m0 || m1

        return l2b(c)

    def decrypt_block(self, ciphertext):
        c = b2l(ciphertext)
        msk = (1 << (self.BLOCK_SIZE // 2)) - 1

        m1 = c & msk
        m0 = (c >> (self.BLOCK_SIZE // 2)) & msk

        K = self.KEY
        s = self.DELTA * 32

        for i in range(32):
            m1 -= ((m0 << 4) + K[2]) ^ (m0 + s) ^ ((m0 >> 5) + K[3])
            print(m1)
            m1 &= msk
            print(m1)
            m0 -= ((m1 << 4) + K[0]) ^ (m1 + s) ^ ((m1 >> 5) + K[1])
            print(m0)
            m0 &= msk
            s -= self.DELTA

        original_msg = l2b((m0 << 32) + m1)
        return original_msg


if __name__ == '__main__':
    KEY = "850c1413787c389e0b34437a6828a1b2"
    # KEY = "112233445566778899AABBCCDDEEFF11"
    cipher = Cipher(bytes.fromhex(KEY))
    print(bytes.fromhex(KEY))
    ct = "b36c62d96d9daaa90634242e1e6c76556d020de35f7a3b248ed71351cc3f3da97d4d8fd0ebc5c06a655eb57f2b250dcb2b39c8b2000297f635ce4a44110ec66596c50624d6ab582b2fd92228a21ad9eece4729e589aba644393f57736a0b870308ff00d778214f238056b8cf5721a843"
    # ct = "94B1F1E721D5D3525247793D40D1C97F36E7F749C53F70F6AEACFD86F9F06F4EAFD9E2E32B655F7"
    pt = cipher.decrypt(bytes.fromhex(ct))
    print(pt)
    # ct = cipher.encrypt(b"flag{644b1f007a595ec4923b0a7de6fc809a}")
    # print(ct)
    # pt = cipher.decrypt(ct)
    # print(pt)




