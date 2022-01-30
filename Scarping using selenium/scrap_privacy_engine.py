from webbrowser import get
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://blog.privacyengine.io/"

response = requests.get(url)
print(response.status_code)

page_content = response.text
# with open('page.html','w') as f:
#     f.write(page_content[:1000])

doc = BeautifulSoup(page_content,'html.parser')
h2_title_tags = doc.find_all('h2')
# print(h2_title_tags[:2])
links_of_blog = []
h20 = h2_title_tags[0]
for i in range(len(h2_title_tags)):
    for c in h2_title_tags[i].children:
        links_of_blog.append(c['href'])
# print(links_of_blog)

topic_desc = doc.find_all('div',{'class':'full-width post-listing-summary-wrap'})
# print(topic_desc[1].text.strip())
listof_topic_desc = [i.text.strip() for i in topic_desc]
# print(listof_topic_desc)

titles = [i.text.strip() for i in h2_title_tags]
# print(titles)

data_dict = {'Title':titles,
                'Description':listof_topic_desc,
                'URL':links_of_blog}
data_df = pd.DataFrame(data_dict)
# print(data_df)

# data_df.to_csv('privacy_data.csv')

resposnse1 = requests.get(links_of_blog[0])
# print(resposnse1.status_code)
page_doc = BeautifulSoup(resposnse1.text,'html.parser')
