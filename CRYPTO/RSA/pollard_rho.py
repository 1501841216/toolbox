# wangdingcup baihu
# crypto02 rsa

from Crypto.Util.number import long_to_bytes, bytes_to_long
import myRSA
nbits = 2048
gbits = 1000
# g = getPrime(int(gbits))
# a = int(nbits*0.5)-gbits
# # print(a)
# p = 2*g*a +1
# print(len(str(p)))

n = 49025724928152491719950645039355675823887062840095001672970308684156817293484070166684235178364916522473822184239221170514602692903302575847326054102901449806271709230774063675539139201327878971370342483682454617270705142999317092151456200639975738970405158598235961567646064089356496022247689989925574384915789399433283855087561428970245448888799812611301566886173165074558800757040196846800189738355799057422298556992606146766063202605288257843684190291545600282197788724944382475099313284546776350595539129553760118549158103804149179701853798084612143809757187033897573787135477889183344944579834942896249251191453
e = 65537
cfile = open('F:\\CTF\\CTFQD\\games\\2024wdcup\\2024网鼎白虎\\crypto\\7f03e33a7ee0805bd173fc6447a70b83\\cipher.txt','rb')
c = bytes_to_long(cfile.read())
# print(c)
# temp = gmpy2.iroot(c, 2)[0]
# p = gmpy2.next_prime(temp)
# q = n // p


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def mapx(x):
    x=(pow(x,n-1,n)+3)%n    #pow(x,n-1,n)是为了减小数值，加速运算，
    return x

def pollard_rho (x1,x2):
    while True:
        x1=mapx(x1)
        x2=mapx(mapx(x2))
        p=gcd(x1-x2,n)
        if (p == n):
            print("fail")
            return
        elif (p!=1):
            print("p: "+str(p))
            print("q: "+str(n//p))
            break

def main():
    pollard_rho(1,1)
    return

# main()
p = 270739053411293468044358005572326880715866131246316305975150551797771999927260913691624449594733673350641598358977228099278925982221096409496197961213452575581038864123668037331549492912118266914139408344450017736857756347795681452284667629499583154669046006953194443040693208729068117415444168170452989294079
q = 181081097501198023069853833182353184261284123229534078254107942099502325869566163846505417960576038861954213847321685798395883194037860319430010178354074600519049325312842897561278830450748961589667396822373094094674865532726953310816962745801088563041800719074771895743022649725941252134035150899684475275107
m = myRSA.pqec_4_m(p,q,e,c)
print(m)