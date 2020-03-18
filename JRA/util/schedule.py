import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup

YEAR = int(datetime.now().strftime("%Y"))


def annual_schedule(year=YEAR):
    alldays = []
    for month in range(1, 13):
        days = open_days(month, year)
        for day in days:
            alldays.append(day)
    return alldays


def open_days(month, year):
    base_url = "https://keiba.yahoo.co.jp/schedule/list/{}/".format(year)
    payload = {"month": str(month)}
    soup = BeautifulSoup(requests.get(base_url, payload).text, "lxml")
    return [int(f"{year:04d}{month:02d}{day:02d}") for day in _parse_to_days(soup)]


def _parse_to_days(soup):
    days = []
    for s in soup.find("table").find_all("tr"):
        if s.td is not None:
            day = re.sub("\\D", "", s.td.contents[0])
            if day != "":
                days.append(int(day))
    return list(set(days))
