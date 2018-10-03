from sqlalchemy import create_engine
from kichiuma_setup import Base,BangumiData,HorsePillar
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
p = 'rf'

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
    num_race = len(soup.select(".bango"))

    #レース内容を取得
    for no in range(num_race):
        p_num = no + 1
        race_id = ymd + str(p_num).zfill(2) + str(course_code).zfill(2)
        params = {'race_id':race_id,'date':date,'no':p_num,'id':course_code,'p':p}
        response = requests.get(url,params=params)
        print(response.url)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text,'lxml')
        title = soup.title.string
        print(title)

        #レース情報
        year = soup.title.string.split("　")[2].split("年")[0]
        month = soup.title.string.split("　")[2].split("年")[1].split("月")[0].zfill(2)
        day = soup.title.string.split("　")[2].split("年")[1].split("月")[1].split("日")[0].zfill(2)
        ymd = year + month + day
        this_info = soup.find("div",id="race_title")
        course_name = this_info.find("td",id='course').text
        race_num = int(this_info.find("td",id='number').text)
        race_name = this_info.find("span",id="title").text
        left_right = this_info.find("td",width="68%").text.split("　")[2][0]
        distance = this_info.find("td",width="68%").text.split("　")[2][1:].replace('m','')
        start_time = this_info.b.text.split(' ')[1]
        prizelist = []
        for i in this_info.find("td",id="prize").childGenerator():
            if str(i).find("br") < 0 and str(i).find("賞金"):
                prizelist.append(int(str(i).replace(',','')))

        prize1 = prizelist[0]
        prize2 = prizelist[1]
        prize3 = prizelist[2]
        prize4 = prizelist[3]
        prize5 = prizelist[4]

        bd = BangumiData(racekey = race_id,
                         ymd = ymd,
                         course_code = course_code,
                         course_name = course_name,
                         race_num = race_num,
                         race_name = race_name,
                         left_right = left_right,
                         distance = distance,
                         start_time = start_time,
                         prize1 = prize1,
                         prize2 = prize2,
                         prize3 = prize3,
                         prize4 = prize4,
                         prize5 = prize5,
                        )
        session.add(bd)

        tr = soup.find_all("tr")
        cnt = 0
        hpl = []
        for r in tr:
            if len(r) == 21:
                #レース情報を馬柱にセット
                hp = HorsePillar()
                
                #出走馬カラム
                num = cnt + 1
                waku = int(r.find('td').text)
                w_horse = r.find('td',class_='horse_box')
                horse = w_horse.a.text
                father = w_horse.find(class_="RFName").text.replace('父','')
                mother = w_horse.find(class_="RMName").text.replace('母','')
                motherfather = w_horse.find(class_="RMFName").text.replace('母父','').replace('(','').replace(')','')

                horse_features = []
                for i in w_horse.childGenerator():
                    if str(i).find('br') < 0 and str(i).find('span') < 0:
                        horse_features.append(i)

                horse_body_features = horse_features[0].split(' ')
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
                
                #度数
                w_dosuu = r.find('td',class_='dosuu_box')
                dosuu_list = []
                for i in w_dosuu.childGenerator():
                    if str(i).find('br') < 0:
                        dl = i.split('-')
                        dosuu_list.append([int(dl[0]),int(dl[1]),int(dl[2]),int(dl[3])])

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
                
                #騎手カラム
                w_jockey = r.find('td',class_='kisyu_box')
                jockey_items = []

                for i in w_jockey.childGenerator():
                    if str(i).find("br") < 0:
                        jockey_items.append(str(i))
                hp.kinryo = int(float(jockey_items[0].replace('kg','')))
                jockey = jockey_items[1].split("(")
                hp.jockey_name = jockey[0]
                hp.jockey_shozoku = jockey[1].replace(')','')
                jockey_seiseki = jockey_items[2].split('-')
                hp.jockey_seiseki_icchaku = jockey_seiseki[0]
                hp.jockey_seiseki_nichaku = jockey_seiseki[1]
                hp.jockey_seiseki_sanchaku = jockey_seiseki[2]
                hp.jokcey_seiseki_chakugai = jockey_seiseki[3]
                trainer = jockey_items[3].split("(")
                hp.trainer_name = trainer[0]
                hp.trainer_shozoku = trainer[1].replace(')','')
                
                #成績処理
                sl = r.find_all('td',valign='top')
                zenso_no = 1
                for s in sl:
                    race_infos = []
                    for s_elm in s.childGenerator():
                        if str(s_elm).find('br') < 0:
                            race_infos.append(s_elm)
                    kaisai_infos = race_infos[0].split('.')
                    course_name_z = kaisai_infos[0][:-2]
                    year = kaisai_infos[0][-2:]
                    month = kaisai_infos[1]
                    day = kaisai_infos[2][0:2]
                    ymd_z = year + month + day
                    
                    if s.span is not None:
                        order_of_arrival = s.span.text
                    else :
                        order_of_arrival = 0
                    
                    race_name_z = race_infos[2]
                    course_info = str(race_infos[3]).split(' ')
                    distance_z = int(course_info[0].replace('m',''))
                    left_right_z = course_info[1]
                    time_z = course_info[2]
                    baba_z = course_info[3]
                    goal_info = str(race_infos[4]).split(' ')
                    
                    if order_of_arrival == 0:
                        agari_3f = 9999
                        chakusa = 9999
                    else :
                        if goal_info[0] == '非計測':
                            agari_3f = 9999
                        else :
                            agari_3f = float(goal_info[0])
                        chakusa = float(goal_info[1])
                        
                    kinryo_z = float(str(race_infos[5])[0:4])
                    jockey_name_z = re.findall(r'(\d+|\D+)', str(race_infos[5]))[3]
                    
                    if len(race_infos) > 7:
                        pop_order = int(re.findall(r'(\d+|\D+)', str(race_infos[5]))[4])
                    else :
                        pop_order = 0
                    
                    gate_infos = str(race_infos[6]).split(' ')
                    num_of_all_horse = int(str(gate_infos[0]).replace('ト',''))
                    waku = str(gate_infos[1])[0]
                    weight = 0
                    if gate_infos[2] != '－' and gate_infos[2] != '計不':
                        weight = int(gate_infos[2])
                    corner1 = 0
                    corner2 = 0
                    corner3 = 0
                    corner4 = 0
                    
                    if len(race_infos) > 7:
                        corners = race_infos[7].split('-')
                        if len(corners) == 4:
                            corner1 = corners[::-1][3]
                        if len(corners) >= 3:
                            corner2 = corners[::-1][2]
                        if len(corners) >= 2:
                            corner3 = corners[::-1][1]
                        corner4 = corners[::-1][0]
                    
                    if len(race_infos) > 8:
                        win_horse = race_infos[8]
                    else :
                        win_horse = '競走除外等により不明'
                    
                    setattr(hp,"zenso"+str(zenso_no)+"_course_name",course_name_z)
                    setattr(hp,"zenso"+str(zenso_no)+"_ymd",ymd_z)
                    setattr(hp,"zenso"+str(zenso_no)+"_order_of_arrival",order_of_arrival)
                    setattr(hp,"zenso"+str(zenso_no)+"_race_name",race_name_z)
                    setattr(hp,"zenso"+str(zenso_no)+"_distance",distance_z)
                    setattr(hp,"zenso"+str(zenso_no)+"_left_right",left_right_z)
                    setattr(hp,"zenso"+str(zenso_no)+"_time",time_z)
                    setattr(hp,"zenso"+str(zenso_no)+"_baba",baba_z)
                    setattr(hp,"zenso"+str(zenso_no)+"_agari_3f",agari_3f)
                    setattr(hp,"zenso"+str(zenso_no)+"_chakusa",chakusa)
                    setattr(hp,"zenso"+str(zenso_no)+"_kinryo",kinryo_z)
                    setattr(hp,"zenso"+str(zenso_no)+"_jockey_name",jockey_name_z)
                    setattr(hp,"zenso"+str(zenso_no)+"_pop_order",pop_order)
                    setattr(hp,"zenso"+str(zenso_no)+"_num_of_all_horse",num_of_all_horse)
                    setattr(hp,"zenso"+str(zenso_no)+"_waku",waku)
                    setattr(hp,"zenso"+str(zenso_no)+"_weight",weight)
                    setattr(hp,"zenso"+str(zenso_no)+"_corner1",corner1)
                    setattr(hp,"zenso"+str(zenso_no)+"_corner2",corner2)
                    setattr(hp,"zenso"+str(zenso_no)+"_corner3",corner3)
                    setattr(hp,"zenso"+str(zenso_no)+"_corner4",corner4)
                    setattr(hp,"zenso"+str(zenso_no)+"_win_horse",win_horse)

                    zenso_no += 1
                session.add(hp)
                cnt += 1

session.commit()
