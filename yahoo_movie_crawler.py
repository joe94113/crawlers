import requests
import re
import json
from bs4 import BeautifulSoup


Y_MOVIE_URL = 'https://tw.movies.yahoo.com/movie_thisweek.html'

# 以下網址後面加上 "/id=MOVIE_ID" 即為該影片各項資訊
Y_INTRO_URL = 'https://tw.movies.yahoo.com/movieinfo_main.html'  # 詳細資訊
Y_PHOTO_URL = 'https://tw.movies.yahoo.com/movieinfo_photos.html'  # 劇照
Y_TIME_URL = 'https://tw.movies.yahoo.com/movietime_result.html'  # 時刻表


def get_web_page(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_movies(dom):
    soup = BeautifulSoup(dom, 'html5lib')
    movies = []
    rows = soup.find_all('div', 'release_info_text')
    for row in rows:
        movie = list()
        #評價
        movie.append(row.find('div', 'leveltext').span.text.strip())
        #片名
        movie.append(row.find('div', 'release_movie_name').a.text.strip())
        #電影照片
        movie.append(row.parent.find_previous_sibling('div', 'release_foto').a.img['src'])
        #上映日期
        movie.append(get_date(row.find('div', 'release_movie_time').text))
        #介紹
        movie.append(row.find('div', 'release_text').text.replace(u'詳全文', '').strip())
        trailer_a = row.find_next_sibling('div', 'release_btn color_btnbox').find_all('a')[1]
        #電影網址
        movie.append(trailer_a['href'] if 'href' in trailer_a.attrs.keys() else '')
        movies.append(movie)
    return movies


def get_date(date_str):
    # e.g. "上映日期：2017-03-23" -> match.group(0): "2017-03-23"
    pattern = '\d+-\d+-\d+'
    match = re.search(pattern, date_str)
    if match is None:
        return date_str
    else:
        return match.group(0)

def main():
    page = get_web_page(Y_MOVIE_URL)
    if page:
        movies = get_movies(page)
        for movie in movies:
            print(movie)
            # get_complete_intro(movie["movie_id"])


if __name__ == '__main__':
    main()
