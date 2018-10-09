from sqlalchemy import create_engine
from kichiuma_setup import Base,Returninfo,SeisekiData
from sqlalchemy.orm import sessionmaker
import requests,sys,re
from bs4 import BeautifulSoup
from courseutil import Courseref

ymd = sys.argv[1]

##ここからDB操作
engine = create_engine('sqlite:///kichiuma.db')
Base.metadata.bind=engine
Session = sessionmaker(bind=engine)
session = Session()

year = int(ymd[0:4])
month = int(ymd[4:6])
day = int(ymd[6:8])

url ='http://www.kichiuma-chiho.net/php/search.php'

date = str(year) + '/' + str(month) + '/' + str(day)
p = 'res'

#開催会場一覧を取得
cr = Courseref()
id_list = []
for r in cr.course_list:
    racelist_params = {'date':date,'id':r[0]}
    response = requests.get(url,params=racelist_params)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text,'lxml')
    if soup.title.string != 'エラー':
        print(soup.title.string)
        if r[0] != 3:
            id_list.append(r[0])
        kaisailist = soup.select(".kaisai_navi a")
        for s in kaisailist:
            w_id = int(str(s).split(";id=")[1].split("\">")[0])
            if w_id != 3:
                id_list.append(w_id)
        break

for w_id in id_list:
    #レース一覧を取得
    course_code = w_id
    racelist_params = {'date':date,'id':course_code}
    response = requests.get(url,params=racelist_params)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text,'lxml')
    start_race = int(soup.find("div",class_="bango").text)
    num_race = len(soup.select(".bango")) + start_race

    #レース内容を取得
    for no in range(start_race,num_race):
        p_num = no
        race_id = ymd + str(p_num).zfill(2) + str(course_code).zfill(2)
        
        #馬柱取得
        params = {'race_id':race_id,'date':date,'no':p_num,'id':course_code,'p':p}
        response = requests.get(url,params=params)
        print(response.url)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text,'lxml')
        title = soup.title.string
        print(title)
        
        ri = Returninfo(racekey = race_id)
        #単勝
        tr = soup.find_all("tr",class_="PayTan")
        w_num = 1
        for r in tr:
            win = int(r.find_all("td")[1].text)
            win_ret = int(str(r.find_all("td")[2].text[:-1]).replace(",",""))
            win_pop = int(str(r.find_all("td")[3].text)[:-3])
            setattr(ri,'win' + str(w_num) + '_num',win)
            setattr(ri,'win' + str(w_num) + '_ret',win_ret)
            setattr(ri,'win' + str(w_num) + '_pop',win_pop)
            w_num += 1

        #複勝
        tr = soup.find_all("tr",class_="PayFuku")
        w_num = 1
        for r in tr:
            place1 = re.sub(r'\D', '', r.find_all("td")[1].text)
            #place1 = int(r.find_all("td")[1].text)
            place1_ret = re.sub(r'\D', '',r.find_all("td")[2].text)
            #place1_ret = int(str(r.find_all("td")[2].text[:-1]).replace(",",""))
            place1_pop = re.sub(r'\D', '',r.find_all("td")[3].text)
            #place1_pop = int(str(r.find_all("td")[3].text)[:-2])
            setattr(ri,'place' + str(w_num) + '_num',place1)
            setattr(ri,'place' + str(w_num) + '_ret',place1_ret)
            setattr(ri,'place' + str(w_num) + '_pop',place1_pop)
            w_num += 1

        #枠連、馬連
        tr = soup.find_all("tr",class_="PayWaku")
        kenshu_flg = 'wakuren'
        w_num = 1
        for r in tr:
            kenshu = str(r.find_all("td")[0].text)
            if kenshu == '枠連複':
                kenshu_flg = 'wakuren'
                w_num = 1
            elif kenshu == '馬連複':
                kenshu_flg = 'umaren'
                w_num = 1

            ren_num1 = str(r.find_all("td")[1].text).split("-")[0]
            ren_num2 = str(r.find_all("td")[1].text).split("-")[1]
            ren_ret = int(str(r.find_all("td")[2].text[:-1]).replace(",",""))
            ren_pop = int(str(r.find_all("td")[3].text)[:-3])
            setattr(ri,kenshu_flg + str(w_num) + '_num1',ren_num1)
            setattr(ri,kenshu_flg + str(w_num) + '_num2',ren_num2)
            setattr(ri,kenshu_flg + str(w_num) + '_ret',ren_ret)
            setattr(ri,kenshu_flg + str(w_num) + '_pop',ren_pop)
            w_num += 1

        #ワイド
        tr = soup.find_all("tr",class_="PayWide")
        w_num = 1
        for r in tr:
            wide_num1 = str(r.find_all("td")[1].text).split("-")[0]
            wide_num2 = str(r.find_all("td")[1].text).split("-")[1]
            wide_ret = int(str(r.find_all("td")[2].text[:-1]).replace(",",""))
            wide_pop = int(str(r.find_all("td")[3].text)[:-2])
            setattr(ri,'wide' + str(w_num) + '_num1',wide_num1)
            setattr(ri,'wide' + str(w_num) + '_num2',wide_num2)
            setattr(ri,'wide' + str(w_num) + '_ret',wide_ret)
            setattr(ri,'wide' + str(w_num) + '_pop',wide_pop)
            w_num += 1

        #三連複
        tr = soup.find_all("tr",class_="PaySanFuku")
        w_num = 1
        for r in tr:
            sanrenpuku_num1 = str(r.find_all("td")[1].text).split("-")[0]
            sanrenpuku_num2 = str(r.find_all("td")[1].text).split("-")[1]
            sanrenpuku_num3 = str(r.find_all("td")[1].text).split("-")[2]
            sanrenpuku_ret = int(str(r.find_all("td")[2].text[:-1]).replace(",",""))
            sanrenpuku_pop = int(str(r.find_all("td")[3].text)[:-2])
            setattr(ri,'sanrenpuku' + str(w_num) + '_num1',sanrenpuku_num1)
            setattr(ri,'sanrenpuku' + str(w_num) + '_num2',sanrenpuku_num2)
            setattr(ri,'sanrenpuku' + str(w_num) + '_num3',sanrenpuku_num3)
            setattr(ri,'sanrenpuku' + str(w_num) + '_ret',sanrenpuku_ret)
            setattr(ri,'sanrenpuku' + str(w_num) + '_pop',sanrenpuku_pop)
            w_num += 1

        #三連単
        tr = soup.find_all("tr",class_="PaySanTan")
        w_num = 1
        for r in tr:
            sanrentan_num1 = str(r.find_all("td")[1].text).split("-")[0]
            sanrentan_num2 = str(r.find_all("td")[1].text).split("-")[1]
            sanrentan_num3 = str(r.find_all("td")[1].text).split("-")[2]
            sanrentan_ret = int(str(r.find_all("td")[2].text[:-1]).replace(",",""))
            sanrentan_pop = int(str(r.find_all("td")[3].text)[:-2])
            setattr(ri,'sanrentan' + str(w_num) + '_num1',sanrentan_num1)
            setattr(ri,'sanrentan' + str(w_num) + '_num2',sanrentan_num2)
            setattr(ri,'sanrentan' + str(w_num) + '_num3',sanrentan_num3)
            setattr(ri,'sanrentan' + str(w_num) + '_ret',sanrentan_ret)
            setattr(ri,'sanrentan' + str(w_num) + '_pop',sanrentan_pop)
            w_num += 1
        session.add(ri)

        #個別成績
        tr = soup.find_all("tr")
        for r in tr:
            if len(r) == 29:
                s = r.find_all("td")
                if len(s) > 0:
                    order_of_arrival = int(s[0].text)
                    waku = int(s[1].text)
                    num = int(s[2].text)
                    kinryo = float(s[6].text[0:4])
                    jockey_name = s[7].text
                    trainer_name = s[8].text
                    weight = int(s[9].text)
                    time = s[10].text
                    chakusa = s[11].text
                    agari_3f = float(s[12].text)
                    pop_order = int(s[13].text)
                    sd = SeisekiData(racehorsekey = race_id + str(num).zfill(2),
                                     order_of_arrival=order_of_arrival,
                                     waku=waku,
                                     num=num,
                                     kinryo=kinryo,
                                     jockey_name=jockey_name,
                                     trainer_name=trainer_name,
                                     weight=weight,
                                     time=time,
                                     chakusa=chakusa,
                                     agari_3f=agari_3f,
                                     pop_order=pop_order)
                    session.add(sd)
session.commit()
