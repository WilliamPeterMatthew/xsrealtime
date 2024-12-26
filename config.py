ojdomain="https://oj.cppu.edu.cn/"
subdomain="jcdx20XXxs"
domain=ojdomain+"d/"+subdomain+"/"

loginurl=domain+"login"
logouturl=domain+"logout"
messageurl=domain+"home/messages"

starttime=XXXXXXXXXX

contests=["xxxxxxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxxxxxx"]

scoreboardurls=[]
for i in contests:
    scoreboardurls.append(domain+"contest/"+i+"/scoreboard?page=")

recordurls=[]
for i in contests:
    recordurls.append(domain+"record?tid="+i+"&page=")

botloginname="xxxxx"
botpassword="xxxxxxxxx"
