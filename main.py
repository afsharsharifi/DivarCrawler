import json
import urllib.request

import requests
from bs4 import BeautifulSoup

BASE = "https://divar.ir/s/"
CITY = "tehran"
CATEGORY = "game-consoles"

# REQUEST URL => https://divar.ir/s/tehran/game-consoles
# PAGINATION => https://divar.ir/s/tehran/game-consoles?page=1

page = 1
while True:
    r = requests.get(f'{BASE}{CITY}/{CATEGORY}')
    print(r)
    soup = BeautifulSoup(r.content, "html.parser")
    div_res = soup.find_all("div", class_="post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46")
    res = []
    for d_res in div_res:
        res.append(d_res.find("a"))
    page = page + 1
    for item in res:
        divar_item = item["href"].rsplit("/")[-1]
        print(divar_item)
        with urllib.request.urlopen(f"https://api.divar.ir/v5/posts/{divar_item}") as url:
            data = json.loads(url.read().decode())
            print(data["widgets"]["contact"]["phone"])
