import requests
from bs4 import BeautifulSoup
from time import sleep
n=0
r = requests.get("https://p.eagate.573.jp/game/eac2dx/infinitas/p/common/info/iidx_mlist.html")


soup = BeautifulSoup(r.content, "html.parser")
l=soup.find_all("td",id="td1")
for a in l:
    print(a.getText())
    n+=1
    if n%50==0:
        sleep(1)

print(n)
