import requests
import cchardet
from bs4 import BeautifulSoup
from time import sleep

n=0

r = requests.get("https://p.eagate.573.jp/game/eac2dx/infinitas/p/common/info/iidx_mlist.html")
#r.encoding = cchardet.detect(r.content)["encoding"]
#print(r.encoding)

#soup = BeautifulSoup(r.content, "html.parser")
soup = BeautifulSoup(r.content, "lxml")
#l=soup.find_all("td",id="td1")
for tag in soup.find_all('td', id='td1'):
    print(tag.getText())
    n+=1

print(n)
#print(len(l))
#l=soup.select("td id=td1")
#for a in l:
    #print(a.getText())
    #n+=1
