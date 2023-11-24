key = \
    'The life that I have' \
    'Is all that I have' \
    'And the life that I have' \
    'Is yours.' \
    'The love that I have' \
    'Of the life that I have' \
    'Is yours and yours and yours.' \
    'A sleep I shall have' \
    'A rest I shall have' \
    'Yet death will be but a pause.' \
    'For the peace of my years' \
    'In the long green grass' \
    'Will be yours and yours and yours.'

key2 = [
    [
        ['The life that I have'],
        ['Is all that I have'],
        ['And the life that I have'],
        ['Is yours.']
    ],
    [
        ['The love that I have'],
        ['Of the life that I have'],
        ['Is yours and yours and yours.']
    ],
    [
        ['A sleep I shall have'],
        ['A rest I shall have'],
        ['Yet death will be but a pause.']
    ],
    [
        ['For the peace of my years'],
        ['In the long green grass'],
        ['Will be yours and yours and yours.']
    ]
]

cipher = 'emzcf sebt yuwi ytrr ortl rbon aluo konf ihye cyog rowh prhj feom ihos perp twnb tpak heoc yaui usoa irtd tnlu ntke onds goym hmpq'
print(len(cipher.strip()))
c_l = cipher.split()
print(len(key2))
str = ''
i=1
for elem in c_l:
        segm = key2[(ord(elem[0])-i)%len(key2)]
        line = segm[(ord(elem[1])-i)%len(segm)]
        line_l = line[0].split()
        word = line_l[(ord(elem[2])-i)%len(line_l)]
        char = word[(ord(elem[3])-i)%len(word)]
        str += char

print(str)

