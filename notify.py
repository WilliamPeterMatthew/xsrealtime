import requests
import config
import re
import time
from bs4 import BeautifulSoup as BSf

import warnings
warnings.filterwarnings("ignore")

userinfo={"uname":config.botloginname,"password":config.botpassword,"tfa":"","csrfToken":""}
session=requests.Session()
session.verify = False
# session.verify = 'cppucert.cer'

def task(alist,text):
    response=session.post(url=config.loginurl,data=userinfo)
    notifiednum=0
    for x in alist:
        data={"operation":"send","uid":int(x),"content":text}
        response=session.post(url=config.messageurl,data=data)
        notifiednum+=1
    print("Notified",notifiednum,"users.")
    response=session.post(url=config.logouturl,data={})

text=""
textsel=int(input("文本内容↓\n0)自定义\n1)来自文件\n请输入："))
if textsel==1 :
    tf=open("text.txt",mode="r",encoding="utf-8")
    text=tf.read()+"\n（此消息为单向通知，请勿在系统上回复，如需帮助请联系工作人员。）"

if textsel==0 :
    text=input("请输入通知内容：\n")+"\n（此消息为单向通知，请勿在系统上回复，如需帮助请联系工作人员。）"

notsel=int(input("通知范围↓\n0)自定义\n1)C/Cpp组\n2)Py组\n3)全部组\n请输入："))
notrange=[]
if notsel&1 :
    cpp=open("cpp.txt",mode="r",encoding="utf-8")
    notrange+=eval(cpp.read())

if notsel&2 :
    py=open("py.txt",mode="r",encoding="utf-8")
    notrange+=eval(py.read())

if notsel==0 :
    notrange=eval(input("请输入范围（Python List）：\n"))

task(notrange,text)
