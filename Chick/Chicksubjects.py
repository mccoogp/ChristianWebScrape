import pandas as pd
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()


def find_tag(spot, html_content):
    while html_content[spot] != ">":
        spot +=1
    spot += 2
    tag = ""
    while html_content[spot] != "<":
        if html_content[spot] == "\xa0":
            tag += " "
        elif html_content[spot] == "&":
            tag += " "
            spot += 5
        elif html_content[spot] != ",":
            tag += html_content[spot]
        spot +=1
    return spot, tag[:len(tag)-1]

df = pd.DataFrame(columns=['Title', 'Stock Number', "Subject", "Tag(s)"])

for page in range(23):
    url = f'https://www.chick.com/products/category?type=tracts#&&Language=English&Status=All&SortBy=A-Z&PageNumber={page+1}&Category=All&ShowCount=12'


    driver.get(url)

    time.sleep(3)
    print("Loading Now")

    html_content = driver.page_source

    n = 0
    for num in range(12):
        n+=1
        texttofind = "title-price"
        while html_content[n:n+len(texttofind)] != texttofind:
            n+=1

        texttofind = "stk="
        while html_content[n:n+len(texttofind)] != texttofind:
            n+=1
        spot = n+len(texttofind)
        stk = ""
        while html_content[spot] != "&":
            stk += html_content[spot]
            spot +=1
        while html_content[spot] != ">":
            spot +=1
        spot += 1
        title = ""
        while html_content[spot] != "<":
            title += html_content[spot]
            spot +=1


        texttofind = "Subject:"
        while html_content[n:n+len(texttofind)] != texttofind:
            n+=1
        spot = n
        while html_content[spot] != ">":
            spot +=1
        spot += 1
        sub = ""
        while html_content[spot] != "<":
            if html_content[spot] == "&":
                sub += " "
                spot+=5
            else:
                sub += html_content[spot]
            spot +=1

        texttofind = "Tag(s):"
        while html_content[n:n+len(texttofind)] != texttofind:
            n+=1
        spot = n+15

        tags = []
        while html_content[spot: spot+2] == "<a":
            spot, tag = find_tag(spot, html_content)
            spot += 4
            tags.append(tag)
        print(title,stk,sub,tags)
        df2 = pd.DataFrame({'Title':[title], 'Stock Number':[stk], "Subject":[sub], "Tag(s)":[tags]})
        df = pd.concat([df,df2], ignore_index=True)

page = 23
url = f'https://www.chick.com/products/category?type=tracts#&&Language=English&Status=All&SortBy=A-Z&PageNumber={page+1}&Category=All&ShowCount=12'


driver.get(url)


time.sleep(3)

html_content = driver.page_source

n = 0
for num in range(4):
    n+=1
    texttofind = "title-price"
    while html_content[n:n+len(texttofind)] != texttofind:
        n+=1

    texttofind = "stk="
    while html_content[n:n+len(texttofind)] != texttofind:
        n+=1
    spot = n+len(texttofind)
    stk = ""
    while html_content[spot] != "&":
        stk += html_content[spot]
        spot +=1
    while html_content[spot] != ">":
        spot +=1
    spot += 1
    title = ""
    while html_content[spot] != "<":
        title += html_content[spot]
        spot +=1


    texttofind = "Subject:"
    while html_content[n:n+len(texttofind)] != texttofind:
        n+=1
    spot = n
    while html_content[spot] != ">":
        spot +=1
    spot += 1
    sub = ""
    while html_content[spot] != "<":
        if html_content[spot] == "&":
            sub += " "
            spot+=5
        else:
            sub += html_content[spot]
        spot +=1

    texttofind = "Tag(s):"
    while html_content[n:n+len(texttofind)] != texttofind:
        n+=1
    spot = n+15

    tags = []
    while html_content[spot: spot+2] == "<a":
        spot, tag = find_tag(spot, html_content)
        spot += 4
        tags.append(tag)
    print(title,stk,sub,tags)
    df2 = pd.DataFrame({'Title':[title], 'Stock Number':[stk], "Subject":[sub], "Tag(s)":[tags]})
    df = pd.concat([df,df2], ignore_index=True)
print(df)
df.to_csv('comics.csv', index=False)