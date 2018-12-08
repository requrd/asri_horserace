from ..sessioncontroll import baseobj,strobj,baseobj,intobj,colobj,relobj,fkyobj,bkrobj

class HorseIndex(baseobj):
    __tablename__ = 'horseindex'
    blood = colobj(intobj,fkyobj('racehorse.blood'),primary_key = True)
    index = colobj(intobj)

class JockeyIndex(baseobj):
    __tablename__ = 'jockeyindex'
    jockey_code = colobj(intobj,fkyobj('racehorse.jockey_code'),primary_key = True)
    index = colobj(intobj)

class TrainerIndex(baseobj):
    __tablename__ = 'trainerindex'
    trainer_code = colobj(intobj,fkyobj('racehorse.trainer_code'),primary_key = True)
    index = colobj(intobj)

class OikiriStateIndex(baseobj):
    __tablename__ = 'oikiristateindex'
    oikiri_state = colobj(intobj,fkyobj('train_oikiri.oikiri_state'),primary_key = True)
    index = colobj(intobj)

class TrainCourseCodeIndex(baseobj):
    __tablename__ = 'traincoursecodeindex'
    train_course_code = colobj(strobj,fkyobj('train_oikiri.train_course_code'),primary_key = True)
    index = colobj(intobj)

class HobokusakiIndex(baseobj):
    __tablename__ = 'hobokusakiindex'
    index = colobj(intobj,primary_key = True)
    hobokusaki = colobj(strobj,fkyobj('racehorse.hobokusaki'))

