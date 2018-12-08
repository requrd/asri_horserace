import pandas as pd,tensorflow as tf,numpy as np,keras,sys
from sklearn.preprocessing import StandardScaler
from keras.models import Model,load_model
from jrdbdummies import CategoryGetter
from horseview.horsemodel import KaisaiData,PredictData,db

pred_date = sys.argv[1]
modelname = sys.argv[2]
#modelname = 'ResNet_jrdb_20180927_5output_2010_2017.h5'

#変数設定
num_max_horse = 18

##ここからDB操作
kaisais = KaisaiData.query.filter(KaisaiData.ymd == pred_date).all()

num_race = 0
for k in kaisais:
    num_race += len(k.races)
print(num_race)

#数値データ作成
num_score = 80
score_data = np.zeros([num_race,num_max_horse,num_score])
w = 0
for k in kaisais:
    for r in k.races:
        hn = 0
        for h in r.racehorses:
            score_data[w,hn,0]=k.turf_baba_in
            score_data[w,hn,1]=k.turf_baba_center
            score_data[w,hn,2]=k.turf_baba_out
            score_data[w,hn,3]=k.turf_baba_sa
            score_data[w,hn,4]=k.turf_baba_straight_saiuchi
            score_data[w,hn,5]=k.turf_baba_straight_in
            score_data[w,hn,6]=k.turf_baba_straight_center
            score_data[w,hn,7]=k.turf_baba_straight_out
            score_data[w,hn,8]=k.turf_baba_straight_oosoto
            score_data[w,hn,9]=k.dart_baba_in
            score_data[w,hn,10]=k.dart_baba_center
            score_data[w,hn,11]=k.dart_baba_out
            score_data[w,hn,12]=k.dart_baba_sa
            score_data[w,hn,13]=k.renzoku_day
            score_data[w,hn,14]=k.turf_length
            score_data[w,hn,15]=k.precipitation
            score_data[w,hn,16]=r.num_of_all_horse
            score_data[w,hn,17]=h.idm
            score_data[w,hn,18]=h.jockey_score
            score_data[w,hn,19]=h.info_score
            score_data[w,hn,20]=h.routin
            score_data[w,hn,21]=h.train_score
            score_data[w,hn,22]=h.trainer_score
            score_data[w,hn,23]=h.train_code
            score_data[w,hn,24]=h.trainer_hyoka_code
            score_data[w,hn,25]=h.jockey_rate_rentai
            score_data[w,hn,26]=h.gekiso_score
            score_data[w,hn,27]=h.kinryo
            score_data[w,hn,28]=h.kakutoku_money
            score_data[w,hn,29]=h.shukaku_money
            score_data[w,hn,30]=h.joken
            score_data[w,hn,31]=h.ten_score
            score_data[w,hn,32]=h.pace_score
            score_data[w,hn,33]=h.up_score
            score_data[w,hn,34]=h.position_score
            score_data[w,hn,35]=h.commit_weight
            score_data[w,hn,36]=h.commit_weight_increase
            score_data[w,hn,37]=h.gekiso_order
            score_data[w,hn,38]=h.ls_score_order
            score_data[w,hn,39]=h.ten_score_order
            score_data[w,hn,40]=h.pace_score_order
            score_data[w,hn,41]=h.up_score_order
            score_data[w,hn,42]=h.position_score_order
            score_data[w,hn,43]=h.expect_jokey_win_rate
            score_data[w,hn,44]=h.expect_jokey_rentai_rate
            score_data[w,hn,45]=h.taikei
            score_data[w,hn,46]=h.senaka
            score_data[w,hn,47]=h.do
            score_data[w,hn,48]=h.siri
            score_data[w,hn,49]=h.tomo
            score_data[w,hn,50]=h.harabukuro
            score_data[w,hn,51]=h.head
            score_data[w,hn,52]=h.neck
            score_data[w,hn,53]=h.breast
            score_data[w,hn,54]=h.shoulder
            score_data[w,hn,55]=h.zencho
            score_data[w,hn,56]=h.kocho
            score_data[w,hn,57]=h.maehaba
            score_data[w,hn,58]=h.ushirohaba
            score_data[w,hn,59]=h.maetsunagi
            score_data[w,hn,60]=h.ushirotsunagi
            score_data[w,hn,61]=h.tail
            score_data[w,hn,62]=h.furikata
            score_data[w,hn,63]=h.horse_start_score
            score_data[w,hn,64]=h.horse_latestart_rate
            score_data[w,hn,65]=h.mambaken_score
            score_data[w,hn,66]=h.runtimes_first_train
            score_data[w,hn,67]=h.days_after_first_train
            score_data[w,hn,68]=h.trainer_rank
            score_data[w,hn,69]=h.trainanalysis.oikiri_score
            score_data[w,hn,70]=h.trainanalysis.shiage_score
            score_data[w,hn,71]=h.trainoikiri.kaisu
            score_data[w,hn,72]=h.trainoikiri.train_f
            score_data[w,hn,73]=h.trainoikiri.ten_f
            score_data[w,hn,74]=h.trainoikiri.mid_f
            score_data[w,hn,75]=h.trainoikiri.end_f
            score_data[w,hn,76]=h.trainoikiri.ten_f_score
            score_data[w,hn,77]=h.trainoikiri.mid_f_score
            score_data[w,hn,78]=h.trainoikiri.end_f_score
            score_data[w,hn,79]=h.trainoikiri.oikiri_score
            hn += 1
        w = w +1

#数値データの標準化
sds = score_data
ss = StandardScaler()

i = 0
for s in score_data:
    ss.fit(s)
    sds[i] = ss.transform(s)
    i += 1

#カテゴリデータ作成
cg = CategoryGetter()
wnr = 0
w = 0
cdw = []
for i in range(len(kaisais)):
    w_kaisai = kaisais[i]
    for j in range(len(w_kaisai.races)):
        w_race = w_kaisai.races[j]
        for k in range (len(w_race.racehorses)):
            w_horse = w_race.racehorses[k]
            w_hdummies = np.zeros([0])
            
            #開催データ
            w_tennatsu=cg.getTennatsu(w_kaisai.tennatsu)
            
            #レースデータ
            w_distance=cg.getDistance(w_race.distance)
            
            #競走馬データ
            w_bacode=cg.getBacode(w_horse.bacode)
            w_num=cg.getNum(w_horse.num)            
            w_waku=cg.getWaku(w_horse.waku)            
            w_torikeshi=cg.getTorikeshi(w_horse.torikeshi)
            w_banushikai_code=cg.getBanushikaicode(w_horse.banushikai_code)
            w_train_type=cg.getTraintype(w_horse.trainanalysis.train_type)
            
            w_hdummies = np.hstack((
                       w_tennatsu,

                       w_distance,

                       w_bacode,
                       w_num,
                       w_torikeshi,
                       w_banushikai_code,
                       w_train_type
                      ))
            if k == 0:
                w_vdummies = w_hdummies
            else :
                w_vdummies = np.vstack((w_vdummies,w_hdummies))
            w += 1
        cdw.append(w_vdummies)
        wnr += 1
    
category_data = np.zeros([num_race,num_max_horse,len(cdw[0][0])])

for i in range(num_race):
    for j in range(len(cdw[i])):
        category_data[i][j] = cdw[i][j]

x_data = np.concatenate((sds,category_data),axis=2)

#モデルの読み込み
model = load_model(modelname)

preds = model.predict(x_data)
w = 0
for k in kaisais:
    for r in k.races:
        for h in r.racehorses:
            hn = h.num - 1
            pp1 = preds[0][w][hn]
            pp2 = preds[1][w][hn]
            pp3 = preds[2][w][hn]
            pp4 = preds[3][w][hn]
            pp5 = preds[4][w][hn]
            rentai_rate = 1 - ((1 - pp1) * (1 - pp2))
            fukusho_rate = 1 - ((1 - pp1) * (1 - pp2) * (1 - pp3))
            pd = PredictData(racehorsekey = h.racehorsekey,pp_icchaku = float(pp1), rentai_rate = rentai_rate, fukusho_rate = fukusho_rate,tansho_odds = 1/pp1, fukusho_odds = 1/fukusho_rate)
            db.session.add(pd)
        w += 1
db.session.commit()          
