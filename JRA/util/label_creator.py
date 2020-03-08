import numpy as np

#ラベルデータ作成
t_icchaku = np.zeros([num_race,num_max_horse])
t_nichaku = np.zeros([num_race,num_max_horse])
t_sanchaku = np.zeros([num_race,num_max_horse])
t_yonchaku = np.zeros([num_race,num_max_horse])
t_gochaku = np.zeros([num_race,num_max_horse])

w_num = 0
for i in range(len(kaisais)):
    for j in range(len(kaisais[i].races)):
        w_race = kaisais[i].races[j]
        for k in range(len(w_race.racehorses)):
            w_horse = w_race.racehorses[k]
            oa = w_horse.result.order_of_arrival            
            if oa == 1:            
                t_icchaku[w_num,w_horse.num - 1] = 1
            elif oa == 2:
                t_nichaku[w_num,w_horse.num - 1] = 1
            elif oa == 3:
                t_sanchaku[w_num,w_horse.num - 1] = 1
            elif oa == 4:
                t_yonchaku[w_num,w_horse.num - 1] = 1
            elif oa == 5:
                t_gochaku[w_num,w_horse.num - 1] = 1        
        w_num += 1