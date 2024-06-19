c = "!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB"
m = ''
for i in range(len(c)-3, -3, -3):
    m += c[i+1]
    m += c[i]
    m += c[i+2]

print(m)