from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd


chrome_options = Options()
chrome_options.add_argument("--user-data-dir=/Users/parkermccoog/selenium-profile")

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)



wait = WebDriverWait(driver, 15)
df = pd.read_csv("CharismaArts.csv")
texts = list(df['Text'])
titles = list(df['Title'])
dates = list(df['Date'])
years = list(df['Year'])
for num in range(len(df)):
    start = time.time()
    url = df["link"][num]
    driver.get(url)
    title = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text

    try:
        publish_date = driver.find_element(By.TAG_NAME, "time").text
    except:
        publish_date = "Not found"

    article = driver.find_element(By.TAG_NAME, "article")
    paragraphs = article.find_elements(By.TAG_NAME, "p")

    text = "\n\n".join([p.text for p in paragraphs if p.text.strip()])


    texts[num] = text
    titles[num] = title
    dates[num] = publish_date
    years[num] = publish_date.split(",")[-1]
    print(num, time.time() - start, title, publish_date)
df["Text"] = texts
df["Date"] = dates
df["Year"] = years
df["Title"] = titles
df.to_csv('Charisma.csv', index = False)
driver.quit()