import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup

YEAR = int(datetime.now().strftime("%Y"))

def annual_schedule(year=YEAR):
    days = []
    for month in range(1,13):
        for day in open_days(month, year):
            days.append(int("{:04d}{:02d}{:02d}".format(year, month, day)))
    return days


def open_days(month, year):
    base_url = "https://keiba.yahoo.co.jp/schedule/list/{}/".format(
        year)
    payload = {"month": str(month)}
    response = requests.get(base_url, payload)
    soup = BeautifulSoup(response.text, 'lxml')
    return _parse_to_days(soup)


def _parse_to_days(soup):
    days = []
    for s in soup.find("table").find_all("tr"):
        if s.td is not None:
            day = re.sub("\\D", "", s.td.contents[0])
            if day != "":
                days.append(int(day))
    return list(set(days))
