import requests
from bs4 import BeautifulSoup as BS
import csv
# import datetime
 
# current_date = datetime.date.today().isoformat()

global_news_list = []
def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BS(html,'lxml')
    data = soup.find('div',class_="Tag")
    tag_articles = data.find('div',class_="Tag--articles")
    tag_article = tag_articles.find_all('div',class_="Tag--article")
    for new in tag_article:
        image = new.find('img')['src']
        news_title = new.find('a',class_="ArticleItem--name")
        news_title_soup = BS(f'{news_title}','lxml')
        title = news_title_soup.a.text
        href_opisanie = new.find('a',class_="ArticleItem--image")
        soup_href = BS(f'{href_opisanie}', 'lxml')
        a_tag = soup_href.find('a')
        href_value = a_tag['href']
        
        data = {
            'title': title.strip(),
            'image': image,
            'href': href_value
        }
        write_list(data)

def write_list(data):
    with open('news_list.csv','a') as file:
        names = ['title','image','href']
        writer = csv.DictWriter(file, delimiter = '|',fieldnames=names)
        writer.writerow(data)    


def main():
    get_data(get_html('https://kaktus.media/?lable=8&date=2023-11-03&order=time'))
    #get_data(get_html(f'https://kaktus.media/?lable=8&date={current_date}&order=time'))

main()