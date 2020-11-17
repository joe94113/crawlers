# import time

import requests
from bs4 import BeautifulSoup

DCARD_URL = "https://www.dcard.tw/f"


def get_web_page(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.text
    else:
        return None


def get_comments(dom):
    soup = BeautifulSoup(dom, 'html.parser')
    name = soup.find('div', 'sc-7fxob4-4 eiOVFy').text
    comment = soup.find('div', 'phqjxq-0 frrmdi').span.text.strip()
    # time.sleep(1)
    return name, comment


def get_data():
    data = {}
    for count in range(900):
        url = f'{DCARD_URL}/trending/p/234780984/b/{count}'
        dom = get_web_page(url)
        if dom is None:
            break
        name, comment = get_comments(dom)
        if name in data:
            data[name].append(comment)
        else:
            data[name] = [comment]
    return data


if __name__ == "__main__":
    data = get_data()
    for d in data:
        print(f"{d} 總留言數{len(data[d])}")
