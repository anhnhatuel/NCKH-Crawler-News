#!/usr/bin/env python
# coding: utf-8

# In[18]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import codecs
from selenium.webdriver.common.action_chains import ActionChains


# In[50]:


URL= 'https://vnexpress.net/so-hoa/suc-manh-chup-thieu-sang-cua-iphone-11-pro-3988184.html'
def data_review(url):
    lst=[]
    lst_loc=[]
    try:
        driver = webdriver.Chrome(executable_path="/Users/anhnhat/Downloads/archives/chromedriver")
        driver.get(url)
    except:
        print('Connection Error')
        
    #end_html= driver.find_element_by_xpath("html/body/section[@class='container']/section[@class='wrap_sidebar_12']/section[@class='bottom_detail']")
    time.sleep(7)
    #actions = ActionChains(driver)
    #actions.move_to_element(end_html).click().perform()
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
    return lst_loc


# In[ ]:


lst=data_review(URL)
print(lst)

# In[ ]:


lst


# In[51]:





# In[52]:





# In[ ]:




