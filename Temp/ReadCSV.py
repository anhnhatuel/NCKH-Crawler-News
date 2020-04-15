import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


def data_review(url):
    lst = []
    lst_loc = []
    try:
        driver = webdriver.Chrome(executable_path="/Users/anhnhat/Downloads/archives/chromedriver")
        driver.get(url)
    except:
        print('Connection Error')

    end_html = driver.find_element_by_xpath(
        "html/body/section[@class='container']/section[@class='wrap_sidebar_12']/section[@class='bottom_detail']/div[@id='box_comment_vne']/div[@class='box_comment_vne width_common']/div[@class='view_more_coment width_common mb10']/a")
    time.sleep(1)
    actions = ActionChains(driver)
    # actions.click(end_html)
    try:
        actions.move_to_element(end_html).click().perform()
    except:
        print('khong co xem them')
    time.sleep(1)

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
    if (len(lst) == ''):
        lst_loc = 'null'
    return lst_loc
lst1 = []

data=pd.read_csv('/Users/anhnhat/Documents/UEL/NCKH/De tai khai pha du lieu/Crawl News/iPhone7Plus.csv')
for i in data['link']:
    try:
        lst1 = '\c'.join(data_review(i))
        data.insert(6,'comment', lst1)
        data.to_csv('iPhone7PluswithComment.csv', index=False, encoding='utf-8-sig')
        lst=''
        print(lst1)
    except:
        print('Không thể thực hiện')
        try:
            lst1="null"
            data.insert(0, 'comment', lst1)
            data.to_csv('iPhone7PluswithComment.csv', index=False, encoding='utf-8-sig')
        except:
            print("Bó tay")
