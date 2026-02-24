from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=/Users/parkermccoog/selenium-profile")

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
df = pd.DataFrame(columns=["link", "Year", "Date", "Title", "Text"])
exclude = {"https://mycharisma.com/article/#content",
"https://mycharisma.com/article/#",
"https://mycharisma.com/article/%7B%7BSUBSCRIBE_URL%7D%7D",
"https://mycharisma.com/article/%7B%7BLOGIN_URL%7D%7D",
"https://mycharisma.com/article/"}
article_links = set()
for i in range(47):
    url = f"https://mycharisma.com/article/page/{i+1}/"
    print("Link:", url)
    driver.get(url)
    time.sleep(0.5)

    link_elements = driver.find_elements(By.TAG_NAME, "a")



    for elem in link_elements:
        href = elem.get_attribute("href")

        if href:
            #print(href)
            if "https://mycharisma.com/article/" in href and "/page/" not in href:
                if href != url and href not in article_links and href not in exclude:
                    article_links.add((href))
                    df.loc[len(df)] = {"link" : href, "Year": None, "Date": None, "Title": None, "Text": None}
                    print(href)
    print(df)
df.to_csv("CharismaArts.csv", index = False)
