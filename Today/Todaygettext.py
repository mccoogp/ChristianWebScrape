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
driver = webdriver.Chrome(service=service, options=chrome_options)
df = pd.read_csv("TodayArts.csv")
texts = list(df['Text'].fillna(''))
#print(texts)
start = time.time()
for num in range(len(df)):
    if texts[num] == '':
        issue_url = df["link"][num]
        print(issue_url, num)
        driver.get(issue_url)

        time.sleep(0.1)
        body_text = ""
        try:
            article_element = driver.find_element(By.TAG_NAME, "article")
            paragraphs = article_element.find_elements(By.TAG_NAME, "p")
            for p in paragraphs:
                body_text += p.text + "\n"
        except:
            paragraphs = driver.find_elements(By.TAG_NAME, "p")
            for p in paragraphs:
                body_text += p.text + "\n"
        texts[num] = body_text
        if num%100 == 0:
            df["Text"] = texts
            df.to_csv('TodayArts.csv', index = False)
            print("uploaded", time.time()-start)
            start =time.time()
df["Text"] = texts
df.to_csv('TodayArts.csv', index = False)