from jrdbdummies import CategoryGetter
import numpy as np
import training_tool

def getCategoryData(kaisais):
    cg = CategoryGetter()
    cdw = []
    for kaisai in kaisais:
        for race in kaisai.races:
            for horse in race.racehorses:
                w_hdummies = np.zeros([0])
                
                #開催データ
                w_tennatsu = cg.getTennatsu(kaisai.tennatsu)
                
                #レースデータ
                w_distance = cg.getDistance(race.distance)
                
                #競走馬データ
                w_bacode = cg.getBacode(horse.bacode)
                w_num = cg.getNum(horse.num)            
                w_waku = cg.getWaku(horse.waku)            
                w_torikeshi = cg.getTorikeshi(horse.torikeshi)
                w_banushikai_code = cg.getBanushikaicode(horse.banushikai_code)
                w_train_type = cg.getTraintype(horse.trainanalysis.train_type)
                
                w_hdummies = np.hstack((
                        w_tennatsu,
                        w_distance,
                        w_bacode,
                        w_num,
                        w_torikeshi,
                        w_banushikai_code,
                        w_train_type
                        ))
                if horse.num - 1  == 0:
                    w_vdummies = w_hdummies
                else :
                    w_vdummies = np.vstack((w_vdummies,w_hdummies))
            cdw.append(w_vdummies)
    num_race = training_tool.numberOfRaces(kaisais)
    num_max_horse = 18
    category_data = np.zeros([num_race,num_max_horse,len(cdw[0][0])])

    for i in range(num_race):
        for j in range(len(cdw[i])):
            category_data[i][j] = cdw[i][j]

    return category_data