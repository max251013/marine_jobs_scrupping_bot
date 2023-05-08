import requests
from bs4 import BeautifulSoup
from datetime import datetime
import dateparser
import time
#from time import sleep

import json





def get_maritime_zone_offshore():
    url = "https://maritime-zone.com/en/vacancy-fleet_type-offshore_fleet"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("div", class_="item")
    offshore_fleet = 'Offshore Fleet'

    vacancy_dict = {}

    for article in data:
        vacancy_article = article.find("a", class_="card-title").text
        vacancy_info = article.find("div", class_="col-md-9").text.replace("\n\n", "\n").strip()
        vacancy_url = "https://maritime-zone.com" + article.find("a").get("href")
        vacancy_id = vacancy_url.split('/')[-1]

        vacancy_date_time = article.find_all("span")[-2].text

        vacancy_dict[vacancy_id] = {
            "offshore_fleet": offshore_fleet,
            "vacancy_date_time": vacancy_date_time,
            "vacancy_article": vacancy_article,
            "vacancy_url": vacancy_url,
            "vacancy_info": vacancy_info
        }
    with open("vacancy_dict.json", "a") as file:
        json.dump(vacancy_dict, file, indent=4, ensure_ascii=False)



def get_maritime_zone_merchant():
    url = "https://maritime-zone.com/en/vacancy-fleet_type-merchant_fleet"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("div", class_="item")
    merchant_fleet = 'Merchant Fleet'

    vacancy_dict = {}

    for article in data:
        vacancy_article = article.find("a", class_="card-title").text
        vacancy_info = article.find("div", class_="col-md-9").text.replace("\n\n", "\n").strip()
        vacancy_url = "https://maritime-zone.com" + article.find("a").get("href")
        vacancy_id = vacancy_url.split('/')[-1]

        vacancy_date_time = article.find_all("span")[-2].text

        vacancy_dict[vacancy_id] = {
            "merchant_fleet": merchant_fleet,
            "vacancy_date_time": vacancy_date_time,
            "vacancy_article": vacancy_article,
            "vacancy_url": vacancy_url,
            "vacancy_info": vacancy_info
        }
    with open("vacancy_dict.json", "a") as file:
        json.dump(vacancy_dict, file, indent=4, ensure_ascii=False)


def check_vacancy_update_offshore():


    with open('vacancy_dict.json', "r") as file:

        corrected_dict = file.read()

        corrected_dict = corrected_dict.replace('\n', '')

        corrected_dict = corrected_dict.replace('}{', ',')

        vacancy_dict_offshore = json.loads(corrected_dict)



    url = "https://maritime-zone.com/en/vacancy-fleet_type-offshore_fleet"


    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find_all("div", class_="item")



    fresh_vacancy_offshore = {}

    for article in data:
        vacancy_url = "https://maritime-zone.com" + article.find("a").get("href")
        vacancy_id = vacancy_url.split('/')[-1]

        if vacancy_id in vacancy_dict_offshore:
            continue
        else:
            offshore_fleet = 'Offshore Fleet'
            vacancy_article = article.find("a", class_="card-title").text
            vacancy_info = article.find("div", class_="col-md-9").text.replace("\n\n", "\n").strip()
            vacancy_date_time = article.find_all("span")[-2].text


            vacancy_dict_offshore[vacancy_id] = {
                "offshore_fleet": offshore_fleet,
                "vacancy_date_time": vacancy_date_time,
                "vacancy_article": vacancy_article,
                "vacancy_info": vacancy_info,
                "vacancy_url": vacancy_url
                }

            fresh_vacancy_offshore[vacancy_id] = {
                "offshore_fleet": offshore_fleet,
                "vacancy_date_time": vacancy_date_time,
                "vacancy_article": vacancy_article,
                "vacancy_info": vacancy_info,
                "vacancy_url": vacancy_url
                }

    with open("vacancy_dict.json", "a") as file:
        json.dump(vacancy_dict_offshore, file, indent=4, ensure_ascii=False)

    return fresh_vacancy_offshore


def check_vacancy_update_merchant():

    with open('vacancy_dict.json', "r") as file:

        corrected_dict = file.read()

        corrected_dict = corrected_dict.replace('\n', '')

        corrected_dict = corrected_dict.replace('}{', ',')

        vacancy_dict_merchant= json.loads(corrected_dict)



    url = "https://maritime-zone.com/en/vacancy-fleet_type-merchant_fleet"


    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find_all("div", class_="item")


    fresh_vacancy_merchant = {}

    for article in data:
        vacancy_url = "https://maritime-zone.com" + article.find("a").get("href")
        vacancy_id = vacancy_url.split('/')[-1]


        if vacancy_id in vacancy_dict_merchant:
            continue
        else:
            merchant_fleet = 'Merchant Fleet'
            vacancy_article = article.find("a", class_="card-title").text
            vacancy_info = article.find("div", class_="col-md-9").text.replace("\n\n", "\n").strip()
            vacancy_date_time = article.find_all("span")[-2].text

            vacancy_dict_merchant[vacancy_id] = {
                "merchant_fleet": merchant_fleet,
                "vacancy_date_time": vacancy_date_time,
                "vacancy_article": vacancy_article,
                "vacancy_info": vacancy_info,
                "vacancy_url": vacancy_url
                }

            fresh_vacancy_merchant[vacancy_id] = {
                "merchant_fleet": merchant_fleet,
                "vacancy_date_time": vacancy_date_time,
                "vacancy_article": vacancy_article,
                "vacancy_info": vacancy_info,
                "vacancy_url": vacancy_url
                }

    with open("vacancy_dict.json", "a") as file:
        json.dump(vacancy_dict_merchant, file, indent=4, ensure_ascii=False)

    return fresh_vacancy_merchant
#check_vacancy_update_merchant()
#check_vacancy_update_offshore()
#get_maritime_zone_merchant()
#get_maritime_zone_offshore()