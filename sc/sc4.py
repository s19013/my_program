import requests
from bs4 import BeautifulSoup
from time import sleep

r = requests.get("https://p.eagate.573.jp/game/eac2dx/infinitas/p/common/info/iidx_mlist.html")
with open("sc.txt",mode="w",encoding="utf-8") as f:
    f.write(r)


# soup = BeautifulSoup(r.content, "html.parser")
# l=soup.find_all("td",id="td1")
# n=0
# for a in l:
#     print(a.getText())
#     n+=1
#     if n%50==0:
#         sleep(1)
#
# print(n)
