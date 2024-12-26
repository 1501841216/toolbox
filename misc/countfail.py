dir = "C:\\Users\\15018\\Downloads\\misc-2\\3、日志分析\\"
dir2 = "C:\\Users\\15018\\Downloads\\misc-4\\6\\"

count = 0
str = 'Failed'
str2 = '"root"'
str3 = '" 404'
table = 'abcdefghijklmnopqrstuvwxyz'

# f2 = open('new',"a")
# for i in table:
#     for j in table:
#         # print(i+j)
#         if (i+j == 'lu'):
#             break
#         else:
#             f = open(dir + "log" + i + j,"r")
#             for line in f.readlines():
#                 f2.write(line)
f = open("new","r")
for line in f:
        if str2 in line:
            count += 1
print(count)


# for i in table:
#     for j in table:
#         # print(i+j)
#         if (i+j == 'iy'):
#             print(count)
#             break
#         else:
#             f = open(dir2 + "log" + i + j,"r")
#             for line in f.readlines():
#                 if str3 in line:
#                     count += 1
