import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
# Tạo ra một list chứa source:
srciPhone11=[]
countPages=1
#for i in range(5):
requestsPages = requests.get('https://vnexpress.net/tag/iphone-7-plus-622590')
pagesSoup =  BeautifulSoup(requestsPages.text, "html.parser")
for link in pagesSoup.findAll('a', attrs={'href': re.compile("https://vnexpress.net/so-hoa/")}):
    srciPhone11.append(link.get('href'))

srciPhone11 = list(dict.fromkeys(srciPhone11))
#print(srciPhone11)
print(srciPhone11)

records = []  # khai báo list để lưu

#
for link in srciPhone11:
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")

#r = requests.get('https://vnexpress.net/so-hoa/nguoi-trung-quoc-coi-viec-dung-iphone-la-dang-xau-ho-3987272.html')
#soup = BeautifulSoup(r.text, "html.parser")
    results_time = soup.find_all('span', attrs={'class': 'time left'})
    dateNew=results_time[0]
    dateNews=dateNew.contents[0:-2]
    dateNews=dateNews[0]
#Tìm tiêu đề
    results_title = soup.find_all('h1', attrs={'class': 'title_news_detail mb10'})
    titleNews=results_title[0]
#print(first_title.contents[0])

#Tìm description

    results_description = soup.find_all('p', attrs={'class': 'description'})
    decription_News=results_description[0]
#print(first_description.contents[0])

#Tìm nội dung

    results_pharagraph = soup.find_all('p', attrs={'class': 'Normal'})
#first_pharagraph=results_pharagraph[0]
#second_pharagraph=results_pharagraph[1]
#print(first_pharagraph.contents[0])
#print(first_pharagraph.contents[1])
#print(first_pharagraph.contents[2])
    lst = []
    for x in results_pharagraph:
        lst.append(x)
    i=0
    chuoi=""
    for number in range(len(lst)):
        content_count = len(lst[number].contents)
        for num_contents in range(content_count):
            chuoi = chuoi+str(lst[number].contents[num_contents])
            i=i+1
#Tìm link bài viết:

    linkNews = soup.find("link",{"rel":"alternate"})['href']
#print(linkNews)

# Lấy dữ liệu comment xuống
# Xuất ra file csv qua Pandas
    records.append((dateNews,titleNews.contents,decription_News.contents,chuoi,linkNews))
    df = pd.DataFrame(records, columns=['date', 'title', 'description', 'content','link'])
    df.to_csv('FinalVNESamsungip7plus.csv', index=False, encoding='utf-8-sig')
    data = pd.read_csv("FinalVNESamsungip7plus.csv")









