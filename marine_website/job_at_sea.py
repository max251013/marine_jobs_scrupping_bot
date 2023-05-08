import requests
from bs4 import BeautifulSoup
from time import sleep
import json

headers: dict[str, str] = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
                           }

def get_offshore_jobatsea():
    fleet = ['Offshore', 'Oil_Gas_Jobs', 'Drilling', 'oc', 'srd', 'owf']
    for i in fleet:
        url = f"http://jobatsea.online/jobs/{i}/"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.find_all("div", class_="row")
        offshore_fleet = 'Offshore Fleet'
        vacancy_dict = {}

        for article in data:
            vacancy_article = article.find("span", class_="row-info").text.strip()
            vacancy_url = article.find("a").get("href")
            vacancy_info = article.find("span", class_="time-posted").text.strip()
            vacancy_id = vacancy_url.split('/')[-3]
            vacancy_dict[vacancy_id] = {
                "offshore_fleet": offshore_fleet,
                "vacancy_article": vacancy_article,
                "vacancy_url": vacancy_url,
                "vacancy_info": vacancy_info
                }

        with open("vacancy_dict.json", "a") as file:
            json.dump(vacancy_dict, file, indent=4, ensure_ascii=False)



def get_merchant_jobatsea():

    fleet = ['Engine_Officers', 'Deck_Officers', 'Engine_Ratings', 'Deck_Ratings',
             'Catering_Staff', 'Cadets', 'Full_crew', 'Tanker_fleet', 'passenger']
    for i in fleet:
        fleet_name = i
        url = f"http://jobatsea.online/jobs/{fleet_name}/"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.find_all("div", class_="row")
        merchant_fleet = 'Merchant Fleet'

        vacancy_dict = {}
        for article in data:

            vacancy_article = article.find("span", class_="row-info").text.strip()
            vacancy_url = article.find("a").get("href")
            vacancy_info = article.find("span", class_="time-posted").text.strip()
            vacancy_id = vacancy_url.split('/')[-3]


            vacancy_dict[vacancy_id] = {
            "merchant_fleet" : merchant_fleet,
            "vacancy_article": vacancy_article,
            "vacancy_url": vacancy_url,
            "vacancy_info": vacancy_info
            }

        with open("vacancy_dict.json", "a") as file:
            json.dump(vacancy_dict, file, indent=2, ensure_ascii=False)

def check_vacancy_update_offshore_jobatsea():

    with open('vacancy_dict.json', "r") as file:

        corrected_dict = file.read()

        corrected_dict = corrected_dict.replace('\n', '')

        corrected_dict = corrected_dict.replace('}{', ',')

        vacancy_dict_offshore_jobatsea = json.loads(corrected_dict)

    fleet = ['Offshore', 'Oil_Gas_Jobs', 'Drilling', 'oc', 'srd', 'owf']

    fresh_vacancy_offshore_jobatsea = {}

    for i in fleet:

        url = f"http://jobatsea.online/jobs/{i}/"


        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        data = soup.find_all("div", class_="row")

        offshore_fleet = 'Offshore Fleet'

        for article in data:
            vacancy_url = article.find("a").get("href")
            vacancy_id = vacancy_url.split('/')[-3]

            if vacancy_id in vacancy_dict_offshore_jobatsea:
                continue
            else:
                vacancy_article = article.find("span", class_="row-info").text.strip()

                vacancy_info = article.find("span", class_="time-posted").text.strip()



                vacancy_dict_offshore_jobatsea[vacancy_id] = {
                    "offshore_fleet": offshore_fleet,
                    "vacancy_article": vacancy_article,
                    "vacancy_url": vacancy_url,
                    "vacancy_info": vacancy_info
                    }

                fresh_vacancy_offshore_jobatsea[vacancy_id] = {
                    "offshore_fleet": offshore_fleet,
                    "vacancy_article": vacancy_article,
                    "vacancy_url": vacancy_url,
                    "vacancy_info": vacancy_info
                    }

        with open("vacancy_dict.json", "w") as file:
            json.dump(vacancy_dict_offshore_jobatsea, file, indent=4, ensure_ascii=False)

    return fresh_vacancy_offshore_jobatsea

def check_vacancy_update_merchant_jobatsea():

    with open('vacancy_dict.json', "r") as file:

        corrected_dict = file.read()

        corrected_dict = corrected_dict.replace('\n', '')

        corrected_dict = corrected_dict.replace('}{', ',')

        vacancy_dict_merchant_jobatsea = json.loads(corrected_dict)

    fleet = ['Engine_Officers', 'Deck_Officers', 'Engine_Ratings', 'Deck_Ratings',
             'Catering_Staff', 'Cadets', 'Full_crew', 'Tanker_fleet', 'passenger']

    fresh_vacancy_merchant_jobatsea = {}

    for i in fleet:

        url = f"http://jobatsea.online/jobs/{i}/"
        print(url)

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        data = soup.find_all("div", class_="row")

        merchant_fleet = 'Merchant Fleet'



        for article in data:
            vacancy_url = article.find("a").get("href")
            vacancy_id = vacancy_url.split('/')[-3]

            if vacancy_id in vacancy_dict_merchant_jobatsea:
                continue
            else:
                vacancy_article = article.find("span", class_="row-info").text.strip()

                vacancy_info = article.find("span", class_="time-posted").text.strip()


                vacancy_dict_merchant_jobatsea[vacancy_id] = {
                    "merchant_fleet": merchant_fleet,
                    "vacancy_article": vacancy_article,
                    "vacancy_url": vacancy_url,
                    "vacancy_info": vacancy_info
                    }

                fresh_vacancy_merchant_jobatsea[vacancy_id] = {
                    "merchant_fleet": merchant_fleet,
                    "vacancy_article": vacancy_article,
                    "vacancy_url": vacancy_url,
                    "vacancy_info": vacancy_info
                    }



        with open("vacancy_dict.json", "a") as file:
            json.dump(vacancy_dict_merchant_jobatsea, file, indent=4, ensure_ascii=False)

    return fresh_vacancy_merchant_jobatsea


#check_vacancy_update_merchant_jobatsea()
#check_vacancy_update_offshore_jobatsea()
#get_merchant_jobatsea()
#get_offshore_jobatsea()