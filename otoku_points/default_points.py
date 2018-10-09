import pandas as pd
import numpy as np
from jrdbdummies import CategoryGetter

#変数設定
num_max_horse = 18

#汎用DBロード
from sqlalchemy import create_engine
from database_setup import *
from sqlalchemy.orm import sessionmaker

##ここからDB操作
engine = create_engine('sqlite:///jrdb.db')
Base.metadata.bind=engine
Session = sessionmaker(bind=engine)
session = Session()

kaisais = session.query(KaisaiData).order_by(KaisaiData.ymd).filter(KaisaiData.ymd >= '20100101',KaisaiData.ymd <= '20171231').all()

#芝処理
w_winret = []
w_placeret = []
points = []
cg = CategoryGetter()

for i in range(len(kaisais)):
    for j in range(len(kaisais[i].races)):
        w_race = kaisais[i].races[j]
        if w_race.tdscode == 1:
            n = len(w_race.racehorses_w)
            idm_mat = np.zeros(n)
            winhorse = w_race.returninfo.win1_num
            winret = w_race.returninfo.win1_ret
            p1 = w_race.returninfo.place1_num
            p1_ret = w_race.returninfo.place1_ret
            p2 = w_race.returninfo.place2_num
            p2_ret = w_race.returninfo.place2_ret
            p3 = w_race.returninfo.place3_num
            p3_ret = w_race.returninfo.place3_ret
            
#★★★ 岡宮追記　start ★★★
            jockey_score_mat = np.zeros(n)
            info_score_mat = np.zeros(n)
            train_score_mat = np.zeros(n)
            trainer_score_mat = np.zeros(n)
            jockey_rate_rentai_mat = np.zeros(n)
            gekiso_score_mat = np.zeros(n)
            pace_score_mat = np.zeros(n)
            up_score_mat = np.zeros(n)
            position_score_mat = np.zeros(n)
            ls_score_order_mat = np.zeros(n)
            ten_score_order_mat = np.zeros(n)
            pace_score_order_mat = np.zeros(n)
            up_score_order_mat = np.zeros(n)
            position_score_order_mat = np.zeros(n)
            expect_jokey_win_rate_mat = np.zeros(n)
            expect_jokey_rentai_rate_mat = np.zeros(n)
            horse_start_score_mat = np.zeros(n)
            mambaken_score_mat = np.zeros(n)
            train_oikiri_score_mat = np.zeros(n)
            shiage_score_mat = np.zeros(n)
            end_f_score_mat = np.zeros(n)
            oikiri_score_mat = np.zeros(n)
#★★★ 岡宮追記　end ★★★

            
        
            #順位データの入力、払戻金の設定
            for k in range(n):
                w_horse = w_race.racehorses_w[k]
                idm_mat[k] = w_horse.idm           
                
#★★★ 岡宮追記　start ★★★
                jockey_score_mat[k] = w_horse.jockey_score
                info_score_mat[k] = w_horse.info_score
                train_score_mat[k] = w_horse.train_score
                trainer_score_mat[k] = w_horse.trainer_score
                jockey_rate_rentai_mat[k] = w_horse.jockey_rate_rentai
                gekiso_score_mat[k] = w_horse.gekiso_score
                pace_score_mat[k] = w_horse.pace_score
                up_score_mat[k] = w_horse.up_score
                position_score_mat[k] = w_horse.position_score
                ls_score_order_mat[k] = w_horse.ls_score_order
                ten_score_order_mat[k] = w_horse.ten_score_order
                pace_score_order_mat[k] = w_horse.pace_score_order
                up_score_order_mat[k] = w_horse.up_score_order
                position_score_order_mat[k] = w_horse.position_score_order
                expect_jokey_win_rate_mat[k] = w_horse.expect_jokey_win_rate
                expect_jokey_rentai_rate_mat[k] = w_horse.expect_jokey_rentai_rate
                horse_start_score_mat[k] = w_horse.horse_start_score
                mambaken_score_mat[k] = w_horse.mambaken_score
                train_oikiri_score_mat[k] = w_horse.train_oikiri_score
                shiage_score_mat[k] = w_horse.shiage_score
                end_f_score_mat[k] = w_horse.end_f_score
                oikiri_score_mat[k] = w_horse.oikiri_score
#★★★ 岡宮追記　end ★★★
                
                
                #払戻金処理
                if winhorse -1 == k:
                    w_winret.append(winret)
                else:
                    w_winret.append(0)
                if p1 - 1 == k:
                    w_placeret.append(p1_ret)
                elif p2 - 1 == k:
                    w_placeret.append(p2_ret)
                elif p3 - 1 == k:
                    w_placeret.append(p3_ret)
                else :
                    w_placeret.append(0)
                    
            idm_orders = np.argsort(idm_mat)[::-1]
            
#★★★ 岡宮追記　start ★★★
            jockey_score_orders = np.argsort(jockey_score_mat)[::-1]
            info_score_orders = np.argsort(info_score_mat)[::-1]
            train_score_orders = np.argsort(train_score_mat)[::-1]
            trainer_score_orders = np.argsort(trainer_score_mat)[::-1]
            jockey_rate_rentai_orders = np.argsort(jockey_rate_rentai_mat)[::-1]
            gekiso_score_orders = np.argsort(gekiso_score_mat)[::-1]
            pace_score_orders = np.argsort(pace_score_mat)[::-1]
            up_score_orders = np.argsort(up_score_mat)[::-1]
            position_score_orders = np.argsort(position_score_mat)[::-1]
            ls_score_order_orders = np.argsort(ls_score_order_mat)[::-1]
            ten_score_order_orders = np.argsort(ten_score_order_mat)[::-1]
            pace_score_order_orders = np.argsort(pace_score_order_mat)[::-1]
            up_score_order_orders = np.argsort(up_score_order_mat)[::-1]
            position_score_order_orders = np.argsort(position_score_order_mat)[::-1]
            expect_jokey_win_rate_orders = np.argsort(expect_jokey_win_rate_mat)[::-1]
            expect_jokey_rentai_rate_orders = np.argsort(expect_jokey_rentai_rate_mat)[::-1]
            horse_start_score_orders = np.argsort(horse_start_score_mat)[::-1]
            mambaken_score_orders = np.argsort(mambaken_score_mat)[::-1]
            train_oikiri_score_orders = np.argsort(train_oikiri_score_mat)[::-1]
            shiage_score_orders = np.argsort(shiage_score_mat)[::-1]
            end_f_score_orders = np.argsort(end_f_score_mat)[::-1]
            oikiri_score_orders = np.argsort(oikiri_score_mat)[::-1]
#★★★ 岡宮追記　end ★★★
            #得点加算処理
            for l in range(n):
                wp = 0
                w_horse_p = w_race.racehorses_w[l]

                #IDM順位
                if n >8:
                    #4位以内でプラス
                    for m in range(4):
                        if idm_orders[m] == l:
                            wp += 1
                    #9位以降でマイナス
                    for m in range(9,n):
                        if idm_orders[m] == l:
                            wp -= 1
                        
                #カテゴリ変数
                #馬番号
                even_odd = w_horse.num%2
                if even_odd == 0:
                    wp += 1
                
                #脚質
                if int(w_horse.leg_type) == 2:
                    wp += 1
                
                #ブリンカー
                if (w_horse.brinkers == 1) or (w_horse.brinkers == 2):
                    wp -= 1
                    
                #見習い
                if (w_horse.minarai == 1) or (w_horse.minarai == 3):
                    wp -= 1
                
                #降級フラグ
                if w_horse.kokyu_flg == 1:
                    wp += 1
                #騎手印
                if w_horse.jockey_shirushi != 0:
                    wp += 1
                    
                #芝適性
                if (w_horse.turf_adjust_code == 0) or (w_horse.turf_adjust_code == 3):
                    wp -= 1
                
                #ダ適性
                if w_horse.dart_adjust_code == 0:
                    wp -= 1
                
                #性別
                racejoken = w_race.kigo
                if racejoken >= 100:
                    racejoken = racejoken%100
                if (racejoken / 10) >= 1 and (racejoken / 10) < 2:
                    wp -= 1
                
                #馬記号
                #芝はなし
                
                #輸送
                if (w_horse.yuso == 0) or (w_horse.yuso == 4) or (w_horse.yuso == 1):
                    wp -= 1
                
                #降級フラグ
                if w_horse.kokyu_flg == 1:
                    wp += 1
                #激走タイプ
                if np.argmax(cg.getGekisotype(w_horse.gekiso_type)) == 4:
                    wp += 1
                elif np.argmax(cg.getGekisotype(w_horse.gekiso_type)) == 5:
                    wp -= 1
                    
                #芝ダ障フラグ
                if w_horse.turf_dart_steeple_flg == 2:
                    wp -= 1
                    
                #距離フラグ
                if w_horse.distance_flg == 1:
                    wp -= 1
                
                #クラスフラグ
                if (w_horse.class_flg == 1) or (w_horse.class_flg == 1):
                    wp += 1
                    
                #転厩フラグ
                if (w_horse.tenkyu_flg == 1) or (w_horse.tenkyu_flg == 2):
                    wp -= 1
                elif w_horse.tenkyu_flg == 3:
                    wp += 1
                    
                #調教タイプ
                tt = np.argmax(cg.getTraintype(w_horse.train_type))
                if (tt == 3) or (tt == 6) or (tt == 9) or (tt == 10):
                    wp -= 1
                    
                #調教コース種類
                if (w_horse.train_course_kind == 0) or (w_horse.train_course_kind == 2):
                    wp -= 1
                    
                #坂
                if w_horse.saka == 0:
                    wp -= 1
                    
                #ウッドチップ
                if w_horse.wood == 0:
                    wp -= 1
                    
                #ダート
                if w_horse.dart == 1:
                    wp -= 1
                #芝
                if w_horse.turf == 1:
                    wp -= 1
                #ポリトラック
                if w_horse.politruck == 1:
                    wp -= 1
                    
                #調教距離
                if w_horse.train_distance == 1:
                    wp -= 1
                    
                #調教重点
                if (w_horse.train_juten != 3):
                    wp -= 1
                    
                #調教量評価
                if np.argmax(cg.getTrainvolhyoka(w_horse.train_vol_hyoka)) >= 3:
                    wp -= 1
                    
                #追切種類
                if w_horse.oikiri_kind != 3:
                    wp -= 1
                    
                #前走１コース位置
                if (w_horse.zenso1_course_position == 3) or (w_horse.zenso1_course_position == 4):
                    wp -= 1
                    
                #前走1脚質
                if int(w_horse.zenso1_race_leg_type) == 2:
                    wp += 1
                elif int(w_horse.zenso1_race_leg_type) >= 3:
                    wp -= 1
                    
                #前走1,4角コース取り
                if (w_horse.zenso1_corner4_course_position == 0) or (w_horse.zenso1_corner4_course_position == 2):
                    wp -= 1
                    
                #前走2コース位置
                if w_horse.zenso2_course_position == 2:
                    wp -= 1
                #前走2脚質
                if int(w_horse.zenso2_race_leg_type) >= 3:
                    wp -= 1
                elif int(w_horse.zenso2_race_leg_type) == 0:
                    wp += 1
                    
                #前走3コース位置
                if (w_horse.zenso3_course_position == 3) or (w_horse.zenso3_course_position == 4):
                    wp -= 1
                    
                #前走3脚質
                if int(w_horse.zenso3_race_leg_type) >= 4:
                    wp -= 1
                elif int(w_horse.zenso3_race_leg_type) == 1:
                    wp += 1

#★★★ 岡宮追記　start ★★★
                g = 8
                if (g > n):
                    g = n
                for m in range(0,g):
                    if jockey_score_orders[m] == l:
                        wp +=1
                if info_score_orders[4] == l:	
                    wp +=1
                for m in range(0,5):
                    if train_score_orders[m] == l:
                        wp +=1
                for m in range(0,5):
                    if trainer_score_orders[m] == l:	
                        wp +=1
                if (n > 7):
                    if trainer_score_orders[6] == l:
                        wp +=2
                g = 6
                if (g > n):
                    g = n
                for m in range(0,g):
                    if jockey_rate_rentai_orders[m] == l:
                        wp +=1
                if (n > 7):
                    if jockey_rate_rentai_orders[7] == l:
                        wp +=2
                for m in range(0,4):
                    if gekiso_score_orders[m] == l:
                        wp +=1
                for m in range(0,4):
                    if ten_score_order_orders[m] == l:
                        wp +=1
                for m in range(0,3):
                    if pace_score_orders[m] == l:	
                        wp +=1
                for m in range(0,3):
                    if up_score_orders[m] == l:
                        wp +=1
                if position_score_orders[2] == l:	
                    wp +=1
                g = 6
                if (g > n):
                    g = n
                for m in range(0,g):
                    if ls_score_order_orders[m] == l:
                        wp -=1
                for m in range(14,n):
                    if ten_score_order_orders[m] == l:
                        wp +=1
                for m in range(15,n):
                    if pace_score_order_orders[m] == l:
                        wp +=1
                if (n > 7):
                    if up_score_order_orders[7] == l:
                        wp +=1
                for m in range(12,n):
                    if position_score_order_orders[m] == l:
                        wp +=1
                g = 8
                if (g > n):
                    g = n
                for m in range(0,g):
                    if expect_jokey_win_rate_orders[m] == l:
                        wp +=1
                g = 8
                if (g > n):
                    g = n
                for m in range(2,g):
                    if expect_jokey_rentai_rate_orders[m] == l:
                        wp +=1
                if (n > 7):
                    if horse_start_score_orders[7] == l:
                        wp +=1
                if (n > 6):
                    if mambaken_score_orders[6] == l:
                        wp +=1
                for m in range(0,3):
                    if train_oikiri_score_orders[m] == l:
                        wp +=1
                for m in range(0,4):
                    if shiage_score_orders[m] == l:
                        wp -=0
                for m in range(0,2):
                    if end_f_score_orders[m] == l:
                        wp +=1
                for m in range(0,3):
                    if oikiri_score_orders[m] == l:
                        wp +=1


                #調教矢印コード
                if w_horse.train_code == 1:
                    wp +=1
                if w_horse.train_code == 2:
                    wp +=1
                #siri
                if w_horse.siri == 3:
                    wp -=1
                #tomo
                if w_horse.tomo == 3:
                    wp -=1
                #neck
                if w_horse.neck == 1:
                    wp -=1
                #breast
                if w_horse.breast == 1:	
                    wp +=1
                if w_horse.breast == 3:
                    wp -=1
                #maehaba
                if w_horse.maehaba == 0:
                    wp -=1
                if w_horse.maehaba == 1:
                    wp -=1
                #ushirohaba
                if w_horse.ushirohaba == 0:
                    wp -=1
                if w_horse.ushirohaba == 1:
                    wp -=1
                #厩舎ランク
                if w_horse.trainer_rank == 0:
                    wp -=1
                if w_horse.trainer_rank == 8:
                    wp -=1
                if w_horse.trainer_rank == 2:
                    wp +=1
                #回数
                if w_horse.kaisu == 0:
                    wp -=1
                #出遅
                if w_horse.zenso1_start_late>=2 and w_horse.zenso1_start_late <= n:
                    wp -=1
                #位置取
                if w_horse.zenso1_position == 3:
                    wp -=1
                #コーナー順位４
                if w_horse.zenso1_corner_order4 >= 1 and w_horse.zenso1_corner_order4 <= 4:
                    wp +=1
                if w_horse.zenso1_corner_order4 >= 14 and w_horse.zenso1_corner_order4 <= n:
                    wp -=1               
                points.append(wp)
                
t_ret = []

for i in range(len(points)):
    t_ret.append([points[i],w_winret[i],w_placeret[i]])

print("芝頭数:",len(t_ret))

#ダート処理
w_winret = []
w_placeret = []
points = []
cg = CategoryGetter()

for i in range(len(kaisais)):
    for j in range(len(kaisais[i].races)):
        w_race = kaisais[i].races[j]
        if w_race.tdscode == 2:
            n = len(w_race.racehorses_w)
            idm_mat = np.zeros(n)
            
#★★★ 岡宮追記　start ★★★            
            jockey_score_mat = np.zeros(n)
            train_score_mat = np.zeros(n)
            trainer_score_mat = np.zeros(n)
            jockey_rate_rentai_mat = np.zeros(n)
            gekiso_score_mat = np.zeros(n)
            pace_score_mat = np.zeros(n)
            up_score_mat = np.zeros(n)
            position_score_mat = np.zeros(n)
            ls_score_order_mat = np.zeros(n)
            ten_score_order_mat = np.zeros(n)
            pace_score_order_mat = np.zeros(n)
            up_score_order_mat = np.zeros(n)
            up_score_order_mat = np.zeros(n)
            position_score_order_mat = np.zeros(n)
            expect_jokey_win_rate_mat = np.zeros(n)
            expect_jokey_rentai_rate_mat = np.zeros(n)
            mambaken_score_mat = np.zeros(n)
            train_oikiri_score_mat = np.zeros(n)
            shiage_score_mat = np.zeros(n)
            end_f_score_mat = np.zeros(n)
            oikiri_score_mat = np.zeros(n)
            zenso1_natural_score_mat = np.zeros(n)
            zenso1_racep_score_mat = np.zeros(n)
#★★★ 岡宮追記　end ★★★            
            
            winhorse = w_race.returninfo.win1_num
            winret = w_race.returninfo.win1_ret
            p1 = w_race.returninfo.place1_num
            p1_ret = w_race.returninfo.place1_ret
            p2 = w_race.returninfo.place2_num
            p2_ret = w_race.returninfo.place2_ret
            p3 = w_race.returninfo.place3_num
            p3_ret = w_race.returninfo.place3_ret
        
            #順位データの入力、払戻金の設定
            for k in range(n):
                w_horse = w_race.racehorses_w[k]
                idm_mat[k] = w_horse.idm          
                
#★★★ 岡宮追記　start ★★★                        
                jockey_score_mat[k] = w_horse.jockey_score
                train_score_mat[k] = w_horse.train_score
                trainer_score_mat[k] = w_horse.trainer_score
                jockey_rate_rentai_mat[k] = w_horse.jockey_rate_rentai
                gekiso_score_mat[k] = w_horse.gekiso_score
                pace_score_mat[k] = w_horse.pace_score
                up_score_mat[k] = w_horse.up_score
                position_score_mat[k] = w_horse.position_score
                ls_score_order_mat[k] = w_horse.ls_score_order
                ten_score_order_mat[k] = w_horse.ten_score_order
                pace_score_order_mat[k] = w_horse.pace_score_order
                up_score_order_mat[k] = w_horse.up_score_order
                position_score_order_mat[k] = w_horse.position_score_order
                expect_jokey_win_rate_mat[k] = w_horse.expect_jokey_win_rate
                expect_jokey_rentai_rate_mat[k] = w_horse.expect_jokey_rentai_rate
                mambaken_score_mat[k] = w_horse.mambaken_score
                train_oikiri_score_mat[k] = w_horse.train_oikiri_score
                shiage_score_mat[k] = w_horse.shiage_score
                end_f_score_mat[k] = w_horse.end_f_score
                oikiri_score_mat[k] = w_horse.oikiri_score
                zenso1_natural_score_mat[k] = w_horse.zenso1_natural_score
                zenso1_racep_score_mat[k] = w_horse.zenso1_racep_score
#★★★ 岡宮追記　end ★★★       
                               
                #払戻金処理
                if winhorse -1 == k:
                    w_winret.append(winret)
                else:
                    w_winret.append(0)
                if p1 - 1 == k:
                    w_placeret.append(p1_ret)
                elif p2 - 1 == k:
                    w_placeret.append(p2_ret)
                elif p3 - 1 == k:
                    w_placeret.append(p3_ret)
                else :
                    w_placeret.append(0)

            idm_orders = np.argsort(idm_mat)[::-1]

#★★★ 岡宮追記　start ★★★                        
            jockey_score_orders = np.argsort(jockey_score_mat)[::-1]
            train_score_orders = np.argsort(train_score_mat)[::-1]
            trainer_score_orders = np.argsort(trainer_score_mat)[::-1]
            jockey_rate_rentai_orders = np.argsort(jockey_rate_rentai_mat)[::-1]
            gekiso_score_orders = np.argsort(gekiso_score_mat)[::-1]
            pace_score_orders = np.argsort(pace_score_mat)[::-1]
            up_score_orders = np.argsort(up_score_mat)[::-1]
            position_score_orders = np.argsort(position_score_mat)[::-1]
            ls_score_order_orders = np.argsort(ls_score_order_mat)[::-1]
            ten_score_order_orders = np.argsort(ten_score_order_mat)[::-1]
            pace_score_order_orders = np.argsort(pace_score_order_mat)[::-1]
            up_score_order_orders = np.argsort(up_score_order_mat)[::-1]
            position_score_order_orders = np.argsort(position_score_order_mat)[::-1]
            expect_jokey_win_rate_orders = np.argsort(expect_jokey_win_rate_mat)[::-1]
            expect_jokey_rentai_rate_orders = np.argsort(expect_jokey_rentai_rate_mat)[::-1]
            mambaken_score_orders = np.argsort(mambaken_score_mat)[::-1]
            train_oikiri_score_orders = np.argsort(train_oikiri_score_mat)[::-1]
            shiage_score_orders = np.argsort(shiage_score_mat)[::-1]
            end_f_score_orders = np.argsort(end_f_score_mat)[::-1]
            oikiri_score_orders = np.argsort(oikiri_score_mat)[::-1]
            zenso1_natural_score_orders = np.argsort(zenso1_natural_score_mat)[::-1]
            zenso1_racep_score_orders = np.argsort(zenso1_racep_score_mat)[::-1]
#★★★ 岡宮追記　end ★★★                        

            
            #得点加算処理
            for l in range(n):
                wp = 0
                w_horse_p = w_race.racehorses_w[l]
                
                #IDM順位
                if n>8:
                    #4位以内でプラス
                    for m in range(4):
                        if idm_orders[m] == l:
                            wp += 1
                    #9位以降でマイナス
                    for m in range(9,n):
                        if idm_orders[m] == l:
                            wp -= 1
                        
                #カテゴリ変数
                #馬番号
                even_odd = w_horse.num%2
                if even_odd == 0:
                    wp += 1
                
                #脚質
                if int(w_horse.leg_type) == 2:
                    wp += 1
                
                #ブリンカー
                if (w_horse.brinkers == 1) or (w_horse.brinkers == 2):
                    wp -= 1
                    
                #見習い
                if (w_horse.minarai == 1) or (w_horse.minarai == 3):
                    wp -= 1
                
                #降級フラグ
                if w_horse.kokyu_flg == 1:
                    wp += 1
                #騎手印
                if w_horse.jockey_shirushi != 0:
                    wp += 1
                    
                #芝適性
                if (w_horse.turf_adjust_code == 0) or (w_horse.turf_adjust_code == 3):
                    wp -= 1
                
                #ダ適性
                if w_horse.dart_adjust_code == 0:
                    wp -= 1
                
                #性別
                racejoken = w_race.kigo
                if racejoken >= 100:
                    racejoken = racejoken%100
                if (racejoken / 10) >= 1 and (racejoken / 10) < 2:
                    wp -= 1
                
                #馬記号
                if w_horse.umakigo_code == 6:
                    wp += 1
                
                #輸送
                if (w_horse.yuso == 0) or (w_horse.yuso == 4):
                    wp -= 1
                
                #降級フラグ
                if w_horse.kokyu_flg == 1:
                    wp += 1

                #激走タイプ
                gt = np.argmax(cg.getGekisotype(w_horse.gekiso_type))
                if (gt == 1) or (gt == 3):
                    wp += 1
                elif (gt == 5) or (gt == 6):
                    wp -= 1

                #芝ダ障フラグ
                if w_horse.turf_dart_steeple_flg == 1:
                    wp -= 1
                    
                #距離フラグ
                if w_horse.distance_flg == 1:
                    wp -= 1
                
                #クラスフラグ
                if (w_horse.class_flg == 1) or (w_horse.class_flg == 1):
                    wp += 1
                    
                #転厩フラグ
                if (w_horse.tenkyu_flg == 1) or (w_horse.tenkyu_flg == 2):
                    wp -= 1
                elif w_horse.tenkyu_flg == 3:
                    wp += 1
                    
                #調教タイプ
                tt = np.argmax(cg.getTraintype(w_horse.train_type))
                if (tt == 1) or (tt == 8):
                    wp += 1
                if (tt == 0) or (tt >= 5 and tt <= 7) or (tt >= 9):
                    wp -= 1
                    
                #調教コース種類
                if (w_horse.train_course_kind == 0) or (w_horse.train_course_kind == 2):
                    wp -= 1
                    
                #坂
                if w_horse.saka == 0:
                    wp -= 1
                    
                #ウッドチップ
                if w_horse.wood == 0:
                    wp -= 1
                    
                #ダート
                if w_horse.dart == 1:
                    wp -= 1
                #芝
                if w_horse.turf == 1:
                    wp -= 1
                #ポリトラック
                #ダートではマイナス要素なし
                    
                #調教距離
                if w_horse.train_distance == 1:
                    wp -= 1
                    
                #調教重点
                if (w_horse.train_juten != 3):
                    wp -= 1
                    
                #調教量評価
                if np.argmax(cg.getTrainvolhyoka(w_horse.train_vol_hyoka)) >= 2:
                    wp -= 1
                    
                #追切種類
                if w_horse.oikiri_kind == 0:
                    wp -= 1
                    
                #前走１コース位置
                if w_horse.zenso1_course_position == 1:
                    wp -= 1
                    
                #前走1脚質
                if int(w_horse.zenso1_race_leg_type) >= 3:
                    wp -= 1
                    
                #前走1,4角コース取り
                if (w_horse.zenso1_corner4_course_position == 0) or (w_horse.zenso1_corner4_course_position == 2):
                    wp -= 1
                    
                #前走2コース位置
                #ダートは特になし

                #前走2脚質
                if int(w_horse.zenso2_race_leg_type) >= 3:
                    wp -= 1
                elif int(w_horse.zenso2_race_leg_type) == 1:
                    wp += 1
                    
                #前走3コース位置
                if (w_horse.zenso3_course_position == 3) or (w_horse.zenso3_course_position == 4):
                    wp -= 1
                    
                #前走3脚質
                if int(w_horse.zenso3_race_leg_type) >= 3:
                    wp -= 1
                    
                    
#★★★ 岡宮追記　start ★★★
                g = 8
                if (g > n):
                    g = n
                for m in range(0,g):
                    if jockey_score_orders[m] == l:
                        wp +=1
                if info_score_orders[5] == l:
                    wp +=1
                for m in range(0,5):
                    if train_score_orders[m] == l:
                        wp +=1
                if (n > 7):
                    if train_score_orders[7] == l:
                        wp +=2
                for m in range(0,5):
                    if trainer_score_orders[m] == l:
                        wp +=1
                if (n > 9):
                    if trainer_score_orders[6] == l:
                        wp +=2
                for m in range(0,6):
                    if jockey_rate_rentai_orders[m] == l:
                        wp +=1
                for m in range(0,4):
                    if gekiso_score_orders[m] == l:
                        wp +=1
                for m in range(0,3):
                    if pace_score_orders[m] == l:
                        wp +=1
                for m in range(0,3):
                    if up_score_orders[m] == l:
                        wp +=1
                for m in range(2,n):
                    if up_score_orders[m] == l:
                        wp +=2
                if position_score_orders[2] == l:
                    wp +=1
                for m in range(0,6):
                    if ls_score_order_orders[m] == l:
                        wp -=1
                for m in range(14,n):
                    if ten_score_order_orders[m] == l:
                        wp +=1
                for m in range(15,n):
                    if pace_score_order_orders[m] == l:
                        wp +=1
                if (n > 7):
                    if up_score_order_orders[7] == l:
                        wp -=0
                for m in range(15,n):
                    if up_score_order_orders[m] == l:
                        wp +=1
                g = 15
                if (g > n):
                    g = n
                for m in range(12,g):
                    if position_score_order_orders[m] == l:
                        wp +=1
                g = 8
                if (g > n):
                    g = n
                for m in range(0,g):
                    if expect_jokey_win_rate_orders[m] == l:
                        wp +=1
                g = 8
                if (g > n):
                    g = n
                for m in range(2,g):
                    if expect_jokey_rentai_rate_orders[m] == l:
                        wp +=1
                if (n > 9):
                    if expect_jokey_rentai_rate_orders[9] == l:
                        wp +=2
                if (n > 9):
                    if mambaken_score_orders[6] == l:
                        wp +=1
                for m in range(0,3):
                    if train_oikiri_score_orders[m] == l:
                        wp +=1
                for m in range(0,4):
                    if shiage_score_orders[m] == l:
                        wp -=0
                for m in range(0,2):
                    if end_f_score_orders[m] == l:
                        wp +=1
                if end_f_score_orders[3] == l:
                    wp +=2
                for m in range(0,3):
                    if oikiri_score_orders[m] == l:
                        wp +=1
                for m in range(0,4):
                    if zenso1_natural_score_orders[m] == l:
                        wp +=1
                if zenso1_racep_score_orders[1] == l:
                    wp +=2


                if w_horse.train_code == 1:
                    wp +=1
                if w_horse.trainer_hyoka_code == 1:
                    wp +=1
                if w_horse.tomo == 3:
                    wp -=1
                if w_horse.head == 3:
                    wp +=1
                if w_horse.breast == 1:
                    wp +=1
                if w_horse.kocho == 1:
                    wp -=1
                if w_horse.maehaba == 0:
                    wp -=1
                if w_horse.maehaba == 1:
                    wp -=1
                if w_horse.ushirohaba == 0:
                    wp -=1
                if w_horse.ushirohaba == 1:
                    wp -=1
                if w_horse.maetsunagi == 3:
                    wp -=1
                if w_horse.ushirotsunagi == 3:
                    wp -=1
                if w_horse.trainer_rank == 0:
                    wp -=1
                if w_horse.trainer_rank == 8:
                    wp -=1
                if w_horse.trainer_rank >=1 and w_horse.trainer_rank <=3:
                    wp +=1
                if w_horse.kaisu == 3:
                    wp -=1
                if w_horse.zenso1_start_late>=2 and w_horse.zenso1_start_late<=n:
                    wp -=1
                if w_horse.zenso1_position == 3:
                    wp +=1
                if w_horse.zenso1_corner_order4>=5 and w_horse.zenso1_corner_order4<=6:
                    wp +=1
                if w_horse.zenso1_corner_order4>=15 and w_horse.zenso1_corner_order4<=17:
                    wp +=1
                
                points.append(wp)
                
d_ret = []

for i in range(len(points)):
    d_ret.append([points[i],w_winret[i],w_placeret[i]])

print("ダ頭数:",len(d_ret))

#芝テスト用
win = 0
place = 0
winb = 0
plcb = 0
winc = 0
plc = 0
for i in range(len(t_ret)):
    point = t_ret[i][0]
    winb += 1
    plcb += 1
    win += t_ret[i][1]
    place += t_ret[i][2]
    if t_ret[i][1] > 0:
        winc += 1
    if t_ret[i][2] > 0:
        plc += 1
    
print(win/winb)
print(place/plcb)
print(winc/winb)
print(plc/plcb)
print(winb)
print(win)
print(place)

#ダテスト用
win = 0
place = 0
winb = 0
plcb = 0
winc = 0
plc = 0
for i in range(len(d_ret)):
    point = d_ret[i][0]
    winb += 1
    plcb += 1
    win += d_ret[i][1]
    place += d_ret[i][2]
    if d_ret[i][1] > 0:
        winc += 1
    if d_ret[i][2] > 0:
        plc += 1
    
print(win/winb)
print(place/plcb)
print(winc/winb)
print(plc/plcb)
print(winb)
print(win)
print(place)

#芝回収率
#得点順にソート
w_t_ret = np.zeros([len(t_ret),len(t_ret[0])])
for i in range(len(t_ret)):
    w_t_ret[i] = t_ret[i]
po = np.argsort(w_t_ret[:,0])

#回収率チェック
ptret = []
for i in range(len(t_ret)):
    w_horse_num = po[i]
    tp = t_ret[w_horse_num][0]
    twr = t_ret[w_horse_num][1]
    tpr = t_ret[w_horse_num][2]
    if i == 0:
        mp = tp
        print("mp:",mp)
        w_win_ret = 0
        w_place_ret = 0
        cnt = 0
        win_cnt = 0
        place_cnt = 0
    if mp == tp:
        w_win_ret += twr
        w_place_ret += tpr
        cnt += 1
        if twr > 0:
            win_cnt += 1
        if tpr > 0:
            place_cnt += 1
    else:
        ptret.append([mp,(w_win_ret/cnt),(w_place_ret/cnt),(win_cnt/cnt),(place_cnt/cnt),w_win_ret,w_place_ret,cnt])
        mp = tp
        w_win_ret = twr
        w_place_ret = tpr
        cnt = 1
        if twr > 0:
            win_cnt = 1
        else :
            win_cnt = 0
        if tpr > 0:
            place_cnt = 1
        else :
            place_cnt = 0
    if i == len(t_ret) - 1:
        ptret.append([mp,w_win_ret/cnt,w_place_ret/cnt,win_cnt/cnt,place_cnt/cnt,w_win_ret,w_place_ret,cnt])
        
#芝回収率
for i in range(len(ptret)):
    print(ptret[i])
    
#ダ回収率
#得点順にソート
w_d_ret = np.zeros([len(d_ret),len(d_ret[0])])
for i in range(len(d_ret)):
    w_d_ret[i] = d_ret[i]
po = np.argsort(w_d_ret[:,0])

#回収率チェック
pdret = []
for i in range(len(d_ret)):
    w_horse_num = po[i]
    tp = d_ret[w_horse_num][0]
    twr = d_ret[w_horse_num][1]
    tpr = d_ret[w_horse_num][2]
    if i == 0:
        mp = tp
        print("mp:",mp)
        w_win_ret = 0
        w_place_ret = 0
        cnt = 0
        win_cnt = 0
        place_cnt = 0
    if mp == tp:
        w_win_ret += twr
        w_place_ret += tpr
        cnt += 1
        if twr > 0:
            win_cnt += 1
        if tpr > 0:
            place_cnt += 1
    else:
        pdret.append([mp,(w_win_ret/cnt),(w_place_ret/cnt),(win_cnt/cnt),(place_cnt/cnt),w_win_ret,w_place_ret,cnt])
        mp = tp
        w_win_ret = twr
        w_place_ret = tpr
        cnt = 1
        if twr > 0:
            win_cnt = 1
        else :
            win_cnt = 0
        if tpr > 0:
            place_cnt = 1
        else :
            place_cnt = 0
    if i == len(d_ret) - 1:
        pdret.append([mp,w_win_ret/cnt,w_place_ret/cnt,win_cnt/cnt,place_cnt/cnt,w_win_ret,w_place_ret,cnt])
        
#ダート回収率
for i in range(len(pdret)):
    print(pdret[i])
