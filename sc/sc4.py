import requests
from bs4 import BeautifulSoup

r = requests.get(
    "https://p.eagate.573.jp/game/eac2dx/infinitas/p/common/info/iidx_mlist.html"
)

soup = BeautifulSoup(r.content, "html.parser")
print(soup.text)
l = soup.find_all(id="td1")
n = 0

for a in l:
    # print(a.getText())
    n += 1
# print(n)
