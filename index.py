import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
postLinks = []
driver.get("https://waitbutwhy.com/")
content = driver.page_source
soup = BeautifulSoup(content)
for element in soup.findAll(attrs={'class': 'read-more'}):
    postLinks.append(element.attrs['href'])

print(postLinks)
resultText = open(
    "/home/popi/Documents/Documents/projetos/webscrapping/text.txt", "w")

driver.get(postLinks[0])
driver.page_source
page = open(
    "/home/popi/Documents/Documents/projetos/webscrapping/page.html", "w")
page.write(driver.page_source)

# for link in postLinks:
#     driver.get(link)
#     linkPage = BeautifulSoup(driver.page_source)
#     page = open(
#         "/home/popi/Documents/Documents/projetos/webscrapping/page.html", "w")
#     page.write(linkPage)
#     textDivWrapper = linkPage.findAll("p")
#     text = []
#     for p in textDivWrapper:
#         text.append(p.text)
#         for p in text:
#             resultText.write("\n")
#             resultText.write(p)
#         resultText.write("\n")
