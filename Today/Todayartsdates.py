import pandas as pd
df = pd.read_csv("TodayArts.csv")
dates = df["Date"]
months = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}
years = df["Year"]
for num in range(len(dates)):
    na = True
    if len(dates[num].split("-")) == 2:
        if dates[num].split("-")[0] in months and dates[num].split("-")[1].isnumeric():
            dates[num] = str(months[dates[num].split("-")[0]]) + "-" + dates[num].split("-")[1] + "-" + str(years[num])
        elif dates[num].split("-")[0] in months and dates[num].split("-")[1] in months:
            dates[num] = str(months[dates[num].split("-")[1]]) + "-1-" + str(years[num])
    elif len(dates[num].split("-")) == 1:
        if dates[num].split("-")[0] in months:
            dates[num] = str(months[dates[num].split("-")[0]]) + "-1-" + str(years[num])
df["Date"] = dates
df.to_csv('TodayArts.csv', index = False)