from jrdbdummies import CategoryGetter
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

return category_data