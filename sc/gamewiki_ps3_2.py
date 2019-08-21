import requests
from bs4 import BeautifulSoup

r = requests.get("https://www26.atwiki.jp/gcmatome/pages/24.html")

soup = BeautifulSoup(r.content, "html.parser")
# ltd=soup.find_all("td")
l=soup.select('td a')
box=[]
for a in l:
     if a is not None:
         box.append(a)


with open("ps3.txt",mode="w",encoding="utf-8") as f:
    for b in box:
        f.write("{}\n".format(b.getText()))
#result = [line for line in lines_strip if 'title' in line]
#for a in result:
    #print(a)
