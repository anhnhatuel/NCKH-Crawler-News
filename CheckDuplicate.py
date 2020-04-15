import pandas as pd

#device_cols=['date', 'title', 'description', 'content', 'link']
device_cols=['comment','link']

data = pd.read_csv("cmt.csv")
data = data.drop_duplicates(keep='first')
data.to_csv('cmt.csv', index=False, encoding='utf-8-sig')

