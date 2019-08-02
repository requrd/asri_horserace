from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bs4 import BeautifulSoup
import requests
import sys
import re
import datetime
import time
from kichiuma_setup import (
    Base,
    BangumiData,
    HorsePillar,
    SpeedData,
    SpeedRankData,
    RecommendData,
)
from courseutil import Courseref

ymd = sys.argv[1]

# ここからDB操作
engine = create_engine("sqlite:///kichiuma.db")
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

year = int(ymd[0:4])
month = int(ymd[4:6])
day = int(ymd[6:8])

url = "http://www.kichiuma-chiho.net/php/search.php"
url_nar = "http://www2.keiba.go.jp/KeibaWeb/TodayRaceInfo/DebaTable"
url_nar_racelist = "http://www.keiba.go.jp/KeibaWeb/TodayRaceInfo/RaceList"

date = str(year) + "/" + str(month) + "/" + str(day)
date_nar = str(year).zfill(2) + "/" + str(month).zfill(2) + "/" + str(day).zfill(2)
p = "rf"

# 開催会場一覧をNAR公式から取得
cr = Courseref()
id_list = []
for r in cr.course_list:
    racelist_params = {"k_raceDate": date_nar, "k_babaCode": r[0]}
    response = requests.get(url_nar_racelist, params=racelist_params)
    if response.status_code != 200:
        response = requests.get(url, params=racelist_params)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "lxml")
    if soup.title.string != "エラー":
        print(soup.title.string)
        if r[0] != 3:
            id_list.append(r[0])

        course_list = soup.find_all("a", class_="courseBtn")
        for c in course_list:
            w_url = c.get("href")
            if w_url is not None:
                w_id = int(w_url.split("?")[-1].split("&")[1].split("=")[-1])
                id_list.append(w_id)
        break

# 開催会場ごとの処理
for w_id in id_list:
    # レース一覧をNAR公式より取得
    course_code = w_id
    racelist_params = {"k_raceDate": date_nar, "k_babaCode": course_code}
    response = requests.get(url_nar_racelist, params=racelist_params)
    if response.status_code != 200:
        response = requests.get(url_nar_racelist, params=racelist_params)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "lxml")
    racelist = soup.find("section", class_="raceTable").find_all("a")
    start_race = int(
        soup.find("section", class_="raceTable")
        .find("a")
        .get("href")
        .split("?")[-1]
        .split("&")[1]
        .split("=")[-1]
    )
    num_race = start_race
    for r in racelist:
        if r.get("href") is not None:
            w_url = r.get("href").split("?")[0]
            if w_url == "../TodayRaceInfo/DebaTable":
                num_race += 1
    # レース内容を吉馬から取得
    for no in range(start_race, num_race):
        p_num = no
        race_id = ymd + str(p_num).zfill(2) + str(course_code).zfill(2)

        # 馬柱取得
        params = {
            "race_id": race_id,
            "date": date,
            "no": p_num,
            "id": course_code,
            "p": p,
        }
        response = requests.get(url, params=params)
        print(response.url)
        if response.status_code != 200:
            response = requests.get(url, params=params)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, "lxml")
        title = soup.title.string
        print(title)

        # 地方競馬取得
        race_id_nar = (
            str(year)
            + str(month).zfill(2)
            + str(day).zfill(2)
            + str(p_num).zfill(2)
            + str(course_code)
        )
        date_nar = str(year) + "/" + str(month).zfill(2) + "/" + str(day).zfill(2)
        params_nar = {
            "k_raceDate": date_nar,
            "k_raceNo": p_num,
            "k_babaCode": course_code,
        }
        response_nar = requests.get(url_nar, params=params_nar)
        print(response_nar.url)
        if response_nar.status_code != 200:
            response_nar = requests.get(url_nar, params=params)
        response_nar.encoding = response_nar.apparent_encoding
        soup_nar = BeautifulSoup(response_nar.text, "lxml")
        title_nar = soup_nar.title.string
        print(title_nar)
        pastBody = soup_nar.find("section", class_="cardTable").find_all("tbody")

        # レース情報
        year = soup.title.string.split("　")[2].split("年")[0]
        month = soup.title.string.split("　")[2].split("年")[1].split("月")[0].zfill(2)
        day = (
            soup.title.string.split("　")[2]
            .split("年")[1]
            .split("月")[1]
            .split("日")[0]
            .zfill(2)
        )
        ymd = year + month + day
        this_info = soup.find("div", id="race_title")
        course_name = this_info.find("td", id="course").text
        race_num = int(this_info.find("td", id="number").text)
        race_name = this_info.find("span", id="title").text
        left_right = this_info.find("td", width="68%").text.split("　")[2][0]
        distance = (
            this_info.find("td", width="68%").text.split("　")[2][1:].replace("m", "")
        )
        start_time = this_info.b.text.split(" ")[1]
        prizelist = []
        for i in this_info.find("td", id="prize").childGenerator():
            if str(i).find("br") < 0 and str(i).find("賞金"):
                prizelist.append(int(str(i).replace(",", "")))

        bd = session.query(BangumiData).filter(BangumiData.racekey == race_id).first()
        if bd is None:
            bd = BangumiData()
            bd_exist_flg = 0
        else:
            bd_exist_flg = 1

        bd.racekey = race_id
        bd.ymd = ymd
        bd.course_code = course_code
        bd.course_name = course_name
        bd.race_num = race_num
        bd.race_name = race_name
        bd.left_right = left_right
        bd.distance = distance
        bd.start_time = start_time

        for i in range(len(prizelist)):
            setattr(bd, "prize" + str(i + 1), prizelist[i])

        if bd_exist_flg == 0:
            session.add(bd)

        # 地方競馬　レース情報
        allHorsePastRows1 = pastBody[0].find_all("tr", class_="tBorder")
        allHorsePastRows2to5 = pastBody[0].find_all("tr", class_="")

        i = 0
        allHorsePastRows2 = []
        allHorsePastRows3 = []
        allHorsePastRows4 = []
        allHorsePastRows5 = []

        for allHorsePastRows2to5_elm in allHorsePastRows2to5:
            if (i - 2) % (4) == 0:
                allHorsePastRows2.append(allHorsePastRows2to5_elm)
            if (i - 3) % (4) == 0:
                allHorsePastRows3.append(allHorsePastRows2to5_elm)
            if (i - 0) % (4) == 0 and i != 0:
                allHorsePastRows4.append(allHorsePastRows2to5_elm)
            if (i - 1) % (4) == 0 and i != 1:
                allHorsePastRows5.append(allHorsePastRows2to5_elm)
            i += 1

        # 馬柱情報
        tr = soup.find_all("tr")
        cnt = 0
        hpl = []
        for r in tr:
            if len(r) == 21:
                # レース情報を馬柱にセット
                num = cnt + 1
                rhkey = race_id + str(num).zfill(2)
                hp = (
                    session.query(HorsePillar)
                    .filter(HorsePillar.racehorsekey == rhkey)
                    .first()
                )
                if hp is None:
                    hp = HorsePillar()
                    hp_exist_flg = 0
                else:
                    hp_exist_flg = 1

                # 出走馬カラム
                num = cnt + 1
                waku = int(r.find("td").text)
                w_horse = r.find("td", class_="horse_box")
                horse = w_horse.a.text
                father = w_horse.find(class_="RFName").text.replace("父", "")
                mother = w_horse.find(class_="RMName").text.replace("母", "")
                motherfather = (
                    w_horse.find(class_="RMFName")
                    .text.replace("母父", "")
                    .replace("(", "")
                    .replace(")", "")
                )

                horse_features = []
                for i in w_horse.childGenerator():
                    if str(i).find("br") < 0 and str(i).find("span") < 0:
                        horse_features.append(i)

                horse_body_features = horse_features[0].split(" ")
                hair = horse_body_features[0]
                sex = horse_body_features[1][:-1]
                age = int(horse_body_features[1][-1:])
                owner = horse_features[1]
                producer = horse_features[2]

                hp.racehorsekey = race_id + str(num).zfill(2)
                hp.racekey = race_id
                hp.num = num
                hp.waku = waku
                hp.horse = horse
                hp.father = father
                hp.mother = mother
                hp.motherfather = motherfather
                hp.hair = hair
                hp.sex = sex
                hp.age = age
                hp.owner = owner
                hp.producer = producer

                # 度数
                w_dosuu = r.find("td", class_="dosuu_box")
                dosuu_list = []
                for i in w_dosuu.childGenerator():
                    if str(i).find("br") < 0:
                        dl = i.split("-")
                        dosuu_list.append(
                            [int(dl[0]), int(dl[1]), int(dl[2]), int(dl[3])]
                        )

                hp.seiseki_all_icchaku = dosuu_list[0][0]
                hp.seiseki_all_nichaku = dosuu_list[0][1]
                hp.seiseki_all_sanchaku = dosuu_list[0][2]
                hp.seiseki_all_chakugai = dosuu_list[0][3]

                hp.seiseki_dart_left_icchaku = dosuu_list[1][0]
                hp.seiseki_dart_left_nichaku = dosuu_list[1][1]
                hp.seiseki_dart_left_sanchaku = dosuu_list[1][2]
                hp.seiseki_dart_left_chakugai = dosuu_list[1][3]

                hp.seiseki_dart_right_icchaku = dosuu_list[2][0]
                hp.seiseki_dart_right_nichaku = dosuu_list[2][1]
                hp.seiseki_dart_right_sanchaku = dosuu_list[2][2]
                hp.seiseki_dart_right_chakugai = dosuu_list[2][3]

                hp.seiseki_this_course_icchaku = dosuu_list[3][0]
                hp.seiseki_this_course_nichaku = dosuu_list[3][1]
                hp.seiseki_this_course_sanchaku = dosuu_list[3][2]
                hp.seiseki_this_course_chakugai = dosuu_list[3][3]

                # 騎手カラム
                w_jockey = r.find("td", class_="kisyu_box")
                jockey_items = []

                for i in w_jockey.childGenerator():
                    if str(i).find("br") < 0:
                        jockey_items.append(str(i))
                hp.kinryo = int(float(jockey_items[0].replace("kg", "")))
                jockey = jockey_items[1].split("(")
                hp.jockey_name = jockey[0]
                hp.jockey_shozoku = jockey[1].replace(")", "")
                jockey_seiseki = jockey_items[2].split("-")
                hp.jockey_seiseki_icchaku = jockey_seiseki[0]
                hp.jockey_seiseki_nichaku = jockey_seiseki[1]
                hp.jockey_seiseki_sanchaku = jockey_seiseki[2]
                hp.jokcey_seiseki_chakugai = jockey_seiseki[3]
                trainer = jockey_items[3].split("(")
                hp.trainer_name = trainer[0]
                hp.trainer_shozoku = trainer[1].replace(")", "")

                # 成績処理
                zensoNRow1_raceInfo_data = []
                aHorsePastRows1 = allHorsePastRows1[cnt]
                aHorsePastRows2 = allHorsePastRows2[cnt]
                aHorsePastRows3 = allHorsePastRows3[cnt]
                aHorsePastRows4 = allHorsePastRows4[cnt]
                aHorsePastRows5 = allHorsePastRows5[cnt]

                horseName = aHorsePastRows1.find("a", class_="horseName").text
                hp.lineage_login_code = (
                    aHorsePastRows1.find("a", class_="horseName")
                    .get("href")
                    .split("?")[-1]
                    .split("=")[-1]
                )
                hp.rider_license_no = (
                    aHorsePastRows1.find("a", class_="jockeyName")
                    .get("href")
                    .split("?")[-1]
                    .split("=")[-1]
                )
                zenso1to5Order = aHorsePastRows1.find_all("span", class_="pastRank")
                zenso1to5Raceinfo = aHorsePastRows1.find_all("div", class_="raceInfo")
                raceName = []
                courseCodeList = []
                raceNumList = []
                ninkiBataiju = []
                timeCourner = []
                ichakusa = []

                # 各馬のそれぞれの行のhtmlに含まれるtdでfor文（l番目のtd）
                for l in range(len(aHorsePastRows2.find_all("td"))):
                    if l > 2:
                        if (
                            aHorsePastRows2.find_all("td")[l].text is not None
                            and aHorsePastRows2.find_all("td")[l].text != "\n"
                        ):
                            raceName.append(
                                re.split(
                                    "\n",
                                    aHorsePastRows2.find_all("td")[l]
                                    .text.replace("\n", "")
                                    .replace("\u3000", " "),
                                )
                            )
                        if aHorsePastRows2.find_all("td")[l].a is not None:
                            params_w = (
                                aHorsePastRows2.find_all("td")[l]
                                .a.get("href")
                                .split("?")[-1]
                                .split("&")
                            )
                            courseCodeList.append(params_w[-1].split("=")[-1])
                            raceNumList.append(params_w[-2].split("=")[-1])
                        else:
                            courseCodeList.append(0)
                            raceNumList.append(0)

                for l in range(len(aHorsePastRows3.find_all("td"))):
                    if l > 2:
                        if (
                            aHorsePastRows3.find_all("td")[l].text is not None
                            and aHorsePastRows3.find_all("td")[l].text != "\n"
                        ):
                            if (
                                len(
                                    re.split(
                                        "\u3000|\n| ",
                                        aHorsePastRows3.find_all("td")[l].text.replace(
                                            "\n", ""
                                        ),
                                    )
                                )
                                == 4
                            ):
                                ninkiBataiju.append(
                                    re.split(
                                        "\u3000|\n| ",
                                        aHorsePastRows3.find_all("td")[l].text.replace(
                                            "\n", ""
                                        ),
                                    )
                                )
                            else:
                                ninkiBataiju_elm = []
                                ninkiBataiju_elm.append(
                                    re.split(
                                        "\u3000|\n| ",
                                        aHorsePastRows3.find_all("td")[l].text.replace(
                                            "\n", ""
                                        ),
                                    )[0]
                                )
                                ninkiBataiju_elm.append(
                                    re.split(
                                        "\u3000|\n| ",
                                        aHorsePastRows3.find_all("td")[l].text.replace(
                                            "\n", ""
                                        ),
                                    )[1]
                                )
                                ninkiBataiju_elm.append(
                                    re.search(
                                        r"[一-龥]{1}\s{1}[一-龥]{1}",
                                        aHorsePastRows3.find_all("td")[l].text.replace(
                                            "\n", ""
                                        ),
                                    ).group()
                                )
                                ninkiBataiju_elm.append(
                                    re.split(
                                        "\u3000|\n| ",
                                        aHorsePastRows3.find_all("td")[l].text.replace(
                                            "\n", ""
                                        ),
                                    )[4]
                                )
                                ninkiBataiju.append(ninkiBataiju_elm)
                for l in range(len(aHorsePastRows4.find_all("td"))):
                    if l > 1:
                        if (
                            aHorsePastRows4.find_all("td")[l].text is not None
                            and aHorsePastRows4.find_all("td")[l].text != "\n"
                        ):
                            timeCourner.append(
                                re.split(
                                    "\u3000|\n",
                                    aHorsePastRows4.find_all("td")[l].text.replace(
                                        "\n", ""
                                    ),
                                )
                            )
                for l in range(len(aHorsePastRows5.find_all("td"))):
                    if l > 2:
                        if (
                            aHorsePastRows5.find_all("td")[l].text is not None
                            and aHorsePastRows5.find_all("td")[l].text != "\n"
                        ):
                            ichakusa.append(
                                re.split(
                                    "\u3000|\n",
                                    aHorsePastRows5.find_all("td")[l].text.replace(
                                        "\n", ""
                                    ),
                                )
                            )
                k = 0

                # 各馬のk走前でfor文
                zenso_no = 1
                for k in range(len(zenso1to5Order)):
                    zensoNRaceinfo = zenso1to5Raceinfo[k]
                    zensoNOrder = zenso1to5Order[k]
                    zensoNRow1_raceInfo_data = []
                    zensoNRow2_raceName_data = []

                    # レース情報取得（Row1）
                    for elm in zensoNRaceinfo.childGenerator():
                        if elm.string is not None and elm.string != "\n":
                            data = re.split("\u3000|\n", elm.string.replace("\n", ""))
                            for elm2 in data:
                                zensoNRow1_raceInfo_data.append(elm2)
                    course_name_z = zensoNRow1_raceInfo_data[4]
                    course_code_z = courseCodeList[k]
                    race_num_z = raceNumList[k]
                    ymd_z = datetime.datetime.strptime(
                        zensoNRow1_raceInfo_data[1], "%y.%m.%d"
                    ).strftime("%Y%m%d")
                    order_of_arrival = zensoNRow1_raceInfo_data[0]
                    race_name_z = raceName[k]
                    if zensoNRow1_raceInfo_data[5][:1] == "芝":
                        left_right_z = zensoNRow1_raceInfo_data[5][1:2]
                        distance_z = zensoNRow1_raceInfo_data[5][2:]
                    else:
                        left_right_z = zensoNRow1_raceInfo_data[5][:1]
                        distance_z = zensoNRow1_raceInfo_data[5][1:]
                    if timeCourner[k][0] == "":
                        time_min_z = int(0)
                        time_sec_z = float(0)
                    else:
                        time_min_z = int(timeCourner[k][0].split(":")[0])
                        time_sec_z = float(timeCourner[k][0].split(":")[1])
                    baba_z = zensoNRow1_raceInfo_data[2]
                    horse_num_z = zensoNRow1_raceInfo_data[6].replace("番", "")

                    if timeCourner[k][2] == " " or timeCourner[k][2] == "非計測":
                        agari_3f = 0
                    else:
                        agari_3f = float(timeCourner[k][2])

                    if order_of_arrival == 1:
                        chakusa = 0
                        win_horse = horseName
                    else:
                        chakusa = ichakusa[k][0]
                        win_horse = ichakusa[k][1]

                    kinryo_z = ninkiBataiju[k][3]
                    jockey_name_z = ninkiBataiju[k][2]

                    if ninkiBataiju[k][0].replace("人", "") == "":
                        pop_order = 0
                    else:
                        pop_order = int(ninkiBataiju[k][0].replace("人", ""))

                    num_of_all_horse = int(zensoNRow1_raceInfo_data[3].replace("頭", ""))

                    if ninkiBataiju[k][1] == "－" or ninkiBataiju[k][1] == "計不":
                        weight = 0
                    else:
                        weight = int(ninkiBataiju[k][1])

                    if timeCourner[k][1] == "":
                        corner1 = 0
                        corner2 = 0
                        corner3 = 0
                        corner4 = 0
                    else:
                        if len(timeCourner[k][1].split("-")) == 1:
                            corner1 = 0
                            corner2 = 0
                            corner3 = 0
                            corner4 = timeCourner[k][1].split("-")[0]
                        elif len(timeCourner[k][1].split("-")) == 2:
                            corner1 = 0
                            corner2 = 0
                            corner3 = timeCourner[k][1].split("-")[0]
                            corner4 = timeCourner[k][1].split("-")[1]
                        elif len(timeCourner[k][1].split("-")) == 3:
                            corner1 = 0
                            corner2 = timeCourner[k][1].split("-")[0]
                            corner3 = timeCourner[k][1].split("-")[1]
                            corner4 = timeCourner[k][1].split("-")[2]
                        elif len(timeCourner[k][1].split("-")) == 4:
                            corner1 = timeCourner[k][1].split("-")[0]
                            corner2 = timeCourner[k][1].split("-")[1]
                            corner3 = timeCourner[k][1].split("-")[2]
                            corner4 = timeCourner[k][1].split("-")[3]

                    setattr(hp, "zenso" + str(zenso_no) + "_course_name", course_name_z)
                    setattr(hp, "zenso" + str(zenso_no) + "_course_code", course_code_z)
                    setattr(hp, "zenso" + str(zenso_no) + "_race_num", race_num_z)
                    setattr(hp, "zenso" + str(zenso_no) + "_ymd", ymd_z)
                    setattr(
                        hp,
                        "zenso" + str(zenso_no) + "_order_of_arrival",
                        order_of_arrival,
                    )
                    setattr(hp, "zenso" + str(zenso_no) + "_race_name", race_name_z[0])
                    setattr(hp, "zenso" + str(zenso_no) + "_left_right", left_right_z)
                    setattr(hp, "zenso" + str(zenso_no) + "_distance", distance_z)
                    setattr(hp, "zenso" + str(zenso_no) + "_time_min", time_min_z)
                    setattr(hp, "zenso" + str(zenso_no) + "_time_sec", time_sec_z)
                    setattr(hp, "zenso" + str(zenso_no) + "_baba", baba_z)
                    setattr(hp, "zenso" + str(zenso_no) + "_agari_3f", agari_3f)
                    setattr(hp, "zenso" + str(zenso_no) + "_chakusa", chakusa)
                    setattr(hp, "zenso" + str(zenso_no) + "_kinryo", kinryo_z)
                    setattr(hp, "zenso" + str(zenso_no) + "_jockey_name", jockey_name_z)
                    setattr(hp, "zenso" + str(zenso_no) + "_pop_order", pop_order)
                    setattr(
                        hp,
                        "zenso" + str(zenso_no) + "_num_of_all_horse",
                        num_of_all_horse,
                    )
                    setattr(hp, "zenso" + str(zenso_no) + "_horse_num", horse_num_z)
                    setattr(hp, "zenso" + str(zenso_no) + "_weight", weight)
                    setattr(hp, "zenso" + str(zenso_no) + "_corner1", corner1)
                    setattr(hp, "zenso" + str(zenso_no) + "_corner2", corner2)
                    setattr(hp, "zenso" + str(zenso_no) + "_corner3", corner3)
                    setattr(hp, "zenso" + str(zenso_no) + "_corner4", corner4)
                    setattr(hp, "zenso" + str(zenso_no) + "_win_horse", win_horse)
                    zenso_no += 1
                if hp_exist_flg == 0:
                    session.add(hp)
                cnt += 1

        # スピード指数取得
        params = {
            "race_id": race_id,
            "date": date,
            "no": p_num,
            "id": course_code,
            "p": "sp",
        }
        sp_res = requests.get(url, params=params)
        if sp_res.status_code != 200:
            sp_res = requests.get(url, params=params)
        sp_res.encoding = sp_res.apparent_encoding
        sp_soup = BeautifulSoup(sp_res.text, "lxml")

        # スピード指数追加処理
        tr = sp_soup.find_all("tr")
        w_no = 1
        for r in tr:
            if len(r) == 29:
                rhkey = race_id + str(w_no).zfill(2)
                wsp = r.find_all("td", align="center")
                sp_mod_mark = wsp[2].text
                sp_mod = re.sub(r"\D", "", wsp[3].text)
                sp_mean_mark = wsp[4].text
                sp_mean = re.sub(r"\D", "", wsp[5].text)
                sp_max_mark = wsp[6].text
                sp_max = re.sub(r"\D", "", wsp[7].text)
                spd = (
                    session.query(SpeedData)
                    .filter(SpeedData.racehorsekey == rhkey)
                    .first()
                )
                if spd is None:
                    spd = SpeedData()
                    spd_exist_flg = 0
                else:
                    spd_exist_flg = 1

                spd.racehorsekey = rhkey
                spd.sp_mod = sp_mod
                spd.sp_mod_mark = sp_mod_mark
                spd.sp_mean = sp_mean
                spd.sp_mean_mark = sp_mean_mark
                spd.sp_max = sp_max
                spd.sp_max_mark = sp_max_mark

                # 前走以前の指数
                tb = r.find_all("table")
                zenso_no = 1
                for s in tb:
                    t = s.find_all("td")
                    speed_score = re.sub(r"\D", "", t[1].text)
                    senko_score = re.sub(r"\D", "", t[2].text)
                    agari_score = re.sub(r"\D", "", t[3].text)
                    setattr(spd, "zenso" + str(zenso_no) + "_speed_score", speed_score)
                    setattr(spd, "zenso" + str(zenso_no) + "_senko_score", senko_score)
                    setattr(spd, "zenso" + str(zenso_no) + "_agari_score", agari_score)
                    zenso_no += 1
                if spd_exist_flg == 0:
                    session.add(spd)
                w_no += 1

        # スピード指数ランク取得
        params = {
            "race_id": race_id,
            "date": date,
            "no": p_num,
            "id": course_code,
            "p": "ls",
        }
        ls_res = requests.get(url, params=params)
        if ls_res.status_code != 200:
            ls_res = requests.get(url, params=params)
        ls_res.encoding = ls_res.apparent_encoding
        ls_soup = BeautifulSoup(ls_res.text, "lxml")

        # スピード指数ランク追加処理
        tr = ls_soup.find_all("tr", height=33)
        w_no = 1
        for r in tr:
            s = r.find_all("td")
            rhkey = race_id + str(w_no).zfill(2)
            zenso_rank = s[2].text
            kakoso_rank = s[3].text
            zenso1_sp = re.sub(r"\D", "", s[5].text)
            zenso2_sp = re.sub(r"\D", "", s[6].text)
            zenso3_sp = re.sub(r"\D", "", s[7].text)
            zenso4_sp = re.sub(r"\D", "", s[8].text)
            zenso5_sp = re.sub(r"\D", "", s[9].text)

            spr = (
                session.query(SpeedRankData)
                .filter(SpeedRankData.racehorsekey == rhkey)
                .first()
            )
            if spr is None:
                spr = SpeedRankData()
                spr_exist_flg = 0
            else:
                spr_exist_flg = 1

            spr.racehorsekey = rhkey
            spr.zenso_rank = zenso_rank
            spr.kakoso_rank = kakoso_rank
            spr.zenso1_sp = zenso1_sp
            spr.zenso2_sp = zenso2_sp
            spr.zenso3_sp = zenso3_sp
            spr.zenso4_sp = zenso4_sp
            spr.zenso5_sp = zenso5_sp

            if spr_exist_flg == 0:
                session.add(spr)
            w_no += 1

        # 推奨馬取得
        params = {
            "race_id": race_id,
            "date": date,
            "no": p_num,
            "id": course_code,
            "p": "fp",
        }
        fp_res = requests.get(url, params=params)
        if fp_res.status_code != 200:
            fp_res = requests.get(url, params=params)
        fp_res.encoding = fp_res.apparent_encoding
        fp_soup = BeautifulSoup(fp_res.text, "lxml")

        # 推奨馬追加処理
        tr = fp_soup.find_all("tr")
        w_no = 1
        for r in tr:
            if len(r) == 29:
                s = r.find_all("td")
                rhkey = race_id + str(w_no).zfill(2)
                hyoka = s[2].text
                sp = re.sub(r"\D", "", s[3].text)
                senko_score = re.sub(r"\D", "", s[5].text)
                sp_credit_mark = s[6].text
                sp_credit = re.sub(r"\D", "", s[7].text)
                sp_mod_mark = s[8].text
                sp_mod = re.sub(r"\D", "", s[9].text)
                sp_max_mark = s[10].text
                sp_max = re.sub(r"\D", "", s[11].text)
                last_leg_power_mark = s[10].text
                last_leg_power = re.sub(r"\D", "", s[11].text)

                rd = (
                    session.query(RecommendData)
                    .filter(RecommendData.racehorsekey == rhkey)
                    .first()
                )
                if rd is None:
                    rd = RecommendData()
                    rd_exist_flg = 0
                else:
                    rd_exist_flg = 1

                rd.racehorsekey = rhkey
                rd.hyoka = hyoka
                rd.sp = sp
                rd.senko_score = senko_score
                rd.sp_credit_mark = sp_credit_mark
                rd.sp_credit = sp_credit
                rd.sp_mod_mark = sp_mod_mark
                rd.sp_mod = sp_mod
                rd.sp_max_mark = sp_max_mark
                rd.sp_max = sp_max
                rd.last_leg_power_mark = last_leg_power_mark
                rd.last_leg_power = last_leg_power
                if rd_exist_flg == 0:
                    session.add(rd)
                w_no += 1

session.commit()
