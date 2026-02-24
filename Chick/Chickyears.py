
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from pathlib import Path
import string

directory_path = Path('all-chick-tracts')
df = pd.read_csv('comics.csv')

issues = {}

for file_path in directory_path.rglob('*'):
    if file_path.is_file():
        name = file_path.name
        if name != ".DS_Store":
            #print(name)
            author = ""
            n = 0
            while name[n] != "-":
                n += 1
            n+=2
            while name[n] != "'":
                author += name[n]
                n+=1
            #print(author)
            n += 3
            title = ""
            while name[n] != "(":
                title += name[n]
                n+=1
            title = title[:len(title)-1]

            n += 1
            year = name[n:n+4]
            if year == "AND ":
                year = "1978"
            issues[title.upper().rstrip(string.punctuation)] = [author, year, 0]
#print(issues)
authors = []
years = []
titles = df["Title"]

hardcodedmatches = {"KITTY KITTY! HERE" : "HERE KITTY, KITTY", 
                    "THE GREAT ESCAPE": "ESCAPE OR THE GREAT ESCAPE",
                    "THE SACRIFICE" : "THE STORY OF ABRAHAM AND ISAAC - THE SACRIFICE", 
                    "GREATEST STORY EVER TOLD" : 'THE GREATEST STORY EVER TOLD', 
                    "LIES AND MS. HENN APES" : "APES, LIES AND MS. HENN",
                    "FAIRY TALES" : "FAIRY TAILS",
                    "FOUR ANGELS" : "FOUR BROTHERS OR FOUR ANGELS",
                    "FRAME UP" : "FRAME-UP",
                    "KILLER STORM" : "THE STORY OF NOAH - KILLER STORM",
                    "LOVE THE JEWISH PEOPLE" : "SUPPORT YOUR LOCAL JEW OR JEOPARDY OR LOVE THE JEWISH PEOPLE",
                    "SECRET OF PRAYER" : "THE SECRET OF PRAYER",
                    "THAT'S BAPHOMET" : "THE CURSE OF BAPHOMET OR THAT'S BAPHOMET",
                    "UNINVITED" : "UNIVITED"}
for title in titles:
    title = title.upper()
    if "," in title:
        title = title[title.find(",")+2:] + " " + title[:title.find(",")]
        #print(title)
    title = title.rstrip(string.punctuation)
    if title in hardcodedmatches:
        title = hardcodedmatches[title]
    if title in issues:
        authors.append(issues[title][0])
        years.append(issues[title][1])
        issues[title][2] = 1
        #print(title)
    else:
        authors.append("")
        years.append("")
        print(title)
#print(authors)
#print(years)
print("---break---")
for title in issues.keys():
    if issues[title][2] == 0:
        print(title)


df["Author"] = authors
df["Year"] = years
df.to_csv('comics.csv', index=False)  