import os
import requests
from bs4 import BeautifulSoup

query = "연예인"
search_url = f"https://search.imbc.com/news?qt={query}"

download_folder = f"./{query}" # ./연예인

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

response = requests.get(search_url)
soup = BeautifulSoup(response.text, "html.parser")\

uls = soup.find("ul", class_="list-type news-list")
lis = uls.find_all("li")

articles = []
downloaded = 0
for item in lis:
    title = item.find("span", class_="nw_tit ellipsis-multi").text
    description = item.find("span", class_="nw_txt ellipsis-multi").text
    img_url = item.find("img").get("src")
    img_data = requests.get(f"https:{img_url}").content
    # ./태풍/image_1.jpg
    img_name = os.path.join(download_folder, f"image_{downloaded}.jpg")
    downloaded = downloaded + 1
    article = {
        "title" : title,
        "description" : description
    }
    articles.append(article)

    with open(img_name, "wb") as img_file:
        img_file.write(img_data)

print(f"{downloaded}개의 이미지를 다운로드 했습니다")
print(articles)