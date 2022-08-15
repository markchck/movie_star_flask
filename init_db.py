from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbMovieStar

import requests
from bs4 import BeautifulSoup

urls = []
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rpeople.nhn',headers=headers)

def get_url():
  # 타겟 URL을 읽어서 HTML를 받아오고

  # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
  soup = BeautifulSoup(data.text, 'html.parser')
  trs = soup.select("#old_content > table > tbody > tr")
  base_url = 'https://movie.naver.com'
  for tr in trs:
    title = tr.select_one('td.title > a')
    if title is not None:
      image_url = title['href']
      url = base_url + image_url
      urls.append(url)
      
def url_detail():
  for url in urls:
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    star_info = soup.select_one("#content > div.article > div.mv_info_area")
    name = star_info.select_one('div.mv_info.character > h3 > a').text
    image = star_info.select_one('div.poster > img')['src']
    # print(name, image)
    doc = {
      'name': name, 'image': image, 'url' : url, 'like': 0
    }
    db.movie_star.insert_one(doc)
    print('완료', name)

def insert_all():
  db.movie_star.drop()
  get_url()
  url_detail()

insert_all()

# stars = list(db.movie_star.find({}))
# print(stars)
