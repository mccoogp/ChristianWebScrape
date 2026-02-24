from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

df = pd.DataFrame(columns=["link", "Year", "Date"])


chrome_options = Options()
chrome_options.add_argument("--user-data-dir=/Users/parkermccoog/selenium-profile")

service = Service()

print("Starting script", flush=True)
driver = webdriver.Chrome(service=service, options=chrome_options)
for year in range(1956, 2027):
    url = f"https://www.christianitytoday.com/magazine/{year}/"
    driver.get(url)

    time.sleep(2)

    issue_links = driver.find_elements(By.CSS_SELECTOR, f"main a[href*='/magazine/{year}/']")

    all_urls = set()

    for link in issue_links:
        href = link.get_attribute("href")
        if f"/magazine/{year}/" in href and href not in all_urls:
            last = href.split('/')[-1]
            if last != "?c=1":
                all_urls.add(href)
                df.loc[len(df)] = {"link" : href, "Year": year, "Date": href.split('/')[-2]}


    print(f"Found issue URLs for {year}:")
    for issue_url in sorted(all_urls):
        print(issue_url)
    print(df)

print(df)
df.to_csv('TodayMagLinks.csv', index = False)