from ..sessioncontroll import baseobj,strobj,baseobj,intobj,colobj,fkyobj

class PredictData(baseobj):
    __tablename__ = 'predict'
    racehorsekey = colobj(strobj,fkyobj('racehorse.racehorsekey'),primary_key=True)
    pp_icchaku = colobj(intobj)
    rentai_rate = colobj(intobj)
    fukusho_rate = colobj(intobj)
    tansho_odds = colobj(intobj)
    fukusho_odds = colobj(intobj)

