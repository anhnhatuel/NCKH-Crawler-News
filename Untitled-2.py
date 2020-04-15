#!/usr/bin/env python
# coding: utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import codecs
from selenium.webdriver.common.action_chains import ActionChains


# In[14]:

def get_html_link(url):
    try:
        new_url = url[:url.rfind(".html")]
        new_url=(str(new_url+'.html')).strip()
    except:
        print('Trich chuoi loi')
    return new_url

URL1= 'https://vnexpress.net/so-hoa/luong-nguoi-ban-iphone-8-de-mua-iphone-x-tang-dot-bien-3660420.html?vn_source=Tag&vn_campaign=Stream&vn_medium=Item-42&vn_term=Desktop&vn_thumb=1'
URL= 'https://vnexpress.net/so-hoa/apple-dang-che-giau-su-thieu-sang-tao-3996445.html'
def data_review(url):
    lst=[]
    lst_loc=[]
    try:
        driver = webdriver.Chrome(executable_path="/Users/anhnhat/Downloads/archives/chromedriver")
        driver.get(url)
    except:
        print('Connection Error')
        
    end_html= driver.find_element_by_xpath("html/body/section[@class='container']/section[@class='wrap_sidebar_12']/section[@class='bottom_detail']/div[@id='box_comment_vne']/div[@class='box_comment_vne width_common']/div[@class='view_more_coment width_common mb10']/a")
    time.sleep(2)
    actions = ActionChains(driver)
    #actions.click(end_html)
    try:
        actions.move_to_element(end_html).click().perform()
    except:
        print('khong co xem them')
    time.sleep(2)
    
    try:
        content_element = driver.find_element_by_xpath("html/body/section[@class='container']/section[@class='wrap_sidebar_12']/section[@class='bottom_detail']/div[@id='box_comment_vne']/div[@class='box_comment_vne width_common']/div[@class='width_common']/div[@id='list_comment']")
        content_html = content_element.get_attribute("innerHTML")
        soup = BeautifulSoup(content_html, "html.parser")
        p_tags = soup.find_all("p",{"class":"full_content"})
        for p in p_tags:
            lst.append(p.text)
        for x in lst:
            if x not in lst_loc:
                lst_loc.append(x)
        if(lst==[]):
            lst_loc.append(" ")
    except:
        print("Error")
    driver.close()
    if(len(lst)==''):
        lst_loc='null'
    return lst_loc

lst1=[]
# In[15]:
URL1=get_html_link(URL1)
records=[]
try:
    lst1='\c'.join(data_review(URL1))
except:
    print('Không thể thực hiện')
print(lst1)
records.append(lst1)
df = pd.DataFrame(records, columns=['comment'])
df.to_csv('commenttest.csv', index=False, encoding='utf-8-sig')
# In[13]:

# In[51]:





# In[52]:





# In[ ]:




