from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd



chrome_options = Options()
chrome_options.add_argument("--user-data-dir=/Users/parkermccoog/selenium-profile")
chrome_options.add_argument("--headless=new")
service = Service()

print("Starting script", flush=True)
driver = webdriver.Chrome(service=service, options=chrome_options)
df = pd.read_csv("TodayMagLinks.csv")
newdf = pd.DataFrame(columns=["link", "Year", "Date", "Title", "Text"])
article_links = set()
for num in range(len(df)):
    issue_url = df["link"][num]
    print(issue_url)
    driver.get(issue_url)

    time.sleep(0.5)

    link_elements = driver.find_elements(By.TAG_NAME, "a")



    for elem in link_elements:
        href = elem.get_attribute("href")

        if href:
            #print(href)
            if "https://www.christianitytoday.com/" in href:
                if len(href.split("/")[3]) == 4 and str.isnumeric(href.split("/")[3]) and href != issue_url and href not in article_links:
                    article_links.add((href))
                    newdf.loc[len(newdf)] = {"link" : href, "Year": df["Year"][num], "Date": df["Date"][num], "Title": href.split("/")[-2].replace("-", " "), "Text": ''}
                    print(href)

    print(newdf)
newdf.to_csv('TodayArts.csv', index = False)
