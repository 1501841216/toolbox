import requests
import base64
from bs4 import BeautifulSoup
import re
import time

def calc(soup):
    expression = re.search(r'(\d+[\+\-\×\÷]\d+)', soup.string)
    print(expression)
    if expression:
        # 计算结果
        expression = expression.group(1).replace('×', '*').replace('÷', '/')
        result = int(eval(expression))
        print(result)
        return result
    else:
        return None




def get_question_and_post_answer(url):
    # for i in range(50):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    answer = calc(soup)
    data = {'answer': answer}
    res2 = requests.post(url, data=data)
    print(res2.text)

def get_question_and_post_answer2(url,s):
    res =None
    for i in range(52):
        print(f"【Round {i}】")
        if res is None:
            res = s.get(url)
        else:
            res = s.post(url, data={'answer': answer})
            print(res.text)
        soup = BeautifulSoup(res.text, 'html.parser')
        answer = calc(soup)
        res = s.post(url, data={'answer': answer})

def get_question_and_post_answer3(url,s):
    res = s.get(url)
    for i in range(52):
        print(f"【Round {i}】")
        soup = BeautifulSoup(res.text, 'html.parser')
        answer = calc(soup)
        res = s.post(url, data={'answer': answer})
        print(res.text)

url = "http://challenge.basectf.fun:33554"
s = requests.Session()
get_question_and_post_answer2(url,s)

# import requests
#
# url="http://challenge.basectf.fun:33554"
# s = requests.Session()
# response = s.get(url)
# for i in range(51):
#     print(response.text)
#     res=0
#     prob=response.text.split('second ')[1][:-1]
#     if prob.find('÷')!= -1:
#         num=prob.split('÷')
#         res=int(num[0])//int(num[1])
#     else:
#         if prob.find('×') != -1:
#             num = prob.split('×')
#             res = int(num[0]) * int(num[1])
#         else:
#             res= eval(prob)
#     print(res)
#     response = s.post(url, data={'answer': res})