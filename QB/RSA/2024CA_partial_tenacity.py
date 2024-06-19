"""
with open('output.txt', 'w') as f:
    f.write(f'n = {cipher.key.n}\n')
    f.write(f'ct = {enc_flag.hex()}\n')
    f.write(f'p = {str(cipher.key.p)[::2]}\n')
    f.write(f'q = {str(cipher.key.q)[1::2]}')
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import myRSA


class RSACipher:
    def __init__(self, bits):
        self.key = RSA.generate(bits)
        self.cipher = PKCS1_OAEP.new(self.key)

    def encrypt(self, m):
        return self.cipher.encrypt(m)

    def decrypt(self, c):
        return self.cipher.decrypt(c)


cipher = RSACipher(1024)

n = 118641897764566817417551054135914458085151243893181692085585606712347004549784923154978949512746946759125187896834583143236980760760749398862405478042140850200893707709475167551056980474794729592748211827841494511437980466936302569013868048998752111754493558258605042130232239629213049847684412075111663446003
ct = "7f33a035c6390508cee1d0277f4712bf01a01a46677233f16387fae072d07bdee4f535b0bd66efa4f2475dc8515696cbc4bc2280c20c93726212695d770b0a8295e2bacbd6b59487b329cc36a5516567b948fed368bf02c50a39e6549312dc6badfef84d4e30494e9ef0a47bd97305639c875b16306fcd91146d3d126c1ea476"
p = 151441473357136152985216980397525591305875094288738820699069271674022167902643
q = 15624342005774166525024608067426557093567392652723175301615422384508274269305

# m = cipher.decrypt(bytes.fromhex(ct))
def restore_key(n, e, p, q):
    # Compute d and u
    phi = (p-1) * (q-1)
    d = pow(e, -1, phi)
    u = pow(p, -1, q)

    # Create the RSA key object
    key = RSA.construct((n, e, p, q))

    return key


print(myRSA.query_factors(n))
