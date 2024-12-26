import requests
import config
import sysconfig
import re
import time
import random
from bs4 import BeautifulSoup as BSf

import warnings
warnings.filterwarnings("ignore")

userinfo={"uname":config.botloginname,"password":config.botpassword,"tfa":"","csrfToken":""}
session=requests.Session()
session.verify = False
# session.verify = 'cppucert.cer'

sysuserinfo={"loginname":sysconfig.sysloginname,"password":sysconfig.syspassword}
syssess=requests.Session()
syssess.verify = False
# syssess.verify = 'cppucert.cer'

def task():
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    response=session.post(url=config.loginurl,data=userinfo)
    records=[]
    for x in config.recordurls:
        recordpagenum=0
        while 1:
            recordpagenum+=1
            response=session.get(x+str(recordpagenum))
            soup=BSf(response.text,'lxml')
            trs=soup.select('tr')
            nnum=len(trs)
            if nnum<=1:
                break
            for i in range(1,nnum):
                tds=trs[i].select('td')
                st=re.sub(r'[^a-zA-Z0-9]','',tds[2].a.string.strip())
                records.append((trs[i]['data-rid'],tds[0]['class'][2],int(tds[0].select('span')[1].string),tds[1].b.string,st,int(tds[6].span['data-timestamp'])-config.starttime))
        recordpagenum-=1
        print("Read",recordpagenum,"pages.")
    response=session.post(url=config.logouturl,data={})
    sorted_records=sorted(records,key=lambda x:x[5],reverse=True)
    sysres=syssess.post(url=sysconfig.loginurl,data=sysuserinfo)
    if sysconfig.forceupdate:
        sysres=syssess.post(url=sysconfig.forcedelurl,data={})
    nums=0
    preallows=eval(sysconfig.allowrepeat)
    allows=preallows
    print("Try to upload the records, with",preallows,"existing records allowed to be backtracked.")
    for i in sorted_records:
        if i[1]!='pass' and i[1]!='fail':
            continue
        adddata={'data_rid':i[0],'status':i[1],'dscore':i[2],'problemid':i[3],'loginname':i[4],'sendtime':i[5]}
        sysres=syssess.post(url=sysconfig.addurl,data=adddata)
        sysdict=eval(sysres.text)
        if sysdict['code']==2:
            if allows==0:
                break
            allows-=1
        nums+=1
    sysres=syssess.post(url=sysconfig.calcurl,data={})
    print("Added",nums-preallows+allows,"records.")
    sysres=syssess.post(url=sysconfig.logouturl,data={})

while 1:
    task()
    nwtime=eval(sysconfig.sleeptime)
    print("Now sleep",nwtime,"seconds.")
    time.sleep(nwtime)