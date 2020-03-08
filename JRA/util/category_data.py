import numpy as np
from jrdbdummies import CategoryGetter

def getCategoryData(kaisais):
    categories = _getCategories(kaisais)
    return _convertToMatrix(categories)
    
def _convertToMatrix(categories):
    matrix = np.zeros([len(categories), 18, len(categories[0][0])])
    for raceNum in range(len(categories)):
        for horseNum in range(len(categories[raceNum])):
            matrix[raceNum][horseNum] = categories[raceNum][horseNum]
    return matrix

def _getCategories(kaisais):
    categories = []
    for kaisai in kaisais:
        for race in kaisai.races:
            categories.append(_getRaceCategories(kaisai, race))
    return categories

def _getRaceCategories(kaisai, race):
    dummies = None
    for horse in race.racehorses:
        if horse.num == 1:
            dummies = _getCategory(kaisai, race, horse)
        else :
            dummies = np.vstack((dummies, _getCategory(kaisai, race, horse)))
    return dummies

def _getCategory(kaisai, race, horse):
    cg = CategoryGetter()
    return np.hstack((
        cg.getTennatsu(kaisai.tennatsu),
        cg.getDistance(race.distance),
        cg.getBacode(horse.bacode),
        cg.getNum(horse.num),
        cg.getWaku(horse.waku),
        cg.getTorikeshi(horse.torikeshi),
        cg.getBanushikaicode(horse.banushikai_code),
        cg.getTraintype(horse.trainanalysis.train_type)
    ))

