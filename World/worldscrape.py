from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import pandas as pd
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=/Users/parkermccoog/selenium-profile")

service = Service()

print("Starting script", flush=True)
driver = webdriver.Chrome(service=service, options=chrome_options)
print("here", flush=True)
driver.get("https://wng.org/search?production-world-articles%5BrefinementList%5D%5Btype%5D%5B0%5D=articles")
wait = WebDriverWait(driver, 10)

'''
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "authors-list"))
)

author_elements = driver.find_elements(By.CLASS_NAME, "ais-RefinementList-labelText")

#authors = ["the%20editors", "andrée%20seu%20peterson", "joel%20belz", "cal%20thomas", "arsenio%20orteza", "janie%20b.%20cheaney", "gene%20edward%20veith", "megan%20basham", "emily%20belz", "john%20dawson", "lynn%20vincent", "sophia%20lee", "susan%20olasky", "bob%20jones", "chris%20stamper", "alisa%20harris", "mark%20bergin", "d.c.%20innes", "daniel%20james%20devine", "tony%20woodlief", "edward%20e.%20plowman", "collin%20garbarino", "bob%20brow", "anthony%20bradley", "andrew%20coffin", "la%20shawn%20barber", "june%20cheng", "marvin%20olasky", "mindy%20belz", "jamie%20dean"]

urls = set()
for year in range(1990,2026):
    url = f"https://wng.org/search?production-world-articles%5BrefinementList%5D%5Btype%5D%5B0%5D=articles&production-world-articles%5BrefinementList%5D%5Byear%5D%5B0%5D={year}"
    driver.get(url)
    
    filename = "output_file.txt"
    mode = 'w'

    with open(filename, mode, encoding='utf-8') as file:
        file.write(driver.page_source)
    wait.until(EC.presence_of_element_located((By.ID, "authors-list")))
    try:
        show_more = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#authors-list .ais-RefinementList-showMore")))
        show_more.click()
        time.sleep(1)
    except:
        time.sleep(1)



    author_elements = driver.find_elements(By.CSS_SELECTOR, "#authors-list .ais-RefinementList-labelText")

    authors = sorted(set(a.text.strip() for a in author_elements if a.text.strip()))

    print(f"Found {len(authors)} authors:\n", authors, year)
    for author in authors:
        print(author)


        url = f"https://wng.org/search?production-world-articles%5BrefinementList%5D%5Bauthors%5D%5B0%5D={author.replace(' ', '%20')}&production-world-articles%5BrefinementList%5D%5Btype%5D%5B0%5D=articles&production-world-articles%5BrefinementList%5D%5Byear%5D%5B0%5D={year}&production-world-articles%5Bpage%5D="
        
        
        for i in range(50):
            found = False
            driver.get(url + str(i+1))
            links = driver.find_elements(By.TAG_NAME, "a")
            for link in links:
                href = link.get_attribute("href")
                if href and href.startswith("https://wng.org/articles/"):
                    urls.add(href)
                    found = True
            if not found:
                break
    url = f"https://wng.org/search?production-world-articles%5BrefinementList%5D%5Btype%5D%5B0%5D=articles&production-world-articles%5BrefinementList%5D%5Byear%5D%5B0%5D={year}&production-world-articles%5Bpage%5D="
    for i in range(50):
            found = False
            driver.get(url + str(i+1))
            links = driver.find_elements(By.TAG_NAME, "a")
            for link in links:
                href = link.get_attribute("href")
                if href and href.startswith("https://wng.org/articles/"):
                    urls.add(href)
                    found = True
            if not found:
                break

'''

import json



# Reload
with open('urls.json', 'r') as f:
    urls = json.load(f)

df = pd.read_csv("world.csv")
'''
filename = "output_file.txt"
mode = 'w' # Use 'a' to append instead of overwrite

with open(filename, mode, encoding='utf-8') as file:
    file.write(driver.page_source)
    #print(driver.page_source)
'''
count = 0
for repeat in range(10):
    for url in urls[len(df):len(urls)]:

        driver.get(url)
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "article"))
    )

        try:
            title_element = driver.find_element(By.TAG_NAME, "h1")
            title = title_element.text.strip()
        except:
            title = None

        try:
            meta_desc = driver.find_element(By.XPATH, "//meta[@property='og:description']")
            content = meta_desc.get_attribute("content")
            author = content.split("|")[0].strip()
        except:
            author = None

        try:
            date_element = driver.find_element(By.CLASS_NAME, "postDate")
            full_text = date_element.text.strip()

            date_posted = full_text.replace("Post Date:", "").strip()
        except:
            date_posted = None

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

        # print results
        count += 1
        print(count, "Title:", title, date_posted)
        #print("Author:", author)
        #print("Date Posted:", date_posted)
        #print("Body Text:", body_text[:500], "...")
        df.loc[len(df)] = [title, author, date_posted, body_text]

    df.to_csv("world.csv", index=False)
    print("\n\nDownloaded\n\n")

'''
print(len(urls))
with open('set.pkl', 'wb') as f:
    pickle.dump(urls, f)'''