"""
题目
p = getPrime(512)
q = getPrime(512)
r = getPrime(512)
n = p * q * r
leak = p * q
e = 0x10001
c = pow(m, e, n)
"""
"""
思路
c = pow(m, e, n)
c = pow(m, e, p * q * r)
c = m^e - k * p * q * r
c modr = m^e
c = m^e mod r
"""
import gmpy2
from Crypto.Util.number import*
c = 173595148273920891298949441727054328036798235134009407863895058729356993814829340513336567479145746034781201823694596731886346933549577879568197521436900228804336056005940048086898794965549472641334237175801757569154295743915744875800647234151498117718087319013271748204766997008772782882813572814296213516343420236873651060868227487925491016675461540894535563805130406391144077296854410932791530755245514034242725719196949258860635915202993968073392778882692892
n = 1396260492498511956349135417172451037537784979103780135274615061278987700332528182553755818089525730969834188061440258058608031560916760566772742776224528590152873339613356858551518007022519033843622680128062108378429621960808412913676262141139805667510615660359775475558729686515755127570976326233255349428771437052206564497930971797497510539724340471032433502724390526210100979700467607197448780324427953582222885828678441579349835574787605145514115368144031247
leak = 152254254502019783796170793516692965417859793325424454902983763285830332059600151137162944897787532369961875766745853731769162511788354655291037150251085942093411304833287510644995339391240164033052417935316876168953838783742499485868268986832640692657031861629721225482114382472324320636566226653243762620647
e = 0x10001
r = n//leak
phi =  r-1
d = gmpy2.invert(e, phi)

print(d)
print(n)

m = pow(c,d,r)
print(m)
print(long_to_bytes(m))