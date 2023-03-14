import requests
from bs4 import BeautifulSoup
from time import sleep


for count2 in range(1, 20):

    sleep (3)

    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}

    url2 = f"http://jobatsea.online/jobs?p={count2}"

    response2 = requests.get(url2, headers=headers)

    soup2 = BeautifulSoup(response2.text, "html.parser")

    data2 = soup2.find_all("div", class_="row")

    for j in data2:
        vacancy2 = j.find("span", class_="row-info").text
        url2_ref = j.find("a").get("href")
        info2 = j.find("span", class_="time-posted").text

        print(vacancy2+"\n"+info2+"\n"+url2)
