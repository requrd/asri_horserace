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
nar_url ='http://www2.keiba.go.jp/KeibaWeb/TodayRaceInfo/RaceMarkTable'

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
        
        #NARから馬柱取得
        params = {'k_raceDate':date,'k_raceNo':p_num,'k_babaCode':course_code}
        response = requests.get(nar_url,params=params)
        print(response.url)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text,'lxml')
        title = soup.title.string
        print(title)
        
        ri = Returninfo(racekey = race_id)
        return_infos = soup.find_all("td",class_="dbtbl")[1].find("tr",class_="dbdata")
        td = return_infos.find_all("td")

        tickets = soup.find_all("td",class_="dbtbl")[1].find_all('td',colspan='3')
        sell_tickets = []
        for r in tickets:
            sell_tickets.append(r.text)

        ##単勝
        i = sell_tickets.index('単勝') + 1
        w = 1
        for s in td[i].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'win' + str(w) + '_num',int(s))
                w += 1
            
        w = 1
        for s in td[i+1].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'win' + str(w) + '_ret',int(re.sub(r'\D', '',s)))
                w += 1
            
        w = 1
        for s in td[i+2].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'win' + str(w) + '_pop',int(s))
                w += 1

        ##複勝
        i = sell_tickets.index('複勝')*3 + 1
        w = 1
        for s in td[i].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'place' + str(w) + '_num',int(s))
                w += 1
            
        w = 1
        for s in td[i+1].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'place' + str(w) + '_ret',int(re.sub(r'\D', '',s)))
                w += 1
            
        w = 1
        for s in td[i+2].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'place' + str(w) + '_pop',int(s))
                w += 1

        ##枠連
        if len(tickets) == 9:
            i = sell_tickets.index('枠連複')*3 + 1
            w = 1
            for s in td[i].childGenerator():
                if str(s).find('br') < 0:
                    num1 = str(s).split('-')[0]
                    num2 = str(s).split('-')[1]
                    setattr(ri,'wakuren' + str(w) + '_num1',num1)
                    setattr(ri,'wakuren' + str(w) + '_num2',num2)
                    w += 1
            
            w = 1
            for s in td[i+1].childGenerator():
                if str(s).find('br') < 0:
                    setattr(ri,'wakuren' + str(w) + '_ret',int(re.sub(r'\D', '',s)))
                    w += 1
                
            w = 1
            for s in td[i+2].childGenerator():
                if str(s).find('br') < 0:
                    setattr(ri,'wakuren' + str(w) + '_pop',int(s))
                    w += 1

        ##馬連
        i = sell_tickets.index('馬連複')*3 + 1
        w = 1
        for s in td[i].childGenerator():
            if str(s).find('br') < 0:
                num1 = str(s).split('-')[0]
                num2 = str(s).split('-')[1]
                setattr(ri,'umaren' + str(w) + '_num1',num1)
                setattr(ri,'umaren' + str(w) + '_num2',num2)
                w += 1
            
        w = 1
        for s in td[i+1].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'umaren' + str(w) + '_ret',int(re.sub(r'\D', '',s)))
                w += 1
            
        w = 1
        for s in td[i+2].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'umaren' + str(w) + '_pop',int(s))
                w += 1

        ##枠単
        if len(tickets) == 9:
            i = sell_tickets.index('枠連単')*3 + 1
            w = 1
            for s in td[i].childGenerator():
                if str(s).find('br') < 0:
                    num1 = str(s).split('-')[0]
                    num2 = str(s).split('-')[1]
                    setattr(ri,'wakutan' + str(w) + '_num1',num1)
                    setattr(ri,'wakutan' + str(w) + '_num2',num2)
                    w += 1
                
            w = 1
            for s in td[i+1].childGenerator():
                if str(s).find('br') < 0:
                    setattr(ri,'wakutan' + str(w) + '_ret',int(re.sub(r'\D', '',s)))
                    w += 1
                
            w = 1
            for s in td[i+2].childGenerator():
                if str(s).find('br') < 0:
                    setattr(ri,'wakutan' + str(w) + '_pop',int(s))
                    w += 1

        ##馬単
        i = sell_tickets.index('馬連単')*3 + 1
        w = 1
        for s in td[i].childGenerator():
            if str(s).find('br') < 0:
                num1 = str(s).split('-')[0]
                num2 = str(s).split('-')[1]
                setattr(ri,'umatan' + str(w) + '_num1',num1)
                setattr(ri,'umatan' + str(w) + '_num2',num2)
                w += 1
            
        w = 1
        for s in td[i+1].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'umatan' + str(w) + '_ret',int(re.sub(r'\D', '',s)))
                w += 1
            
        w = 1
        for s in td[i+2].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'umatan' + str(w) + '_pop',int(s))
                w += 1

        ##ワイド
        i = sell_tickets.index('ワイド')*3 + 1
        w = 1
        for s in td[i].childGenerator():
            if str(s).find('br') < 0:
                num1 = str(s).split('-')[0]
                num2 = str(s).split('-')[1]
                setattr(ri,'wide' + str(w) + '_num1',num1)
                setattr(ri,'wide' + str(w) + '_num2',num2)
                w += 1
            
        w = 1
        for s in td[i+1].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'wide' + str(w) + '_ret',int(re.sub(r'\D', '',s)))
                w += 1
            
        w = 1
        for s in td[i+2].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'wide' + str(w) + '_pop',int(s))
                w += 1

        ##三連複
        i = sell_tickets.index('三連複')*3 + 1
        w = 1
        for s in td[i].childGenerator():
            if str(s).find('br') < 0:
                num1 = str(s).split('-')[0]
                num2 = str(s).split('-')[1]
                num3 = str(s).split('-')[2]
                setattr(ri,'sanrenpuku' + str(w) + '_num1',num1)
                setattr(ri,'sanrenpuku' + str(w) + '_num2',num2)
                setattr(ri,'sanrenpuku' + str(w) + '_num3',num3)
                w += 1
            
        w = 1
        for s in td[i+1].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'sanrenpuku' + str(w) + '_ret',int(re.sub(r'\D', '',s)))
                w += 1
            
        w = 1
        for s in td[i+2].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'sanrenpuku' + str(w) + '_pop',int(s))
                w += 1

        ##三連単
        i = sell_tickets.index('三連単')*3 + 1
        w = 1
        for s in td[i].childGenerator():
            if str(s).find('br') < 0:
                num1 = str(s).split('-')[0]
                num2 = str(s).split('-')[1]
                num3 = str(s).split('-')[2]
                setattr(ri,'sanrentan' + str(w) + '_num1',num1)
                setattr(ri,'sanrentan' + str(w) + '_num2',num2)
                setattr(ri,'sanrentan' + str(w) + '_num3',num3)
                w += 1
            
        w = 1
        for s in td[i+1].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'sanrentan' + str(w) + '_ret',int(re.sub(r'\D', '',s)))
                w += 1
            
        w = 1
        for s in td[i+2].childGenerator():
            if str(s).find('br') < 0:
                setattr(ri,'sanrentan' + str(w) + '_pop',int(s))
                w += 1
        session.add(ri)

        #個別成績
        pattern=r'([+-]?[0-9]+\.?[0-9]*)'
        horse_results_list = soup.find("td",class_="dbtbl").find_all('tr',align='center')
        for r in horse_results_list:
            horse_results = r.find_all('td')
            order_of_arrival = re.sub(r'\D', '',horse_results[0].text)
            waku = re.sub(r'\D', '',horse_results[1].text)
            num = re.sub(r'\D', '',horse_results[2].text)
            lineage_login_code = horse_results[3].a.get('href').split('=')[1]
            #shozoku = horse_results[4].text
            #sex_age = horse_results[5].text
            kinryo = float(horse_results[6].text)
            jockey_license_no = horse_results[7].a.get('href').split('=')[1]
            jockey_name = horse_results[7].a.text.split('(')[0]
            trainer_license_no = horse_results[8].a.get('href').split('=')[1]
            trainer_name = horse_results[8].a.text
            weight = re.sub(r'\D', '',horse_results[9].text)
            weight_increase = re.sub(r'\D', '',horse_results[10].text)
            if (horse_results[11].text).find(':') > 0:
                time_m = int(horse_results[11].text.split(':')[0])
                time_s = int(horse_results[11].text.split(':')[1]) + (int(horse_results[11].text.split(':')[2]) / 10 )
                chakusa = horse_results[12].text
                agari_3f = re.findall(pattern,horse_results[13].text)[0]
            pop_order = re.sub(r'\D', '',horse_results[14].text)
            sd = SeisekiData(racehorsekey = race_id + str(num).zfill(2),
                             order_of_arrival=order_of_arrival,
                             waku=waku,
                             num=num,
                             lineage_login_code=lineage_login_code,
                             kinryo=kinryo,
                             jockey_license_no=jockey_license_no,
                             jockey_name=jockey_name,
                             trainer_license_no=trainer_license_no,
                             trainer_name=trainer_name,
                             weight=weight,
                             weight_increase=weight_increase,
                             time_m=time_m,
                             time_s=time_s,
                             chakusa=chakusa,
                             agari_3f=agari_3f,
                             pop_order=pop_order)
            session.add(sd)
session.commit()
