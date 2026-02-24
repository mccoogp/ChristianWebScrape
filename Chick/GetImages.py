
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd



driver = webdriver.Chrome()

def download_image_requests(image_url, folder_path, file_name):
    os.makedirs(folder_path, exist_ok=True)
    full_path = os.path.join(folder_path, file_name)
    
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        with open(full_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                
        print(f"Image downloaded successfully and saved to: {full_path}")
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to download image from {image_url}: {e}")
    except IOError as e:
        print(f"Failed to save image to file {full_path}: {e}")
df = pd.read_csv('comics.csv')
nums = df["Stock Number"]

links = []
numchecking = len(nums)
url = f'https://www.chick.com/products/tract?stk={int(nums[0])}&ue=d'
driver.get(url)
for item in nums[0:numchecking]:
    linkslocal = []
    num = int(item)
    url = f'https://www.chick.com/products/tract?stk={num}&ue=d'  
    driver.get(url)

    html_content = driver.page_source
    texttofind = '"btn btn-contrast btn-primary filter-btn margin-bottom-10 btn1hide"'
    spot = 0
    for i in range(len(html_content)-len(texttofind)):
        if html_content[i:i+len(texttofind)] == texttofind:
            spot = i
    check = "Select Another Tract"
    if html_content[spot+14+len(texttofind):spot+14+len(texttofind)+len(check)] == check:
        print("working")
        
        spot = 0
        texttofind="/products/category?type=tracts#&&Category=Islam&SortBy=A-Z&PageNumber=1&Language=English&ShowCount=12&Status=Stock"
        for i in range(len(html_content)-len(texttofind)):
            if html_content[i:i+len(texttofind)] == texttofind:
                spot = i
        cat = ""
        n = spot+len(texttofind)+2
        while html_content[n] != "<":
            cat += html_content[n]
            n+=1
        print(cat)


        spot = 0
        for i in range(len(html_content)-len("tracttitle-tp")):
            if html_content[i:i+len("tracttitle-tp")] == "tracttitle-tp":
                spot = i
        title = ""
        n = spot+15
        while html_content[n] != "<":
            title += html_content[n]
            n+=1
        print(title)



        spot = 0
        texttofind = "col-md-12 col-lg-11 removepadding"
        for i in range(len(html_content)-len(texttofind)):
            if html_content[i:i+len(texttofind)] == texttofind:
                spot = i
                break
        n = spot
        for i in range(21):
            texttofind = 'src="/images'
            while True:
                if html_content[n:n+len(texttofind)] == texttofind:
                    break
                n += 1
            srcurl = "https://www.chick.com"
            n +=5
            while html_content[n] != "f":
                srcurl += html_content[n]
                n+=1
            srcurl+="f" 
            save_path = title + str(i) + '.jpg' 
            #folder = title +"-" +cat+ " images"
            folder = title + " images"
            linkslocal.append(srcurl)
            print (srcurl)
    links.append(linkslocal)
for i in range(280-numchecking):
    links.append([])
df["links"] = links    
print(df)
df.to_csv('comics.csv', index=False)   



