from webbrowser import get
import requests
from bs4 import BeautifulSoup
import urllib.request
import json


phone_number = input("Enter Your Phone Number => ")
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
    'accept-language': 'en-IR,en;q=0.9,fa-US;q=0.8,fa;q=0.7,en-US;q=0.6,ar;q=0.5',
    "referer": 'https://divar.ir/',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'origin': 'https://divar.ir',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
}


def StatusCodeMessage(status_code):
    if status_code == 200:
        print("Success")
    else:
        print("Faild")


with requests.Session() as s:
    # Entering phone number
    data_authenticate = {'phone': phone_number}
    result_authenticate = s.post('https://api.divar.ir/v5/auth/authenticate', json=data_authenticate, headers=headers)
    StatusCodeMessage(result_authenticate.status_code)

    # Entering verifaction code
    confirm_code = input("Enter the code that Divar send => ")
    data_confirm = {
        'phone': phone_number,
        'code': confirm_code
    }
    result_confirm = s.post('https://api.divar.ir/v5/auth/confirm', json=data_confirm, headers=headers)
    StatusCodeMessage(result_confirm.status_code)

    # Getting Info of items
    page = 1
    while True:
        req_url = f'https://divar.ir/s/tehran/buy-residential?page={page}'
        r = s.get(req_url)
        soup = BeautifulSoup(r.content, "html.parser")
        res = soup.find_all("a", class_="kt-post-card kt-post-card--outlined kt-post-card--has-chat")
        page = page + 1

        for item in res:
            divar_item = item["href"].rsplit("/")[-1]
            with urllib.request.urlopen(f"https://api.divar.ir/v5/posts/{divar_item}") as url:
                data = json.loads(url.read().decode())
                print(data["widgets"]["contact"]["phone"])
