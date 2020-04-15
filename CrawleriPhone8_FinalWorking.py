#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


# In[27]:
linkCSV='iPhone8withCMT.csv'

def get_html_link(url):
    try:
        new_url = url[:url.rfind(".html")]
        new_url=(str(new_url+'.html')).strip()
    except:
        print('Trich chuoi loi')
    return new_url

#Functiom: Crawler Comment
def data_review(url):
    lst = []
    lst_loc = []
    try:
        driver = webdriver.Chrome(executable_path="/Users/anhnhat/Downloads/archives/chromedriver")
        driver.get(url)
    except:
        print('Connection Error')
    try:
        end_html = driver.find_element_by_xpath(
            "html/body/section[@class='container']/section[@class='wrap_sidebar_12']/section[@class='bottom_detail']/div[@id='box_comment_vne']/div[@class='box_comment_vne width_common']/div[@class='view_more_coment width_common mb10']/a")
        time.sleep(2)
        actions = ActionChains(driver)
    # actions.click(end_html)
    
        actions.move_to_element(end_html).click().perform()
    except:
        print('Khong co element')
    time.sleep(2)

    try:
        content_element = driver.find_element_by_xpath(
            "html/body/section[@class='container']/section[@class='wrap_sidebar_12']/section[@class='bottom_detail']/div[@id='box_comment_vne']/div[@class='box_comment_vne width_common']/div[@class='width_common']/div[@id='list_comment']")
        content_html = content_element.get_attribute("innerHTML")
        soup = BeautifulSoup(content_html, "html.parser")
        p_tags = soup.find_all("p", {"class": "full_content"})
        for p in p_tags:
            lst.append(p.text)
        for x in lst:
            if x not in lst_loc:
                lst_loc.append(x)
        if (lst == []):
            lst_loc.append(" ")
    except:
        print("Error")
    driver.close()
    if (len(lst_loc) == 0):
        lst_loc.append('null')
    return lst_loc



# In[ ]:


# Tạo ra một list chứa source:
srciPhone11=[]
countPages=1
cmtStr=''
test=['https://vnexpress.net/tag/iphone-8-545643','https://vnexpress.net/tag/iphone-8-545643-p2']
for i in test:
    requestsPages = requests.get(i)
    pagesSoup = BeautifulSoup(requestsPages.text, "html.parser")
    for link in pagesSoup.findAll('a', attrs={'href': re.compile("https://vnexpress.net/so-hoa/")}):
        srciPhone11.append(link.get('href'))
srciPhone11 = list(dict.fromkeys(srciPhone11))
#print(srciPhone11)
print(type(srciPhone11))

records = []  # khai báo list để lưu

#
for link in srciPhone11:
    #print(link)
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    #r = requests.get('https://vnexpress.net/so-hoa/nguoi-trung-quoc-coi-viec-dung-iphone-la-dang-xau-ho-3987272.html')
#soup = BeautifulSoup(r.text, "html.parser")
    #results_time = soup.find_all('span', attrs={'class': 'time left'})
    #dateNew=results_time[0]
    #dateNews=dateNew.contents[0:-2]
    #dateNews=dateNews[0]
#Tìm tiêu đề
    results_title = soup.find_all('h1', attrs={'class': 'title_news_detail mb10'})
    titleNews=results_title[0]
#print(first_title.contents[0])

#Tìm description

    #results_description = soup.find_all('p', attrs={'class': 'description'})
    #decription_News=results_description[0]
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

    link=get_html_link(link)
    # Lấy dữ liệu comment xuống
    s=''
    lstthem=data_review(link)
    lst.append(lstthem)
    print(lstthem)
    _strCmt=[]
    for i in lstthem:
        _strCmt=i;
        # s=s+i+"\\c"
    print(s)
    _product='AppleiPhone8'
    rank=''
    # Xuất ra file csv qua Pandas
    for i in range(len(lstthem)):
            records.append((rank,lstthem[i],_product,titleNews,linkNews))
            df = pd.DataFrame(records, columns=['rank','comment','_product','title','link'])
            df.to_csv(linkCSV, index=False, encoding='utf-8-sig')


def checkDuplicate(linkCSV):
    device_cols = ['rank','comment','_product','title','link']
    data = pd.read_csv("iPhone8withCMT.csv")
    data = data.drop_duplicates(keep='first')
    data.to_csv(linkCSV, index=False, encoding='utf-8-sig')

# In[ ]:




