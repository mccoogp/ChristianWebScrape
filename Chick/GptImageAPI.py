from openai import OpenAI

import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

client = OpenAI()

df = pd.read_csv('comics.csv')
links = df["links"]
titles = df["Title"]
responses = []

for response in range(len(titles)):
    responses.append(None)

start = 260
numgen = 20

for i in range(start, start+numgen):
    content = [{"type": "input_text", "text": "Turn this comic strip into a written story."}]

    for link in links[i][2:len(links[i])-1].split(","):
        content.append({
                    "type": "input_image",
                    "image_url": link.strip(" ").strip("'"),
                    })
    #texts = "Dr. Carlton and Dawson arrive at Winthorp Castle, renowned for its priceless treasures. Dawson excitedly reveals that the most famous treasure is kept in The Locked Room. Intrigued, Dr. Carlton listens attentively as Dawson explains a touching history: years ago, Lord Winthorp(\’)s grandfather saved the life of a Maharajah. In gratitude, the Maharajah(\’)s people spent 19 years creating a stunning gift for the Winthorp family. \n In the castle's Great Kitchen, a surprised maid realizes the caretaker forgot to deliver a box, instructing a new boy to take it straight to the caretaker’s room. The boy sneaks inside and finds the caretaker asleep on a soft rug, seemingly undisturbed. \n Later, Dr. Carlton and Dawson are introduced to Lord Winthorp by his butler Jenkins. Lord Winthorp is a proud man who takes great care of the treasures in his home. Dawson tells Winthorp about the Maharajah's gift—a priceless (\")Carpet of Snow,(\") a carpet woven from the hairs of white tigers and carefully maintained since its arrival, even cared for by Queen Victoria herself.\nJenkins opens the door to the locked room, and Lord Winthorp presents the (\")Carpet of Snow(\") to his guests with great fanfare. Suddenly, chaos ensues as a spilled jar of ink stains the carpet. Lord Winthorp is furious, feeling sick over the ruined carpet despite efforts to clean the stain. In his wrath, he demands the carpet be removed and burned, refusing to allow anything with a stain to remain in his castle.\n As the story unfolds, Dr. Carlton explains to Lord Winthorp that in one way, he is like God in Heaven, insisting nothing stained should stay there. The Lord wonders how that could be, as others say he is a good man. Dr. Carlton gently tells him that all people have sinned and that because of this, no soul with a stain can enter Heaven. \nLord Winthorp admits to telling lies, as many do, and Dr. Carlton sternly informs him that the Bible says such liars are destined for hell. Frightened, Winthorp questions how he can have his soul cleaned if they couldn’t even remove a stain from the carpet of snow.\nDr. Carlton explains that being baptized or doing good deeds will not remove the stain of sin on a soul, which all people inherit from Adam and Eve’s original sin. This sin separates everyone from God, meaning all deserve hell. However, God required innocent blood to be shed to atone for sin. In Old Testament times, people sacrificed animals, but those sacrifices could not remove the stain.\nThen, 2,000 years ago, God sent His Son, Jesus Christ, to shed His precious, sinless blood by living a pure life and dying on the cross to take away sin once and for all.\nDr. Carlton explains that Jesus’s blood is special because it was God’s blood, not just human blood, making it pure and sinless. The greatest day in history was when Jesus shed His blood so sins could be washed away, offering eternal life to all who believe.\nFinally, Dr. Carlton invites Lord Winthorp to have his sin stain removed by trusting in Jesus. Winthorp eagerly agrees, praying to repent of his sins and accept Jesus’s sacrifice. Moments later, Winthorp feels his soul cleansed, free from the stain of sin.\nThe story ends with a message to readers: the stain of sin can be removed from anyone’s soul today—there is only one way, by believing that Jesus Christ shed His precious blood and died on the cross, putting trust in Him alone for salvation. This brings eternal life and peace."
    print("\n" + str(i))
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[{
            "role": "user",
            "content": content,
        }],
        max_output_tokens=10000

    )
    #print(response.output_text)
    texts = response.output_text
    print(texts)
    file_content = texts

    with open(f"{titles[i]}.txt", "w") as file:
        file.write(file_content)
    responses[i] = texts



for n in range(len(responses)):
    if responses[n] == None:
        responses[n] = df["Responses"][n]
df["Responses"] = responses


df.to_csv('comics.csv', index=False)  
