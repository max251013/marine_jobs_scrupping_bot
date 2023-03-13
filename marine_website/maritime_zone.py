import requests
from bs4 import BeautifulSoup
from time import sleep

for count1 in range(1, 20):

    sleep (3)

    url1 = f"https://maritime-zone.com/en/vacancy?page={count1}"

    response1 = requests.get(url1)

    soup1 = BeautifulSoup(response1.text, "html.parser")

    data1 = soup1.find_all("div", class_="item")
    for i in data1:
        vacancy1 = i.find("a", class_="card-title").text
        url1 = "https://maritime-zone.com" + i.find("a").get("href")
        info1 = i.find("div", class_="col-md-9").text.replace("\n\n", " ")


        print(vacancy1 + info1 + url1 + "\n")