import requests
from bs4 import BeautifulSoup

r = requests.get("https://www26.atwiki.jp/gcmatome/pages/24.html")

soup = BeautifulSoup(r.content, "html.parser")
l=soup.find_all("a")
box=[]
for a in l:
    if a is not None:
        box.append(a)

for b in box:
    print(b.getText())
#result = [line for line in lines_strip if 'title' in line]
#for a in result:
    #print(a)
