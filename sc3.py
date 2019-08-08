import requests
from bs4 import BeautifulSoup

r = requests.get("https://www26.atwiki.jp/gcmatome/pages/24.html")

soup = BeautifulSoup(r.content, "html.parser")

with open(soup) as f:
    lines = f.readlines()

lines_strip = [line.strip() for line in lines]
result = [line for line in lines_strip if 'title' in line]
for line in result:
    print(line)
