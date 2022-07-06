from bs4 import BeautifulSoup
import requests


URL = "https://lgcnews.com/"

r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')

mydivs = soup.findAll("h3", {"class": "elementor-post__title"})
links = mydivs[0].find("a",href=True)
news = links["href"]

n = requests.get(news)

latest = BeautifulSoup(n.content,'html5lib')

# page = latest.find('div',{"class":"elementor-widget-container"})
title = latest.find('h1',{"class":"elementor-heading-title elementor-size-default"}).get_text()
page = latest.select("body > div.elementor.elementor-54794.elementor-location-single.post-60332.post.type-post.status-publish.format-standard.has-post-thumbnail.hentry.category-north_cyprus_news > div > section > div > div > div.elementor-column.elementor-col-66.elementor-top-column.elementor-element.elementor-element-f8053ad > div > div > div.elementor-element.elementor-element-f040d1c.elementor-widget.elementor-widget-theme-post-content > div")[0].get_text()



# content =page.find("p").getText()
# print(title)
formdata = {"section":"Blog","articletitle":title,"articles":page,"author":"LGC News"}
guideagent = 'http://localhost/api/postnews'

website = requests.post(guideagent, data=formdata)
print(website)