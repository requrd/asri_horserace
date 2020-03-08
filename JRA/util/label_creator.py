import numpy as np

#ラベルデータ作成
t_icchaku = np.zeros([num_race,num_max_horse])
t_nichaku = np.zeros([num_race,num_max_horse])
t_sanchaku = np.zeros([num_race,num_max_horse])
t_yonchaku = np.zeros([num_race,num_max_horse])
t_gochaku = np.zeros([num_race,num_max_horse])

w_num = 0
for kaisai in kaisais:
    for race in kaisai.races:
        for horse in race.racehorses:
            oa = horse.result.order_of_arrival            
            if oa == 1:            
                t_icchaku[w_num,horse.num - 1] = 1
            elif oa == 2:
                t_nichaku[w_num,horse.num - 1] = 1
            elif oa == 3:
                t_sanchaku[w_num,horse.num - 1] = 1
            elif oa == 4:
                t_yonchaku[w_num,horse.num - 1] = 1
            elif oa == 5:
                t_gochaku[w_num,horse.num - 1] = 1        
        w_num += 1