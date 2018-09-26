from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import numpy as np

Base = declarative_base()

class BangumiData(Base):
    __tablename__ = 'bangumi'
    racekey=Column(String,primary_key=True)
    #親に対して
    kaisaikey=Column(String,ForeignKey('kaisai.kaisaikey'))
    #子に対して
    racehorses = relationship("RacehorseData",backref='bangumi',lazy='subquery',innerjoin=True)
    racehorses_w = relationship("WorkTable",backref='bangumi')

    #1:1
    returninfo = relationship("ReturninfoData",uselist=False, backref= 'bangumi',lazy='joined',innerjoin=True)
    ymd=Column(String)
    start_time=Column(String)
    distance=Column(Integer)
    tdscode=Column(Integer)
    right_left=Column(Integer)
    in_out=Column(Integer)
    shubetsu=Column(Integer)
    joken=Column(String)
    kigo=Column(Integer)
    horse_kind_joken = Column(Integer)
    horse_sex_joken = Column(Integer)
    inter_race_joken = Column(Integer)
    juryo=Column(Integer)
    grade=Column(Integer)
    race_name=Column(String)
    kai=Column(String)
    num_of_all_horse=Column(Integer)
    course=Column(Integer)
    kaisai_kbn=Column(Integer)
    race_name_short=Column(String)
    race_name_9char=Column(String)
    data_kbn=Column(Integer)
    money1st=Column(Integer)
    money2nd=Column(Integer)
    money3rd=Column(Integer)
    money4th=Column(Integer)
    money5th=Column(Integer)
    sannyu_money1st=Column(Integer)
    sannyu_money2nd=Column(Integer)
    sellflg_tansho=Column(Integer)
    sellflg_fukusho=Column(Integer)
    sellflg_wakuren=Column(Integer)
    sellflg_umaren=Column(Integer)
    sellflg_umatan=Column(Integer)
    sellflg_wide=Column(Integer)
    sellflg_sanrenpuku=Column(Integer)
    sellflg_sanrentan=Column(Integer)
    yobi=Column(Integer)
    win5flg=Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racekey':self.racekey,
            'ymd':self.ymd,
            'start_time':self.start_time,
            'distance':self.distance,
            'tdscode':self.tdscode,
            'right_left':self.right_left,
            'in_out':self.in_out,
            'shubetsu':self.shubetsu,
            'joken':self.joken,
            'kigo':self.kigo,
            'horse_kind_joken':self.horse_kind_joken,
            'horse_sex_joken':horse_sex_joken,
            'inter_race_joken':inter_race_joken,
            'juryo':self.juryo,
            'grade':self.grade,
            'race_name':self.race_name,
            'kai':self.kai,
            'num_of_all_horse':self.num_of_all_horse,
            'course':self.course,
            'kaisai_kbn':self.kaisai_kbn,
            'race_name_short':self.race_name_short,
            'race_name_9char':self.race_name_9char,
            'data_kbn':self.data_kbn,
            'money1st':self.money1st,
            'money2nd':self.money2nd,
            'money3rd':self.money3rd,
            'money4th':self.money4th,
            'money5th':self.money5th,
            'sannyu_money1st':self.sannyu_money1st,
            'sannyu_money2nd':self.sannyu_money2nd,
            'sellflg_tansho':self.sellflg_tansho,
            'sellflg_fukusho':self.sellflg_fukusho,
            'sellflg_wakuren':self.sellflg_wakuren,
            'sellflg_umaren':self.sellflg_umaren,
            'sellflg_umatan':self.sellflg_umatan,
            'sellflg_wide':self.sellflg_wide,
            'sellflg_sanrenpuku':self.sellflg_sanrenpuku,
            'sellflg_sanrentan':self.sellflg_sanrentan,
            'yobi':self.yobi,
            'win5flg':self.win5flg
        }

class RacehorseData(Base):
    __tablename__ = 'racehorse'
    racehorsekey = Column(String,ForeignKey('seiseki.racehorsekey'),primary_key=True)
    #親に対して
    racekey = Column(String,ForeignKey('bangumi.racekey'))
    #1:1
    trainanalysis = relationship("TrainAnalysisData",uselist=False, backref="racehorse",lazy='joined',innerjoin=True)
    trainoikiri = relationship("TrainOikiriData",uselist=False, backref="racehorse",lazy='joined',innerjoin=True)
    horse_base = relationship("HorsebaseData",uselist=False,backref="racehorse",lazy='joined',innerjoin=True)
    result = relationship("SeisekiData",uselist=False,foreign_keys=[racehorsekey],lazy='joined',innerjoin=False)
    #インデックスに対して
    horseidx = relationship("HorseIndex",uselist=False,backref="racehorse")
    jockeyidx = relationship("JockeyIndex",uselist=False,backref="racehorse")
    traineridx = relationship("TrainerIndex",uselist=False,backref="racehorse")
    hobokusakiidx = relationship("HobokusakiIndex",uselist=False,backref="racehorse")
    bacode = Column(Integer)
    year = Column(Integer)
    kai = Column(Integer)
    day = Column(Integer)
    race = Column(Integer)
    num=Column(Integer)
    blood=Column(Integer)
    horse=Column(String)
    idm=Column(Integer)
    jockey_score=Column(Integer)
    info_score=Column(Integer)
    yobi1=Column(String)
    yobi2=Column(String)
    yobi3=Column(String)
    sogo_score=Column(Integer)
    leg_type=Column(Integer)
    distance_adjust=Column(Integer)
    up_degree=Column(Integer)
    routin=Column(Integer)
    cri_odds=Column(Integer)
    cri_popular_order=Column(Integer)
    cri_fukusho_odds=Column(Integer)
    cri_fukusho_popluar_order=Column(Integer)
    specific_info_1=Column(Integer)
    specific_info_2=Column(Integer)
    specific_info_3=Column(Integer)
    specific_info_4=Column(Integer)
    specific_info_5=Column(Integer)
    sogo_info_1=Column(Integer)
    sogo_info_2=Column(Integer)
    sogo_info_3=Column(Integer)
    sogo_info_4=Column(Integer)
    sogo_info_5=Column(Integer)
    pop_score=Column(Integer)
    train_score=Column(Integer)
    trainer_score=Column(Integer)
    train_code=Column(Integer)
    trainer_hyoka_code=Column(Integer)
    jockey_rate_rentai=Column(Integer)
    gekiso_score=Column(Integer)
    hidume_code=Column(Integer)
    hidume_shape=Column(Integer)
    hidume_size=Column(Integer)
    omotekisei_code=Column(Integer)
    class_code=Column(Integer)
    yobi4=Column(String)
    brinkers=Column(String)
    jockey_name=Column(String)
    kinryo=Column(Integer)
    minarai=Column(Integer)
    trainer_name=Column(String)
    trainer_shozoku=Column(String)
    zenso_seiseki_key_1=Column(String,ForeignKey('seiseki.raceseisekikey'))
    zenso_seiseki_key_2=Column(String,ForeignKey('seiseki.raceseisekikey'))
    zenso_seiseki_key_3=Column(String,ForeignKey('seiseki.raceseisekikey'))
    zenso_seiseki_key_4=Column(String,ForeignKey('seiseki.raceseisekikey'))
    zenso_seiseki_key_5=Column(String,ForeignKey('seiseki.raceseisekikey'))
    zenso1 = relationship("SeisekiData",uselist=False,foreign_keys=[zenso_seiseki_key_1],lazy='joined',innerjoin = False)
    zenso2 = relationship("SeisekiData",uselist=False,foreign_keys=[zenso_seiseki_key_2],lazy='joined',innerjoin = False)
    zenso3 = relationship("SeisekiData",uselist=False,foreign_keys=[zenso_seiseki_key_3],lazy='joined',innerjoin = False)
    zenso4 = relationship("SeisekiData",uselist=False,foreign_keys=[zenso_seiseki_key_4],lazy='joined',innerjoin = False)
    zenso5 = relationship("SeisekiData",uselist=False,foreign_keys=[zenso_seiseki_key_5],lazy='joined',innerjoin = False)
    zenso_racekey_1=Column(String)
    zenso_racekey_2=Column(String)
    zenso_racekey_3=Column(String)
    zenso_racekey_4=Column(String)
    zenso_racekey_5=Column(String)
    waku=Column(Integer)
    yobi5=Column(String)
    sogo_shirushi=Column(Integer)
    idm_shiruishi=Column(Integer)
    info_shirushi=Column(Integer)
    jockey_shirushi=Column(Integer)
    trainer_shirushi=Column(Integer)
    train_shirushi=Column(Integer)
    gekiso_shirushi=Column(Integer)
    turf_adjust_code=Column(Integer)
    dart_adjust_code=Column(Integer)
    jockey_code=Column(Integer)
    trainer_code=Column(Integer)
    yobi6=Column(String)
    kakutoku_money=Column(Integer)
    shukaku_money=Column(Integer)
    joken=Column(Integer)
    ten_score=Column(Integer)
    pace_score=Column(Integer)
    up_score=Column(Integer)
    position_score=Column(Integer)
    pace_predict=Column(String)
    dochu_order=Column(Integer)
    dochu_sa=Column(Integer)
    dochu_in_out=Column(Integer)
    last_order=Column(Integer)
    last_sa=Column(Integer)
    last_in_out=Column(Integer)
    order=Column(Integer)
    sa=Column(Integer)
    in_out=Column(Integer)
    tenkai=Column(String)
    distance_adjust2=Column(Integer)
    commit_weight=Column(Integer)
    commit_weight_increase=Column(Integer)
    torikeshi=Column(Integer)
    sex=Column(Integer)
    owner_name=Column(String)
    banushikai_code=Column(Integer)
    umakigo_code=Column(Integer)
    gekiso_order=Column(Integer)
    ls_score_order=Column(Integer)
    ten_score_order=Column(Integer)
    pace_score_order=Column(Integer)
    up_score_order=Column(Integer)
    position_score_order=Column(Integer)
    expect_jokey_win_rate=Column(Integer)
    expect_jokey_rentai_rate=Column(Integer)
    yuso=Column(String)
    soho=Column(Integer)
    taikei_data=Column(String)
    taikei=Column(Integer)
    senaka = Column(Integer)
    do = Column(Integer)
    siri = Column(Integer)
    tomo = Column(Integer)
    harabukuro = Column(Integer)
    head = Column(Integer)
    neck = Column(Integer)
    breast = Column(Integer)
    shoulder = Column(Integer)
    zencho = Column(Integer)
    kocho = Column(Integer)
    maehaba = Column(Integer)
    ushirohaba = Column(Integer)
    maetsunagi = Column(Integer)
    ushirotsunagi = Column(Integer)
    tail = Column(Integer)
    furikata = Column(Integer)
    taikei_sogo1=Column(Integer)
    taikei_sogo2=Column(Integer)
    taikei_sogo3=Column(Integer)
    umatokki1=Column(Integer)
    umatokki2=Column(Integer)
    umatokki3=Column(Integer)
    horse_start_score=Column(Integer)
    horse_latestart_rate=Column(Integer)
    sanko_zenso=Column(Integer)
    sanko_zenso_jockey_code=Column(String)
    mambaken_score=Column(Integer)
    mambaken_shirushi=Column(Integer)
    kokyu_flg=Column(Integer)
    gekiso_type=Column(String)
    rest_reason_code=Column(Integer)
    flg=Column(String)
    turf_dart_steeple_flg=Column(Integer)
    distance_flg=Column(Integer)
    class_flg=Column(Integer)
    tenkyu_flg=Column(Integer)
    kyosei_flg=Column(Integer)
    norikae_flg=Column(Integer)
    runtimes_first_train=Column(Integer)
    date_first_train=Column(Integer)
    days_after_first_train=Column(Integer)
    hobokusaki=Column(String)
    hobokusaki_rank=Column(String)
    trainer_rank=Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racehorsekey': self.racehorsekey,
            'racekey': self.racekey,
            'bacode': self.bacode,
            'year': self.year,
            'kai': self.kai,
            'day': self.day,
            'race': self.race,
            'num':self.num,
            'blood':self.blood,
            'horse':self.horse,
            'idm':self.idm,
            'jockey_score':self.jockey_score,
            'info_score':self.info_score,
            'yobi1':self.yobi1,
            'yobi2':self.yobi2,
            'yobi3':self.yobi3,
            'sogo_score':self.sogo_score,
            'leg_type':self.leg_type,
            'distance_adjust':self.distance_adjust,
            'up_degree':self.up_degree,
            'routin':self.routin,
            'cri_odds':self.cri_odds,
            'cri_popular_order':self.cri_popular_order,
            'cri_fukusho_odds':self.cri_fukusho_odds,
            'cri_fukusho_popluar_order':self.cri_fukusho_popluar_order,
            'specific_info_1':self.specific_info_1,
            'specific_info_2':self.specific_info_2,
            'specific_info_3':self.specific_info_3,
            'specific_info_4':self.specific_info_4,
            'specific_info_5':self.specific_info_5,
            'sogo_info_1':self.sogo_info_1,
            'sogo_info_2':self.sogo_info_2,
            'sogo_info_3':self.sogo_info_3,
            'sogo_info_4':self.sogo_info_4,
            'sogo_info_5':self.sogo_info_5,
            'pop_score':self.pop_score,
            'train_score':self.train_score,
            'trainer_score':self.trainer_score,
            'train_code':self.train_code,
            'trainer_hyoka_code':self.trainer_hyoka_code,
            'jockey_rate_rentai':self.jockey_rate_rentai,
            'gekiso_score':self.gekiso_score,
            'hidume_code':self.hidume_code,
            'hidume_shape':self.hidume_shape,
            'hidume_size':self.hidume_size,
            'omotekisei_code':self.omotekisei_code,
            'class_code':self.class_code,
            'yobi4':self.yobi4,
            'brinkers':self.brinkers,
            'jockey_name':self.jockey_name,
            'kinryo':self.kinryo,
            'minarai':self.minarai,
            'trainer_name':self.trainer_name,
            'trainer_shozoku':self.trainer_shozoku,
            'zenso_seiseki_key_1':self.zenso_seiseki_key_1,
            'zenso_seiseki_key_2':self.zenso_seiseki_key_2,
            'zenso_seiseki_key_3':self.zenso_seiseki_key_3,
            'zenso_seiseki_key_4':self.zenso_seiseki_key_4,
            'zenso_seiseki_key_5':self.zenso_seiseki_key_5,
            'zenso_racekey_1':self.zenso_racekey_1,
            'zenso_racekey_2':self.zenso_racekey_2,
            'zenso_racekey_3':self.zenso_racekey_3,
            'zenso_racekey_4':self.zenso_racekey_4,
            'zenso_racekey_5':self.zenso_racekey_5,
            'waku':self.waku,
            'yobi5':self.yobi5,
            'sogo_shirushi':self.sogo_shirushi,
            'idm_shiruishi':self.idm_shiruishi,
            'info_shirushi':self.info_shirushi,
            'jockey_shirushi':self.jockey_shirushi,
            'trainer_shirushi':self.trainer_shirushi,
            'train_shirushi':self.train_shirushi,
            'gekiso_shirushi':self.gekiso_shirushi,
            'turf_adjust_code':self.turf_adjust_code,
            'dart_adjust_code':self.dart_adjust_code,
            'jockey_code':self.jockey_code,
            'trainer_code':self.trainer_code,
            'yobi6':self.yobi6,
            'kakutoku_money':self.kakutoku_money,
            'shukaku_money':self.shukaku_money,
            'joken':self.joken,
            'ten_score':self.ten_score,
            'pace_score':self.pace_score,
            'up_score':self.up_score,
            'position_score':self.position_score,
            'pace_predict':self.pace_predict,
            'dochu_order':self.dochu_order,
            'dochu_sa':self.dochu_sa,
            'dochu_in_out':self.dochu_in_out,
            'last_order':self.last_order,
            'last_sa':self.last_sa,
            'last_in_out':self.last_in_out,
            'order':self.order,
            'sa':self.sa,
            'in_out':self.in_out,
            'tenkai':self.tenkai,
            'distance_adjust2':self.distance_adjust2,
            'commit_weight':self.commit_weight,
            'commit_weight_increase':self.commit_weight_increase,
            'torikeshi':self.torikeshi,
            'sex':self.sex,
            'owner_name':self.owner_name,
            'banushikai_code':self.banushikai_code,
            'umakigo_code':self.umakigo_code,
            'gekiso_order':self.gekiso_order,
            'ls_score_order':self.ls_score_order,
            'ten_score_order':self.ten_score_order,
            'pace_score_order':self.pace_score_order,
            'up_score_order':self.up_score_order,
            'position_score_order':self.position_score_order,
            'expect_jokey_win_rate':self.expect_jokey_win_rate,
            'expect_jokey_rentai_rate':self.expect_jokey_rentai_rate,
            'yuso':self.yuso,
            'soho':self.soho,
            'taikei_data':self.taikei_data,
            'taikei':self.taikei,
            'senaka':self.senaka,
            'do':self.do,
            'siri':self.siri,
            'tomo':self.tomo,
            'harabukuro':self.harabukuro,
            'head':self.head,
            'neck':self.neck,
            'breast':self.breast,
            'shoulder':self.shoulder,
            'zencho':self.zencho,
            'kocho':self.kocho,
            'maehaba':self.maehaba,
            'ushirohaba':self.ushirohaba,
            'maetsunagi':self.maetsunagi,
            'ushirotsunagi':self.ushirotsunagi,
            'tail':self.tail,
            'furikata':self.furikata,
            'umatokki1':self.umatokki1,
            'umatokki2':self.umatokki2,
            'umatokki3':self.umatokki3,
            'horse_start_score':self.horse_start_score,
            'horse_latestart_rate':self.horse_latestart_rate,
            'sanko_zenso':self.sanko_zenso,
            'sanko_zenso_jockey_code':self.sanko_zenso_jockey_code,
            'mambaken_score':self.mambaken_score,
            'mambaken_shirushi':self.mambaken_shirushi,
            'kokyu_flg':self.kokyu_flg,
            'gekiso_type':self.gekiso_type,
            'rest_reason_code':self.rest_reason_code,
            'flg':self.flg,
            'turf_dart_steeple_flg':self.turf_dart_steeple_flg,
            'distance_flg':self.distance_flg,
            'class_flg':self.class_flg,
            'tenkyu_flg':self.tenkyu_flg,
            'kyosei_flg':self.kyosei_flg,
            'norikae_flg':self.norikae_flg,
            'runtimes_first_train':self.runtimes_first_train,
            'date_first_train':self.date_first_train,
            'days_after_first_train':self.days_after_first_train,
            'hobokusaki':self.hobokusaki,
            'hobokusaki_rank':self.hobokusaki_rank,
            'trainer_rank':self.trainer_rank
        }

class SeisekiData(Base):
    __tablename__ = 'seiseki'
    racehorsekey=Column(String,primary_key=True)
    racekey=Column(String)
    bacode=Column(Integer)
    year=Column(Integer)
    kai=Column(Integer)
    day=Column(Integer)
    raceno=Column(Integer)
    seisekirace = relationship("SeisekiRaceData", uselist=False, backref="seiseki")
    num=Column(Integer)
    raceseisekikey=Column(String)
    blood=Column(Integer)
    ymd=Column(String)
    horse=Column(String)
    distance=Column(Integer)
    tdscode=Column(Integer)
    right_left=Column(Integer)
    in_out=Column(Integer)
    baba=Column(Integer)
    baba_abst=Column(Integer)
    baba_detail=Column(Integer)
    shubetsu=Column(Integer)
    joken=Column(String)
    kigo=Column(Integer)
    juryo=Column(Integer)
    grade=Column(Integer)
    racename=Column(String)
    num_of_all_horse=Column(Integer)
    racename_ryaku=Column(String)
    order_of_arrival=Column(Integer)
    ijo_kbn=Column(Integer)
    time=Column(Integer)
    kinryo=Column(Integer)
    jockey_name=Column(String)
    trainer_name=Column(String)
    decided_odds=Column(Integer)
    decided_pop_order=Column(Integer)
    idm=Column(Integer)
    natural_score=Column(Integer)
    baba_sa=Column(Integer)
    pace=Column(Integer)
    start_late=Column(Integer)
    position=Column(Integer)
    furi=Column(Integer)
    mae_furi=Column(Integer)
    naka_furi=Column(Integer)
    ushiro_furi=Column(Integer)
    race=Column(Integer)
    course_position=Column(Integer)
    up_code=Column(Integer)
    class_code=Column(Integer)
    batai_code=Column(Integer)
    kehai_code=Column(Integer)
    racepace=Column(String)
    umapace=Column(String)
    ten_score=Column(Integer)
    up_score=Column(Integer)
    pace_score=Column(Integer)
    racep_score=Column(Integer)
    win_horse_name=Column(String)
    time_sa=Column(Integer)
    mae3f_time=Column(Integer)
    agari3f_time=Column(Integer)
    biko=Column(String)
    yobi=Column(String)
    decided_place_odds=Column(Integer)
    juji_win_odds=Column(Integer)
    juji_place_odds=Column(Integer)
    corner_order1=Column(Integer)
    corner_order2=Column(Integer)
    corner_order3=Column(Integer)
    corner_order4=Column(Integer)
    mae3f_sa=Column(Integer)
    agari3f_sa=Column(Integer)
    jockey_code=Column(Integer)
    trainer_code=Column(Integer)
    weight=Column(Integer)
    weight_increase=Column(Integer)
    tenko=Column(Integer)
    course=Column(Integer)
    race_leg_type=Column(String)
    win_ret=Column(Integer)
    place_ret=Column(Integer)
    this_money=Column(Integer)
    earned_money=Column(Integer)
    race_pace_flow=Column(Integer)
    horse_pace_flow=Column(Integer)
    corner4_course_position=Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racehorsekey': self.racehorsekey,
            'racekey': self.racekey,
            'bacode':self.bacode,
            'year':self.year,
            'kai':self.kai,
            'day':self.day,
            'raceno':self.raceno,
            'num':self.num,
            'raceseisekikey':self.raceseisekikey,
            'blood':self.blood,
            'ymd':self.ymd,
            'horse':self.horse,
            'distance':self.distance,
            'tdscode':self.tdscode,
            'right_left':self.right_left,
            'in_out':self.in_out,
            'baba':self.baba,
            'baba_abst':self.baba_abst,
            'baba_detail':self.baba_detail,
            'shubetsu':self.shubetsu,
            'joken':self.joken,
            'kigo':self.kigo,
            'juryo':self.juryo,
            'grade':self.grade,
            'racename':self.racename,
            'num_of_all_horse':self.num_of_all_horse,
            'racename_ryaku':self.racename_ryaku,
            'order_of_arrival':self.order_of_arrival,
            'ijo_kbn':self.ijo_kbn,
            'time':self.time,
            'kinryo':self.kinryo,
            'jockey_name':self.jockey_name,
            'trainer_name':self.trainer_name,
            'decided_odds':self.decided_odds,
            'decided_pop_order':self.decided_pop_order,
            'idm':self.idm,
            'natural_score':self.natural_score,
            'baba_sa':self.baba_sa,
            'pace':self.pace,
            'start_late':self.start_late,
            'position':self.position,
            'furi':self.furi,
            'mae_furi':self.mae_furi,
            'naka_furi':self.naka_furi,
            'ushiro_furi':self.ushiro_furi,
            'race':self.race,
            'course_position':self.course_position,
            'up_code':self.up_code,
            'class_code':self.class_code,
            'batai_code':self.batai_code,
            'kehai_code':self.kehai_code,
            'racepace':self.racepace,
            'umapace':self.umapace,
            'ten_score':self.ten_score,
            'up_score':self.up_score,
            'pace_score':self.pace_score,
            'racep_score':self.racep_score,
            'win_horse_name':self.win_horse_name,
            'time_sa':self.time_sa,
            'mae3f_time':self.mae3f_time,
            'agari3f_time':self.agari3f_time,
            'biko':self.biko,
            'yobi':self.yobi,
            'decided_place_odds':self.decided_place_odds,
            'juji_win_odds':self.juji_win_odds,
            'juji_place_odds':self.juji_place_odds,
            'corner_order1':self.corner_order1,
            'corner_order2':self.corner_order2,
            'corner_order3':self.corner_order3,
            'corner_order4':self.corner_order4,
            'mae3f_sa':self.mae3f_sa,
            'agari3f_sa':self.agari3f_sa,
            'jockey_code':self.jockey_code,
            'trainer_code':self.trainer_code,
            'weight':self.weight,
            'weight_increase':self.weight_increase,
            'tenko':self.tenko,
            'course':self.course,
            'race_leg_type':self.race_leg_type,
            'win_ret':self.win_ret,
            'place_ret':self.place_ret,
            'this_money':self.this_money,
            'earned_money':self.earned_money,
            'race_pace_flow':self.race_pace_flow,
            'horse_pace_flow':self.horse_pace_flow,
            'corner4_course_position':self.corner4_course_position
        }

class SeisekiRaceData(Base):
    __tablename__ = 'seisekirace'
    racekey=Column(String,ForeignKey('seiseki.racekey'),primary_key=True)
    furlongtime1=Column(Integer)
    furlongtime2=Column(Integer)
    furlongtime3=Column(Integer)
    furlongtime4=Column(Integer)
    furlongtime5=Column(Integer)
    furlongtime6=Column(Integer)
    furlongtime7=Column(Integer)
    furlongtime8=Column(Integer)
    furlongtime9=Column(Integer)
    furlongtime10=Column(Integer)
    furlongtime11=Column(Integer)
    furlongtime12=Column(Integer)
    furlongtime13=Column(Integer)
    furlongtime14=Column(Integer)
    furlongtime15=Column(Integer)
    furlongtime16=Column(Integer)
    furlongtime17=Column(Integer)
    furlongtime18=Column(Integer)
    corner1=Column(String)
    corner2=Column(String)
    corner3=Column(String)
    corner4=Column(String)
    paceupposition=Column(Integer)
    truckbias1_in=Column(String)
    truckbias1_center=Column(String)
    truckbias1_out=Column(String)
    truckbias2_in=Column(String)
    truckbias2_center=Column(String)
    truckbias2_out=Column(String)
    truckbias_muko_in=Column(String)
    truckbias_muko_center=Column(String)
    truckbias_muko_out=Column(String)
    truckbias3_in=Column(String)
    truckbias3_center=Column(String)
    truckbias3_out=Column(String)
    truckbias4_saiuchi=Column(String)
    truckbias4_in=Column(String)
    truckbias4_center=Column(String)
    truckbias4_out=Column(String)
    truckbias4_oosoto=Column(String)
    truckbias_straight_saiuchi=Column(String)
    truckbias_straight_in=Column(String)
    truckbias_straight_center=Column(String)
    truckbias_straight_out=Column(String)
    truckbias_straight_oosoto=Column(String)
    comment=Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racekey': self.racekey,
            'furlongtime1':self.furlongtime1,
            'furlongtime2':self.furlongtime2,
            'furlongtime3':self.furlongtime3,
            'furlongtime4':self.furlongtime4,
            'furlongtime5':self.furlongtime5,
            'furlongtime6':self.furlongtime6,
            'furlongtime7':self.furlongtime7,
            'furlongtime8':self.furlongtime8,
            'furlongtime9':self.furlongtime9,
            'furlongtime10':self.furlongtime10,
            'furlongtime11':self.furlongtime11,
            'furlongtime12':self.furlongtime12,
            'furlongtime13':self.furlongtime13,
            'furlongtime14':self.furlongtime14,
            'furlongtime15':self.furlongtime15,
            'furlongtime16':self.furlongtime16,
            'furlongtime17':self.furlongtime17,
            'furlongtime18':self.furlongtime18,
            'corner1':self.corner1,
            'corner2':self.corner2,
            'corner3':self.corner3,
            'corner4':self.corner4,
            'paceupposition':self.paceupposition,
            'truckbias1_in':self.truckbias1_in,
            'truckbias1_center':self.truckbias1_center,
            'truckbias1_out':self.truckbias1_out,
            'truckbias2_in':self.truckbias2_in,
            'truckbias2_center':self.truckbias2_center,
            'truckbias2_out':self.truckbias2_out,
            'truckbias_muko_in':self.truckbias_muko_in,
            'truckbias_muko_center':self.truckbias_muko_center,
            'truckbias_muko_out':self.truckbias_muko_out,
            'truckbias3_in':self.truckbias3_in,
            'truckbias3_center':self.truckbias3_center,
            'truckbias3_out':self.truckbias3_out,
            'truckbias4_saiuchi':self.truckbias4_saiuchi,
            'truckbias4_in':self.truckbias4_in,
            'truckbias4_center':self.truckbias4_center,
            'truckbias4_out':self.truckbias4_out,
            'truckbias4_oosoto':self.truckbias4_oosoto,
            'truckbias_straight_saiuchi':self.truckbias_straight_saiuchi,
            'truckbias_straight_in':self.truckbias_straight_in,
            'truckbias_straight_center':self.truckbias_straight_center,
            'truckbias_straight_out':self.truckbias_straight_out,
            'truckbias_straight_oosoto':self.truckbias_straight_oosoto,
            'comment':self.comment,
        }

class KaisaiData(Base):
    __tablename__ = 'kaisai'
    kaisaikey=Column(String,primary_key=True)
    #子に対して
    races = relationship("BangumiData",backref="kaisai",lazy='subquery',innerjoin=True)
    ymd=Column(Integer)
    kaisai_kbn=Column(Integer)
    day_of_week=Column(String)
    course_name=Column(String)
    tenko=Column(Integer,ForeignKey('tenkomaster.tenko'))
    turf_baba=Column(Integer)
    turf_baba_abst=Column(Integer)
    turf_baba_detail=Column(Integer)
    turf_baba_in=Column(Integer)
    turf_baba_center=Column(Integer)
    turf_baba_out=Column(Integer)
    turf_baba_sa=Column(Integer)
    turf_baba_straight_saiuchi=Column(Integer)
    turf_baba_straight_in=Column(Integer)
    turf_baba_straight_center=Column(Integer)
    turf_baba_straight_out=Column(Integer)
    turf_baba_straight_oosoto=Column(Integer)
    dart_baba=Column(Integer)
    dart_baba_abst=Column(Integer)
    dart_baba_detail=Column(Integer)
    dart_baba_in=Column(Integer)
    dart_baba_center=Column(Integer)
    dart_baba_out=Column(Integer)
    dart_baba_sa=Column(Integer)
    data_kbn=Column(Integer)
    renzoku_day=Column(Integer)
    turf_kind=Column(Integer)
    turf_length=Column(Integer)
    tennatsu=Column(Integer)
    stopfreeze=Column(Integer)
    precipitation=Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'kaisaikey': self.kaisaikey,
            'ymd':self.ymd,
            'kaisai_kbn':self.kaisai_kbn,
            'day_of_week':self.day_of_week,
            'course_name':self.course_name,
            'tenko':self.tenko,
            'turf_baba':self.turf_baba,
            'turf_baba_abst':self.turf_baba_abst,
            'turf_baba_detail':self.turf_baba_detail,
            'turf_baba_in':self.turf_baba_in,
            'turf_baba_center':self.turf_baba_center,
            'turf_baba_out':self.turf_baba_out,
            'turf_baba_sa':self.turf_baba_sa,
            'turf_baba_straight_saiuchi':self.turf_baba_straight_saiuchi,
            'turf_baba_straight_in':self.turf_baba_straight_in,
            'turf_baba_straight_center':self.turf_baba_straight_center,
            'turf_baba_straight_out':self.turf_baba_straight_out,
            'turf_baba_straight_oosoto':self.turf_baba_straight_oosoto,
            'dart_baba':self.dart_baba,
            'dart_baba_abst':self.dart_baba_abst,
            'dart_baba_detail':self.dart_baba_detail,
            'dart_baba_in':self.dart_baba_in,
            'dart_baba_center':self.dart_baba_center,
            'dart_baba_out':self.dart_baba_out,
            'dart_baba_sa':self.dart_baba_sa,
            'data_kbn':self.data_kbn,
            'renzoku_day':self.renzoku_day,
            'turf_kind':self.turf_kind,
            'turf_length':self.turf_length,
            'tennatsu':self.tennatsu,
            'stopfreeze':self.stopfreeze,
            'precipitation':self.precipitation
        }

class TrainAnalysisData(Base):
    __tablename__ = 'train_analysis'
    racehorsekey=Column(String,ForeignKey('racehorse.racehorsekey'),primary_key=True)
    racekey=Column(String)
    num=Column(Integer)
    train_type=Column(String)
    train_course_kind=Column(String)
    saka=Column(Integer)
    wood=Column(Integer)
    dart=Column(Integer)
    turf=Column(Integer)
    pool=Column(Integer)
    steeple=Column(Integer)
    politruck=Column(Integer)
    train_distance=Column(Integer)
    train_juten=Column(Integer)
    oikiri_score=Column(Integer)
    shiage_score=Column(Integer)
    train_vol_hyoka=Column(String)
    shiage_score_change=Column(Integer)
    train_comment=Column(String)
    comment_date=Column(String)
    train_hyoka=Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racehorsekey':self.racehorsekey,
            'racekey':self.racekey,
            'num':self.num,
            'train_type':self.train_type,
            'train_course_kind':self.train_course_kind,
            'saka':self.saka,
            'wood':self.wood,
            'dart':self.dart,
            'turf':self.turf,
            'pool':self.pool,
            'steeple':self.steeple,
            'politruck':self.politruck,
            'train_distance':self.train_distance,
            'train_juten':self.train_juten,
            'oikiri_score':self.oikiri_score,
            'shiage_score':self.shiage_score,
            'train_vol_hyoka':self.train_vol_hyoka,
            'shiage_score_change':self.shiage_score_change,
            'train_comment':self.train_comment,
            'comment_date':self.comment_date,
            'train_hyoka':self.train_hyoka
        }

class TrainOikiriData(Base):
    __tablename__ = 'train_oikiri'
    racehorsekey=Column(String,ForeignKey('racehorse.racehorsekey'),primary_key=True)
    racekey=Column(String)
    num=Column(Integer)
    oikiristateidx = relationship("OikiriStateIndex",uselist=False,backref="train_oikiri")
    traincoureidx = relationship("TrainCourseCodeIndex",uselist=False,backref="train_oikri")
    day_of_week=Column(String)
    train_date=Column(String)
    kaisu=Column(Integer)
    train_course_code=Column(String)
    oikiri_kind=Column(Integer)
    oikiri_state=Column(Integer)
    rider=Column(Integer)
    train_f=Column(Integer)
    ten_f=Column(Integer)
    mid_f=Column(Integer)
    end_f=Column(Integer)
    ten_f_score=Column(Integer)
    mid_f_score=Column(Integer)
    end_f_score=Column(Integer)
    oikiri_score=Column(Integer)
    awase_result=Column(String)
    aite_oikiri_kind=Column(Integer)
    aite_age=Column(Integer)
    aite_class=Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racehorsekey':self.racehorsekey,
            'racekey':self.racekey,
            'num':self.num,
            'day_of_week':self.day_of_week,
            'train_date':self.train_date,
            'kaisu':self.kaisu,
            'train_course_code':self.train_course_code,
            'oikiri_kind':self.oikiri_kind,
            'oikiri_state':self.oikiri_state,
            'rider':self.rider,
            'train_f':self.train_f,
            'ten_f':self.ten_f,
            'mid_f':self.mid_f,
            'end_f':self.end_f,
            'ten_f_score':self.ten_f_score,
            'mid_f_score':self.mid_f_score,
            'end_f_score':self.end_f_score,
            'oikiri_score':self.oikiri_score,
            'awase_result':self.awase_result,
            'aite_oikiri_kind':self.aite_oikiri_kind,
            'aite_age':self.aite_age,
            'aite_class':self.aite_class
        }

class ReturninfoData(Base):
    __tablename__ = 'returninfo'
    racekey=Column(String,ForeignKey('bangumi.racekey'),primary_key=True)
    win1_num=Column(Integer)
    win1_ret=Column(Integer)
    win2_num=Column(Integer)
    win2_ret=Column(Integer)
    win3_num=Column(Integer)
    win3_ret=Column(Integer)
    place1_num=Column(Integer)
    place1_ret=Column(Integer)
    place2_num=Column(Integer)
    place2_ret=Column(Integer)
    place3_num=Column(Integer)
    place3_ret=Column(Integer)
    place4_num=Column(Integer)
    place4_ret=Column(Integer)
    place5_num=Column(Integer)
    place5_ret=Column(Integer)
    wakuren1_num1=Column(Integer)
    wakuren1_num2=Column(Integer)
    wakuren1_ret=Column(Integer)
    wakuren2_num1=Column(Integer)
    wakuren2_num2=Column(Integer)
    wakuren2_ret=Column(Integer)
    wakuren3_num1=Column(Integer)
    wakuren3_num2=Column(Integer)
    wakuren3_ret=Column(Integer)
    umaren1_num1=Column(Integer)
    umaren1_num2=Column(Integer)
    umaren1_ret=Column(Integer)
    umaren2_num1=Column(Integer)
    umaren2_num2=Column(Integer)
    umaren2_ret=Column(Integer)
    umaren3_num1=Column(Integer)
    umaren3_num2=Column(Integer)
    umaren3_ret=Column(Integer)
    wide1_num1=Column(Integer)
    wide1_num2=Column(Integer)
    wide1_ret=Column(Integer)
    wide2_num1=Column(Integer)
    wide2_num2=Column(Integer)
    wide2_ret=Column(Integer)
    wide3_num1=Column(Integer)
    wide3_num2=Column(Integer)
    wide3_ret=Column(Integer)
    wide4_num1=Column(Integer)
    wide4_num2=Column(Integer)
    wide4_ret=Column(Integer)
    wide5_num1=Column(Integer)
    wide5_num2=Column(Integer)
    wide5_ret=Column(Integer)
    wide6_num1=Column(Integer)
    wide6_num2=Column(Integer)
    wide6_ret=Column(Integer)
    wide7_num1=Column(Integer)
    wide7_num2=Column(Integer)
    wide7_ret=Column(Integer)
    umatan1_num1=Column(Integer)
    umatan1_num2=Column(Integer)
    umatan1_ret=Column(Integer)
    umatan2_num1=Column(Integer)
    umatan2_num2=Column(Integer)
    umatan2_ret=Column(Integer)
    umatan3_num1=Column(Integer)
    umatan3_num2=Column(Integer)
    umatan3_ret=Column(Integer)
    umatan4_num1=Column(Integer)
    umatan4_num2=Column(Integer)
    umatan4_ret=Column(Integer)
    umatan5_num1=Column(Integer)
    umatan5_num2=Column(Integer)
    umatan5_ret=Column(Integer)
    umatan6_num1=Column(Integer)
    umatan6_num2=Column(Integer)
    umatan6_ret=Column(Integer)
    sanrenpuku1_num1=Column(Integer)
    sanrenpuku1_num2=Column(Integer)
    sanrenpuku1_num3=Column(Integer)
    sanrenpuku1_ret=Column(Integer)
    sanrenpuku2_num1=Column(Integer)
    sanrenpuku2_num2=Column(Integer)
    sanrenpuku2_num3=Column(Integer)
    sanrenpuku2_ret=Column(Integer)
    sanrenpuku3_num1=Column(Integer)
    sanrenpuku3_num2=Column(Integer)
    sanrenpuku3_num3=Column(Integer)
    sanrenpuku3_ret=Column(Integer)
    sanrentan1_num1=Column(Integer)
    sanrentan1_num2=Column(Integer)
    sanrentan1_num3=Column(Integer)
    sanrentan1_ret=Column(Integer)
    sanrentan2_num1=Column(Integer)
    sanrentan2_num2=Column(Integer)
    sanrentan2_num3=Column(Integer)
    sanrentan2_ret=Column(Integer)
    sanrentan3_num1=Column(Integer)
    sanrentan3_num2=Column(Integer)
    sanrentan3_num3=Column(Integer)
    sanrentan3_ret=Column(Integer)
    sanrentan4_num1=Column(Integer)
    sanrentan4_num2=Column(Integer)
    sanrentan4_num3=Column(Integer)
    sanrentan4_ret=Column(Integer)
    sanrentan5_num1=Column(Integer)
    sanrentan5_num2=Column(Integer)
    sanrentan5_num3=Column(Integer)
    sanrentan5_ret=Column(Integer)
    sanrentan6_num1=Column(Integer)
    sanrentan6_num2=Column(Integer)
    sanrentan6_num3=Column(Integer)
    sanrentan6_ret=Column(Integer)
    #ラベルデータのセット
    #winlabel = np.zeros([18])
    #winlabel[int(win1_num) - 1] = 1

    

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racekey':self.racekey,
            'win1_num':self.win1_num,
            'win1_ret':self.win1_ret,
            'win2_num':self.win2_num,
            'win2_ret':self.win2_ret,
            'win3_num':self.win3_num,
            'win3_ret':self.win3_ret,
            'place1_num':self.place1_num,
            'place1_ret':self.place1_ret,
            'place2_num':self.place2_num,
            'place2_ret':self.place2_ret,
            'place3_num':self.place3_num,
            'place3_ret':self.place3_ret,
            'place4_num':self.place4_num,
            'place4_ret':self.place4_ret,
            'place5_num':self.place5_num,
            'place5_ret':self.place5_ret,
            'wakuren1_num1':self.wakuren1_num1,
            'wakuren1_num2':self.wakuren1_num2,
            'wakuren1_ret':self.wakuren1_ret,
            'wakuren2_num1':self.wakuren2_num1,
            'wakuren2_num2':self.wakuren2_num2,
            'wakuren2_ret':self.wakuren2_ret,
            'wakuren3_num1':self.wakuren3_num1,
            'wakuren3_num2':self.wakuren3_num2,
            'wakuren3_ret':self.wakuren3_ret,
            'umaren1_num1':self.umaren1_num1,
            'umaren1_num2':self.umaren1_num2,
            'umaren1_ret':self.umaren1_ret,
            'umaren2_num1':self.umaren2_num1,
            'umaren2_num2':self.umaren2_num2,
            'umaren2_ret':self.umaren2_ret,
            'umaren3_num1':self.umaren3_num1,
            'umaren3_num2':self.umaren3_num2,
            'umaren3_ret':self.umaren3_ret,
            'wide1_num1':self.wide1_num1,
            'wide1_num2':self.wide1_num2,
            'wide1_ret':self.wide1_ret,
            'wide2_num1':self.wide2_num1,
            'wide2_num2':self.wide2_num2,
            'wide2_ret':self.wide2_ret,
            'wide3_num1':self.wide3_num1,
            'wide3_num2':self.wide3_num2,
            'wide3_ret':self.wide3_ret,
            'wide4_num1':self.wide4_num1,
            'wide4_num2':self.wide4_num2,
            'wide4_ret':self.wide4_ret,
            'wide5_num1':self.wide5_num1,
            'wide5_num2':self.wide5_num2,
            'wide5_ret':self.wide5_ret,
            'wide6_num1':self.wide6_num1,
            'wide6_num2':self.wide6_num2,
            'wide6_ret':self.wide6_ret,
            'wide7_num1':self.wide7_num1,
            'wide7_num2':self.wide7_num2,
            'wide7_ret':self.wide7_ret,
            'umatan1_num1':self.umatan1_num1,
            'umatan1_num2':self.umatan1_num2,
            'umatan1_ret':self.umatan1_ret,
            'umatan2_num1':self.umatan2_num1,
            'umatan2_num2':self.umatan2_num2,
            'umatan2_ret':self.umatan2_ret,
            'umatan3_num1':self.umatan3_num1,
            'umatan3_num2':self.umatan3_num2,
            'umatan3_ret':self.umatan3_ret,
            'umatan4_num1':self.umatan4_num1,
            'umatan4_num2':self.umatan4_num2,
            'umatan4_ret':self.umatan4_ret,
            'umatan5_num1':self.umatan5_num1,
            'umatan5_num2':self.umatan5_num2,
            'umatan5_ret':self.umatan5_ret,
            'umatan6_num1':self.umatan6_num1,
            'umatan6_num2':self.umatan6_num2,
            'umatan6_ret':self.umatan6_ret,
            'sanrenpuku1_num1':self.sanrenpuku1_num1,
            'sanrenpuku1_num2':self.sanrenpuku1_num2,
            'sanrenpuku1_num3':self.sanrenpuku1_num3,
            'sanrenpuku1_ret':self.sanrenpuku1_ret,
            'sanrenpuku2_num1':self.sanrenpuku2_num1,
            'sanrenpuku2_num2':self.sanrenpuku2_num2,
            'sanrenpuku2_num3':self.sanrenpuku2_num3,
            'sanrenpuku2_ret':self.sanrenpuku2_ret,
            'sanrenpuku3_num1':self.sanrenpuku3_num1,
            'sanrenpuku3_num2':self.sanrenpuku3_num2,
            'sanrenpuku3_num3':self.sanrenpuku3_num3,
            'sanrenpuku3_ret':self.sanrenpuku3_ret,
            'sanrentan1_num1':self.sanrentan1_num1,
            'sanrentan1_num2':self.sanrentan1_num2,
            'sanrentan1_num3':self.sanrentan1_num3,
            'sanrentan1_ret':self.sanrentan1_ret,
            'sanrentan2_num1':self.sanrentan2_num1,
            'sanrentan2_num2':self.sanrentan2_num2,
            'sanrentan2_num3':self.sanrentan2_num3,
            'sanrentan2_ret':self.sanrentan2_ret,
            'sanrentan3_num1':self.sanrentan3_num1,
            'sanrentan3_num2':self.sanrentan3_num2,
            'sanrentan3_num3':self.sanrentan3_num3,
            'sanrentan3_ret':self.sanrentan3_ret,
            'sanrentan4_num1':self.sanrentan4_num1,
            'sanrentan4_num2':self.sanrentan4_num2,
            'sanrentan4_num3':self.sanrentan4_num3,
            'sanrentan4_ret':self.sanrentan4_ret,
            'sanrentan5_num1':self.sanrentan5_num1,
            'sanrentan5_num2':self.sanrentan5_num2,
            'sanrentan5_num3':self.sanrentan5_num3,
            'sanrentan5_ret':self.sanrentan5_ret,
            'sanrentan6_num1':self.sanrentan6_num1,
            'sanrentan6_num2':self.sanrentan6_num2,
            'sanrentan6_num3':self.sanrentan6_num3,
            'sanrentan6_ret':self.sanrentan6_ret
        }

class BacodeMaster(Base):
    __tablename__ = 'bacodemaster'
    bacode = Column(Integer,primary_key=True)
    baname = Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'bacode':self.bacode,
            'baname':self.baname
        }

class JuryoMaster(Base):
    __tablename__ = 'juryomaster'
    juryo = Column(Integer,primary_key=True)
    juryo_name = Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'juryo':self.juryo,
            'juryo_name':self.juryo_name
        }

class JokenMaster(Base):
    __tablename__ = 'jokenmaster'
    joken = Column(String,primary_key=True)
    joken_group = Column(Integer)
    joken_name = Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'joken':self.joken,
            'joken_group':self.joken_group,
            'joken_name':self.joken_name
        }

class JokenGroupMaster(Base):
    __tablename__ = 'jokengroupmaster'
    joken_group = Column(Integer,primary_key = True)
    joken_group_name = Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'joken_group':self.joken_group,
            'joken_group_name':self.joken_group_name
        }

class ShubetsuMaster(Base):
    __tablename__ = 'shubetsumaster'
    shubetsu = Column(Integer,primary_key = True)
    shubetsu_name = Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'shubetsu':self.shubetsu,
            'shubetsu_name':self.shubetsu_name
        }
        
class IjokbnMaster(Base):
    __tablename__ = 'ijokbnmaster'
    ijo_kbn = Column(Integer,primary_key = True)
    ijo_kbn_name = Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'ijo_kbn':self.ijo_kbn,
            'ijo_kbn_name':self.ijo_kbn_name
        }

class TenkoMaster(Base):
    __tablename__ = 'tenkomaster'
    tenko = Column(Integer,primary_key = True)
    tenko_name = Column(String)
    
    kaisai = relationship("KaisaiData", uselist=False,backref="tenkoma")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'tenko':self.tenko,
            'tenko_name':self.tenko_name
        }

class RestreasoncodeMaster(Base):
    __tablename__ = 'restreasoncodemaster'
    rest_reason_code = Column(Integer,primary_key = True)
    rest_reason_name = Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'rest_reason_code':self.rest_reason_code,
            'rest_reason_name':self.rest_reason_name
        }

class LegtypeMaster(Base):
    __tablename__ = 'legtypemaster'
    leg_type = Column(Integer,primary_key = True)
    race_leg_type = Column(String)
    leg_type_name = Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'leg_type':self.leg_type,
            'race_leg_type':self.race_leg_type,
            'leg_type_name':self.leg_type_name
        }

class DistanceadjustMaster(Base):
    __tablename__ = 'distanceadjustmaster'
    distance_adjust = Column(Integer,primary_key = True)
    distance_name = Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'distance_adjust':self.distance_adjust,
            'distance_name':self.distance_name
        }

class TrainerData(Base):
    __tablename__ = 'trainer'
    trainer_code=Column(Integer,primary_key=True)
    delete_flg=Column(Integer)
    delete_ymd=Column(Integer)
    trainer_name=Column(String)
    trainer_kana=Column(String)
    trainer_name_short=Column(String)
    shozoku_code=Column(Integer)
    shozoku_region=Column(String)
    birthday=Column(Integer)
    get_licence_year=Column(Integer)
    trainer_comment=Column(String)
    comment_ymd=Column(Integer)
    this_leading=Column(Integer)
    this_seiseki_flat_1st=Column(Integer)
    this_seiseki_flat_2nd=Column(Integer)
    this_seiseki_flat_3rd=Column(Integer)
    this_seiseki_flat_out=Column(Integer)
    this_seiseki_steeple_1st=Column(Integer)
    this_seiseki_steeple_2nd=Column(Integer)
    this_seiseki_steeple_3rd=Column(Integer)
    this_seiseki_steeple_out=Column(Integer)
    this_tokubetsu_win=Column(Integer)
    this_jusho_win=Column(Integer)
    last_leading=Column(Integer)
    last_seiseki_flat_1st=Column(Integer)
    last_seiseki_flat_2nd=Column(Integer)
    last_seiseki_flat_3rd=Column(Integer)
    last_seiseki_flat_out=Column(Integer)
    last_seiseki_steeple_1st=Column(Integer)
    last_seiseki_steeple_2nd=Column(Integer)
    last_seiseki_steeple_3rd=Column(Integer)
    last_seiseki_steeple_out=Column(Integer)
    last_tokubetsu_win=Column(Integer)
    last_jusho_win=Column(Integer)
    total_seiseki_flat_1st=Column(Integer)
    total_seiseki_flat_2nd=Column(Integer)
    total_seiseki_flat_3rd=Column(Integer)
    total_seiseki_flat_out=Column(Integer)
    total_seiseki_steeple_1st=Column(Integer)
    total_seiseki_steeple_2nd=Column(Integer)
    total_seiseki_steeple_3rd=Column(Integer)
    total_seiseki_steeple_out=Column(Integer)
    data_ymd=Column(Integer)
    trainer_index=Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'trainer_code':self.trainer_code,
            'delete_flg':self.delete_flg,
            'delete_ymd':self.delete_ymd,
            'trainer_name':self.trainer_name,
            'trainer_kana':self.trainer_kana,
            'trainer_name_short':self.trainer_name_short,
            'shozoku_code':self.shozoku_code,
            'shozoku_region':self.shozoku_region,
            'birthday':self.birthday,
            'get_licence_year':self.get_licence_year,
            'trainer_comment':self.trainer_comment,
            'comment_ymd':self.comment_ymd,
            'this_leading':self.this_leading,
            'this_seiseki_flat_1st':self.this_seiseki_flat_1st,
            'this_seiseki_flat_2nd':self.this_seiseki_flat_2nd,
            'this_seiseki_flat_3rd':self.this_seiseki_flat_3rd,
            'this_seiseki_flat_out':self.this_seiseki_flat_out,
            'this_seiseki_steeple_1st':self.this_seiseki_steeple_1st,
            'this_seiseki_steeple_2nd':self.this_seiseki_steeple_2nd,
            'this_seiseki_steeple_3rd':self.this_seiseki_steeple_3rd,
            'this_seiseki_steeple_out':self.this_seiseki_steeple_out,
            'this_tokubetsu_win':self.this_tokubetsu_win,
            'this_jusho_win':self.this_jusho_win,
            'last_leading':self.last_leading,
            'last_seiseki_flat_1st':self.last_seiseki_flat_1st,
            'last_seiseki_flat_2nd':self.last_seiseki_flat_2nd,
            'last_seiseki_flat_3rd':self.last_seiseki_flat_3rd,
            'last_seiseki_flat_out':self.last_seiseki_flat_out,
            'last_seiseki_steeple_1st':self.last_seiseki_steeple_1st,
            'last_seiseki_steeple_2nd':self.last_seiseki_steeple_2nd,
            'last_seiseki_steeple_3rd':self.last_seiseki_steeple_3rd,
            'last_seiseki_steeple_out':self.last_seiseki_steeple_out,
            'last_tokubetsu_win':self.last_tokubetsu_win,
            'last_jusho_win':self.last_jusho_win,
            'total_seiseki_flat_1st':self.total_seiseki_flat_1st,
            'total_seiseki_flat_2nd':self.total_seiseki_flat_2nd,
            'total_seiseki_flat_3rd':self.total_seiseki_flat_3rd,
            'total_seiseki_flat_out':self.total_seiseki_flat_out,
            'total_seiseki_steeple_1st':self.total_seiseki_steeple_1st,
            'total_seiseki_steeple_2nd':self.total_seiseki_steeple_2nd,
            'total_seiseki_steeple_3rd':self.total_seiseki_steeple_3rd,
            'total_seiseki_steeple_out':self.total_seiseki_steeple_out,
            'data_ymd':self.data_ymd,
            'trainer_index':self.trainer_index
        }

class JockeyData(Base):
    __tablename__ = 'jockey'
    jockey_code=Column(Integer,primary_key=True)
    delete_flg=Column(Integer)
    delete_ymd=Column(Integer)
    jockey_name=Column(String)
    jockey_name_kana=Column(String)
    jockey_name_short=Column(String)
    shozoku_code=Column(Integer)
    shozoku_region=Column(String)
    birthday=Column(Integer)
    get_licence_year=Column(Integer)
    minarai_kbn=Column(Integer)
    trainer_code=Column(Integer)
    jockey_comment=Column(String)
    comment_ymd=Column(Integer)
    this_leading=Column(Integer)
    this_flat_seiseki_1st=Column(Integer)
    this_flat_seiseki_2nd=Column(Integer)
    this_flat_seiseki_3rd=Column(Integer)
    this_flat_seiseki_out=Column(Integer)
    this_steeple_seiseki_1st=Column(Integer)
    this_steeple_seiseki_2nd=Column(Integer)
    this_steeple_seiseki_3rd=Column(Integer)
    this_steeple_seiseki_out=Column(Integer)
    this_tokubetsu_win=Column(Integer)
    this_jusho_win=Column(Integer)
    last_leading=Column(Integer)
    last_flat_seiseki_1st=Column(Integer)
    last_flat_seiseki_2nd=Column(Integer)
    last_flat_seiseki_3rd=Column(Integer)
    last_flat_seiseki_out=Column(Integer)
    last_steeple_seiseki_1st=Column(Integer)
    last_steeple_seiseki_2nd=Column(Integer)
    last_steeple_seiseki_3rd=Column(Integer)
    last_steeple_seiseki_out=Column(Integer)
    last_tokubetsu_win=Column(Integer)
    last_jusho_win=Column(Integer)
    total_flat_seiseki_1st=Column(Integer)
    total_flat_seiseki_2nd=Column(Integer)
    total_flat_seiseki_3rd=Column(Integer)
    total_flat_seiseki_out=Column(Integer)
    total_steeple_seiseki_1st=Column(Integer)
    total_steeple_seiseki_2nd=Column(Integer)
    total_steeple_seiseki_3rd=Column(Integer)
    total_steeple_seiseki_out=Column(Integer)
    data_ymd=Column(Integer)
    jockey_index=Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'jockey_code':self.jockey_code,
            'delete_flg':self.delete_flg,
            'delete_ymd':self.delete_ymd,
            'jockey_name':self.jockey_name,
            'jockey_name_kana':self.jockey_name_kana,
            'jockey_name_short':self.jockey_name_short,
            'shozoku_code':self.shozoku_code,
            'shozoku_region':self.shozoku_region,
            'birthday':self.birthday,
            'get_licence_year':self.get_licence_year,
            'minarai_kbn':self.minarai_kbn,
            'trainer_code':self.trainer_code,
            'jockey_comment':self.jockey_comment,
            'comment_ymd':self.comment_ymd,
            'this_leading':self.this_leading,
            'this_flat_seiseki_1st':self.this_flat_seiseki_1st,
            'this_flat_seiseki_2nd':self.this_flat_seiseki_2nd,
            'this_flat_seiseki_3rd':self.this_flat_seiseki_3rd,
            'this_flat_seiseki_out':self.this_flat_seiseki_out,
            'this_steeple_seiseki_1st':self.this_steeple_seiseki_1st,
            'this_steeple_seiseki_2nd':self.this_steeple_seiseki_2nd,
            'this_steeple_seiseki_3rd':self.this_steeple_seiseki_3rd,
            'this_steeple_seiseki_out':self.this_steeple_seiseki_out,
            'this_tokubetsu_win':self.this_tokubetsu_win,
            'this_jusho_win':self.this_jusho_win,
            'last_leading':self.last_leading,
            'last_flat_seiseki_1st':self.last_flat_seiseki_1st,
            'last_flat_seiseki_2nd':self.last_flat_seiseki_2nd,
            'last_flat_seiseki_3rd':self.last_flat_seiseki_3rd,
            'last_flat_seiseki_out':self.last_flat_seiseki_out,
            'last_steeple_seiseki_1st':self.last_steeple_seiseki_1st,
            'last_steeple_seiseki_2nd':self.last_steeple_seiseki_2nd,
            'last_steeple_seiseki_3rd':self.last_steeple_seiseki_3rd,
            'last_steeple_seiseki_out':self.last_steeple_seiseki_out,
            'last_tokubetsu_win':self.last_tokubetsu_win,
            'last_jusho_win':self.last_jusho_win,
            'total_flat_seiseki_1st':self.total_flat_seiseki_1st,
            'total_flat_seiseki_2nd':self.total_flat_seiseki_2nd,
            'total_flat_seiseki_3rd':self.total_flat_seiseki_3rd,
            'total_flat_seiseki_out':self.total_flat_seiseki_out,
            'total_steeple_seiseki_1st':self.total_steeple_seiseki_1st,
            'total_steeple_seiseki_2nd':self.total_steeple_seiseki_2nd,
            'total_steeple_seiseki_3rd':self.total_steeple_seiseki_3rd,
            'total_steeple_seiseki_out':self.total_steeple_seiseki_out,
            'data_ymd':self.data_ymd,
            'jockey_index':self.jockey_index
        }

class HorsebaseData(Base):
    __tablename__ = 'horsebase'
    blood=Column(Integer,ForeignKey('racehorse.blood'),primary_key=True)
    horse=Column(String)
    sex=Column(Integer)
    hair=Column(Integer)
    umakigo=Column(Integer)
    father=Column(String)
    mother=Column(String)
    mother_father=Column(String)
    birthday=Column(Integer)
    father_birthyear=Column(Integer)
    mother_birthyear=Column(Integer)
    mother_father_birthyear=Column(Integer)
    owner=Column(String)
    owner_kai_code=Column(Integer)
    producer=Column(String)
    locality=Column(String)
    delete_flg=Column(Integer)
    data_ymd=Column(Integer)
    father_phylogeny=Column(Integer)
    mother_phylogeny=Column(Integer)
    horse_index=Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'blood':self.blood,
            'horse':self.horse,
            'sex':self.sex,
            'hair':self.hair,
            'umakigo':self.umakigo,
            'father':self.father,
            'mother':self.mother,
            'mother_father':self.mother_father,
            'birthday':self.birthday,
            'father_birthyear':self.father_birthyear,
            'mother_birthyear':self.mother_birthyear,
            'mother_father_birthyear':self.mother_father_birthyear,
            'owner':self.owner,
            'owner_kai_code':self.owner_kai_code,
            'producer':self.producer,
            'locality':self.locality,
            'delete_flg':self.delete_flg,
            'data_ymd':self.data_ymd,
            'father_phylogeny':self.father_phylogeny,
            'mother_phylogeny':self.mother_phylogeny,
            'horse_index':self.horse_index
        }


class WorkTable(Base):
    __tablename__ = 'worktable'
    racehorsekey=Column(String,primary_key=True)
    racekey=Column(String,ForeignKey('bangumi.racekey'))
    bacode=Column(Integer)
    year=Column(Integer)
    kai=Column(Integer)
    day=Column(Integer)
    race=Column(Integer)
    num=Column(Integer)
    blood=Column(Integer)
#    horse_base = relationship("HorsebaseData",uselist=False,backref="racehorse",lazy='subquery')
#    result = relationship("SeisekiData",uselist=False,backref="racehorse",lazy='subquery')
    horse=Column(String)
    idm=Column(Integer)
    jockey_score=Column(Integer)
    info_score=Column(Integer)
    sogo_score=Column(Integer)
    leg_type=Column(Integer)
    distance_adjust=Column(Integer)
    up_degree=Column(Integer)
    routin=Column(Integer)
    cri_odds=Column(Integer)
    cri_popular_order=Column(Integer)
    cri_fukusho_odds=Column(Integer)
    cri_fukusho_popluar_order=Column(Integer)
    specific_info_1=Column(Integer)
    specific_info_2=Column(Integer)
    specific_info_3=Column(Integer)
    specific_info_4=Column(Integer)
    specific_info_5=Column(Integer)
    sogo_info_1=Column(Integer)
    sogo_info_2=Column(Integer)
    sogo_info_3=Column(Integer)
    sogo_info_4=Column(Integer)
    sogo_info_5=Column(Integer)
    pop_score=Column(Integer)
    train_score=Column(Integer)
    trainer_score=Column(Integer)
    train_code=Column(Integer)
    trainer_hyoka_code=Column(Integer)
    jockey_rate_rentai=Column(Integer)
    gekiso_score=Column(Integer)
    hidume_code=Column(Integer)
    hidume_code_index=Column(Integer)
    hidume_shape=Column(Integer)
    hidume_size=Column(Integer)
    omotekisei_code=Column(Integer)
    class_code=Column(Integer)
    brinkers=Column(String)
    jockey_name=Column(String)
    kinryo=Column(Integer)
    minarai=Column(Integer)
    trainer_name=Column(String)
    trainer_shozoku=Column(String)
    zenso_seiseki_key_1=Column(String)
    zenso_seiseki_key_2=Column(String)
    zenso_seiseki_key_3=Column(String)
    zenso_seiseki_key_4=Column(String)
    zenso_seiseki_key_5=Column(String)
    zenso_racekey_1=Column(String)
    zenso_racekey_2=Column(String)
    zenso_racekey_3=Column(String)
    zenso_racekey_4=Column(String)
    zenso_racekey_5=Column(String)
    waku=Column(Integer)
    sogo_shirushi=Column(Integer)
    idm_shiruishi=Column(Integer)
    info_shirushi=Column(Integer)
    jockey_shirushi=Column(Integer)
    trainer_shirushi=Column(Integer)
    train_shirushi=Column(Integer)
    gekiso_shirushi=Column(Integer)
    turf_adjust_code=Column(Integer)
    dart_adjust_code=Column(Integer)
    jockey_code=Column(Integer)
    trainer_code=Column(Integer)
    kakutoku_money=Column(Integer)
    shukaku_money=Column(Integer)
    joken=Column(Integer)
    ten_score=Column(Integer)
    pace_score=Column(Integer)
    up_score=Column(Integer)
    position_score=Column(Integer)
    pace_predict=Column(String)
    dochu_order=Column(Integer)
    dochu_sa=Column(Integer)
    dochu_in_out=Column(Integer)
    last_order=Column(Integer)
    last_sa=Column(Integer)
    last_in_out=Column(Integer)
    order=Column(Integer)
    sa=Column(Integer)
    in_out=Column(Integer)
    tenkai=Column(String)
    distance_adjust2=Column(Integer)
    commit_weight=Column(Integer)
    commit_weight_increase=Column(Integer)
    torikeshi=Column(Integer)
    sex=Column(Integer)
    owner_name=Column(String)
    banushikai_code=Column(Integer)
    umakigo_code=Column(Integer)
    gekiso_order=Column(Integer)
    ls_score_order=Column(Integer)
    ten_score_order=Column(Integer)
    pace_score_order=Column(Integer)
    up_score_order=Column(Integer)
    position_score_order=Column(Integer)
    expect_jokey_win_rate=Column(Integer)
    expect_jokey_rentai_rate=Column(Integer)
    yuso=Column(String)
    soho=Column(Integer)
    taikei_data=Column(String)
    taikei=Column(Integer)
    senaka=Column(Integer)
    do=Column(Integer)
    siri=Column(Integer)
    tomo=Column(Integer)
    harabukuro=Column(Integer)
    head=Column(Integer)
    neck=Column(Integer)
    breast=Column(Integer)
    shoulder=Column(Integer)
    zencho=Column(Integer)
    kocho=Column(Integer)
    maehaba=Column(Integer)
    ushirohaba=Column(Integer)
    maetsunagi=Column(Integer)
    ushirotsunagi=Column(Integer)
    tail=Column(Integer)
    furikata=Column(Integer)
    taikei_sogo1=Column(Integer)
    taikei_sogo2=Column(Integer)
    taikei_sogo3=Column(Integer)
    umatokki1=Column(Integer)
    umatokki2=Column(Integer)
    umatokki3=Column(Integer)
    horse_start_score=Column(Integer)
    horse_latestart_rate=Column(Integer)
    sanko_zenso=Column(Integer)
    sanko_zenso_jockey_code=Column(String)
    mambaken_score=Column(Integer)
    mambaken_shirushi=Column(Integer)
    kokyu_flg=Column(Integer)
    gekiso_type=Column(String)
    rest_reason_code=Column(Integer)
    flg=Column(String)
    turf_dart_steeple_flg=Column(Integer)
    distance_flg=Column(Integer)
    class_flg=Column(Integer)
    tenkyu_flg=Column(Integer)
    kyosei_flg=Column(Integer)
    norikae_flg=Column(Integer)
    runtimes_first_train=Column(Integer)
    date_first_train=Column(Integer)
    days_after_first_train=Column(Integer)
    hobokusaki=Column(String)
    hobokusaki_index=Column(Integer)
    hobokusaki_rank=Column(String)
    trainer_rank=Column(Integer)
    train_type=Column(String)
    train_course_kind=Column(String)
    saka=Column(Integer)
    wood=Column(Integer)
    dart=Column(Integer)
    turf=Column(Integer)
    pool=Column(Integer)
    steeple=Column(Integer)
    politruck=Column(Integer)
    train_distance=Column(Integer)
    train_juten=Column(Integer)
    train_oikiri_score=Column(Integer)
    shiage_score=Column(Integer)
    train_vol_hyoka=Column(String)
    shiage_score_change=Column(Integer)
    oikiri_num=Column(Integer)
    kaisu=Column(Integer)
    train_course_code=Column(String)
    train_course_code_index=Column(Integer)
    oikiri_kind=Column(Integer)
    oikiri_state=Column(Integer)
    oikiri_state_index=Column(Integer)
    train_f=Column(Integer)
    ten_f=Column(Integer)
    mid_f=Column(Integer)
    end_f=Column(Integer)
    ten_f_score=Column(Integer)
    mid_f_score=Column(Integer)
    end_f_score=Column(Integer)
    oikiri_score=Column(Integer)
    horse_index=Column(Integer)
    jockey_index=Column(Integer)
    trainer_index=Column(Integer)
    zenso1_bacode=Column(Integer)
    zenso1_year=Column(Integer)
    zenso1_kai=Column(Integer)
    zenso1_day=Column(Integer)
    zenso1_raceno=Column(Integer)
    zenso1_num=Column(Integer)
    zenso1_distance=Column(Integer)
    zenso1_tdscode=Column(Integer)
    zenso1_right_left=Column(Integer)
    zenso1_in_out=Column(Integer)
    zenso1_baba=Column(Integer)
    zenso1_baba_abst=Column(Integer)
    zenso1_baba_detail=Column(Integer)
    zenso1_shubetsu=Column(Integer)
    zenso1_joken=Column(String)
    zenso1_kigo=Column(Integer)
    zenso1_juryo=Column(Integer)
    zenso1_grade=Column(Integer)
    zenso1_num_of_all_horse=Column(Integer)
    zenso1_order=Column(Integer)
    zenso1_ijo_kbn=Column(Integer)
    zenso1_time=Column(Integer)
    zenso1_kinryo=Column(Integer)
    zenso1_decided_odds=Column(Integer)
    zenso1_decided_pop_order=Column(Integer)
    zenso1_natural_score=Column(Integer)
    zenso1_baba_sa=Column(Integer)
    zenso1_pace=Column(Integer)
    zenso1_start_late=Column(Integer)
    zenso1_position=Column(Integer)
    zenso1_furi=Column(Integer)
    zenso1_mae_furi=Column(Integer)
    zenso1_naka_furi=Column(Integer)
    zenso1_ushiro_furi=Column(Integer)
    zenso1_race=Column(Integer)
    zenso1_course_position=Column(Integer)
    zenso1_up_code=Column(Integer)
    zenso1_class_code=Column(Integer)
    zenso1_batai_code=Column(Integer)
    zenso1_kehai_code=Column(Integer)
    zenso1_racepace=Column(String)
    zenso1_umapace=Column(String)
    zenso1_ten_score=Column(Integer)
    zenso1_up_score=Column(Integer)
    zenso1_pace_score=Column(Integer)
    zenso1_racep_score=Column(Integer)
    zenso1_time_sa=Column(Integer)
    zenso1_mae3f_time=Column(Integer)
    zenso1_agari3f_time=Column(Integer)
    zenso1_corner_order1=Column(Integer)
    zenso1_corner_order2=Column(Integer)
    zenso1_corner_order3=Column(Integer)
    zenso1_corner_order4=Column(Integer)
    zenso1_mae3f_sa=Column(Integer)
    zenso1_agari3f_sa=Column(Integer)
    zenso1_jockey_code=Column(Integer)
    zenso1_trainer_code=Column(Integer)
    zenso1_weight=Column(Integer)
    zenso1_weight_increase=Column(Integer)
    zenso1_tenko=Column(Integer)
    zenso1_course=Column(Integer)
    zenso1_race_leg_type=Column(String)
    zenso1_race_pace_flow=Column(Integer)
    zenso1_horse_pace_flow=Column(Integer)
    zenso1_corner4_course_position=Column(Integer)
    zenso1_paceupposition=Column(Integer)
    zenso2_bacode=Column(Integer)
    zenso2_year=Column(Integer)
    zenso2_kai=Column(Integer)
    zenso2_day=Column(Integer)
    zenso2_raceno=Column(Integer)
    zenso2_num=Column(Integer)
    zenso2_distance=Column(Integer)
    zenso2_tdscode=Column(Integer)
    zenso2_right_left=Column(Integer)
    zenso2_in_out=Column(Integer)
    zenso2_baba=Column(Integer)
    zenso2_baba_abst=Column(Integer)
    zenso2_baba_detail=Column(Integer)
    zenso2_shubetsu=Column(Integer)
    zenso2_joken=Column(String)
    zenso2_kigo=Column(Integer)
    zenso2_juryo=Column(Integer)
    zenso2_grade=Column(Integer)
    zenso2_num_of_all_horse=Column(Integer)
    zenso2_order=Column(Integer)
    zenso2_ijo_kbn=Column(Integer)
    zenso2_time=Column(Integer)
    zenso2_kinryo=Column(Integer)
    zenso2_decided_odds=Column(Integer)
    zenso2_decided_pop_order=Column(Integer)
    zenso2_natural_score=Column(Integer)
    zenso2_baba_sa=Column(Integer)
    zenso2_pace=Column(Integer)
    zenso2_start_late=Column(Integer)
    zenso2_position=Column(Integer)
    zenso2_furi=Column(Integer)
    zenso2_mae_furi=Column(Integer)
    zenso2_naka_furi=Column(Integer)
    zenso2_ushiro_furi=Column(Integer)
    zenso2_race=Column(Integer)
    zenso2_course_position=Column(Integer)
    zenso2_up_code=Column(Integer)
    zenso2_class_code=Column(Integer)
    zenso2_batai_code=Column(Integer)
    zenso2_kehai_code=Column(Integer)
    zenso2_racepace=Column(String)
    zenso2_umapace=Column(String)
    zenso2_ten_score=Column(Integer)
    zenso2_up_score=Column(Integer)
    zenso2_pace_score=Column(Integer)
    zenso2_racep_score=Column(Integer)
    zenso2_time_sa=Column(Integer)
    zenso2_mae3f_time=Column(Integer)
    zenso2_agari3f_time=Column(Integer)
    zenso2_corner_order1=Column(Integer)
    zenso2_corner_order2=Column(Integer)
    zenso2_corner_order3=Column(Integer)
    zenso2_corner_order4=Column(Integer)
    zenso2_mae3f_sa=Column(Integer)
    zenso2_agari3f_sa=Column(Integer)
    zenso2_jockey_code=Column(Integer)
    zenso2_trainer_code=Column(Integer)
    zenso2_weight=Column(Integer)
    zenso2_weight_increase=Column(Integer)
    zenso2_tenko=Column(Integer)
    zenso2_course=Column(Integer)
    zenso2_race_leg_type=Column(String)
    zenso2_race_pace_flow=Column(Integer)
    zenso2_horse_pace_flow=Column(Integer)
    zenso2_corner4_course_position=Column(Integer)
    zenso2_paceupposition=Column(Integer)
    zenso3_bacode=Column(Integer)
    zenso3_year=Column(Integer)
    zenso3_kai=Column(Integer)
    zenso3_day=Column(Integer)
    zenso3_raceno=Column(Integer)
    zenso3_num=Column(Integer)
    zenso3_distance=Column(Integer)
    zenso3_tdscode=Column(Integer)
    zenso3_right_left=Column(Integer)
    zenso3_in_out=Column(Integer)
    zenso3_baba=Column(Integer)
    zenso3_baba_abst=Column(Integer)
    zenso3_baba_detail=Column(Integer)
    zenso3_shubetsu=Column(Integer)
    zenso3_joken=Column(String)
    zenso3_kigo=Column(Integer)
    zenso3_juryo=Column(Integer)
    zenso3_grade=Column(Integer)
    zenso3_num_of_all_horse=Column(Integer)
    zenso3_order=Column(Integer)
    zenso3_ijo_kbn=Column(Integer)
    zenso3_time=Column(Integer)
    zenso3_kinryo=Column(Integer)
    zenso3_decided_odds=Column(Integer)
    zenso3_decided_pop_order=Column(Integer)
    zenso3_natural_score=Column(Integer)
    zenso3_baba_sa=Column(Integer)
    zenso3_pace=Column(Integer)
    zenso3_start_late=Column(Integer)
    zenso3_position=Column(Integer)
    zenso3_furi=Column(Integer)
    zenso3_mae_furi=Column(Integer)
    zenso3_naka_furi=Column(Integer)
    zenso3_ushiro_furi=Column(Integer)
    zenso3_race=Column(Integer)
    zenso3_course_position=Column(Integer)
    zenso3_up_code=Column(Integer)
    zenso3_class_code=Column(Integer)
    zenso3_batai_code=Column(Integer)
    zenso3_kehai_code=Column(Integer)
    zenso3_racepace=Column(String)
    zenso3_umapace=Column(String)
    zenso3_ten_score=Column(Integer)
    zenso3_up_score=Column(Integer)
    zenso3_pace_score=Column(Integer)
    zenso3_racep_score=Column(Integer)
    zenso3_time_sa=Column(Integer)
    zenso3_mae3f_time=Column(Integer)
    zenso3_agari3f_time=Column(Integer)
    zenso3_corner_order1=Column(Integer)
    zenso3_corner_order2=Column(Integer)
    zenso3_corner_order3=Column(Integer)
    zenso3_corner_order4=Column(Integer)
    zenso3_mae3f_sa=Column(Integer)
    zenso3_agari3f_sa=Column(Integer)
    zenso3_jockey_code=Column(Integer)
    zenso3_trainer_code=Column(Integer)
    zenso3_weight=Column(Integer)
    zenso3_weight_increase=Column(Integer)
    zenso3_tenko=Column(Integer)
    zenso3_course=Column(Integer)
    zenso3_race_leg_type=Column(String)
    zenso3_race_pace_flow=Column(Integer)
    zenso3_horse_pace_flow=Column(Integer)
    zenso3_corner4_course_position=Column(Integer)
    zenso3_paceupposition=Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racehorsekey':self.racehorsekey,
            'racekey':self.racekey,
            'bacode':self.bacode,
            'year':self.year,
            'kai':self.kai,
            'day':self.day,
            'race':self.race,
            'num':self.num,
            'blood':self.blood,
            'horse':self.horse,
            'idm':self.idm,
            'jockey_score':self.jockey_score,
            'info_score':self.info_score,
            'sogo_score':self.sogo_score,
            'leg_type':self.leg_type,
            'distance_adjust':self.distance_adjust,
            'up_degree':self.up_degree,
            'routin':self.routin,
            'cri_odds':self.cri_odds,
            'cri_popular_order':self.cri_popular_order,
            'cri_fukusho_odds':self.cri_fukusho_odds,
            'cri_fukusho_popluar_order':self.cri_fukusho_popluar_order,
            'specific_info_1':self.specific_info_1,
            'specific_info_2':self.specific_info_2,
            'specific_info_3':self.specific_info_3,
            'specific_info_4':self.specific_info_4,
            'specific_info_5':self.specific_info_5,
            'sogo_info_1':self.sogo_info_1,
            'sogo_info_2':self.sogo_info_2,
            'sogo_info_3':self.sogo_info_3,
            'sogo_info_4':self.sogo_info_4,
            'sogo_info_5':self.sogo_info_5,
            'pop_score':self.pop_score,
            'train_score':self.train_score,
            'trainer_score':self.trainer_score,
            'train_code':self.train_code,
            'trainer_hyoka_code':self.trainer_hyoka_code,
            'jockey_rate_rentai':self.jockey_rate_rentai,
            'gekiso_score':self.gekiso_score,
            'hidume_code':self.hidume_code,
            'hidume_code_index':self.hidume_code_index,
            'hidume_shape':self.hidume_shape,
            'hidume_size':self.hidume_size,
            'omotekisei_code':self.omotekisei_code,
            'class_code':self.class_code,
            'brinkers':self.brinkers,
            'jockey_name':self.jockey_name,
            'kinryo':self.kinryo,
            'minarai':self.minarai,
            'trainer_name':self.trainer_name,
            'trainer_shozoku':self.trainer_shozoku,
            'zenso_seiseki_key_1':self.zenso_seiseki_key_1,
            'zenso_seiseki_key_2':self.zenso_seiseki_key_2,
            'zenso_seiseki_key_3':self.zenso_seiseki_key_3,
            'zenso_seiseki_key_4':self.zenso_seiseki_key_4,
            'zenso_seiseki_key_5':self.zenso_seiseki_key_5,
            'zenso_racekey_1':self.zenso_racekey_1,
            'zenso_racekey_2':self.zenso_racekey_2,
            'zenso_racekey_3':self.zenso_racekey_3,
            'zenso_racekey_4':self.zenso_racekey_4,
            'zenso_racekey_5':self.zenso_racekey_5,
            'waku':self.waku,
            'sogo_shirushi':self.sogo_shirushi,
            'idm_shiruishi':self.idm_shiruishi,
            'info_shirushi':self.info_shirushi,
            'jockey_shirushi':self.jockey_shirushi,
            'trainer_shirushi':self.trainer_shirushi,
            'train_shirushi':self.train_shirushi,
            'gekiso_shirushi':self.gekiso_shirushi,
            'turf_adjust_code':self.turf_adjust_code,
            'dart_adjust_code':self.dart_adjust_code,
            'jockey_code':self.jockey_code,
            'trainer_code':self.trainer_code,
            'kakutoku_money':self.kakutoku_money,
            'shukaku_money':self.shukaku_money,
            'joken':self.joken,
            'ten_score':self.ten_score,
            'pace_score':self.pace_score,
            'up_score':self.up_score,
            'position_score':self.position_score,
            'pace_predict':self.pace_predict,
            'dochu_order':self.dochu_order,
            'dochu_sa':self.dochu_sa,
            'dochu_in_out':self.dochu_in_out,
            'last_order':self.last_order,
            'last_sa':self.last_sa,
            'last_in_out':self.last_in_out,
            'order':self.order,
            'sa':self.sa,
            'in_out':self.in_out,
            'tenkai':self.tenkai,
            'distance_adjust2':self.distance_adjust2,
            'commit_weight':self.commit_weight,
            'commit_weight_increase':self.commit_weight_increase,
            'torikeshi':self.torikeshi,
            'sex':self.sex,
            'owner_name':self.owner_name,
            'banushikai_code':self.banushikai_code,
            'umakigo_code':self.umakigo_code,
            'gekiso_order':self.gekiso_order,
            'ls_score_order':self.ls_score_order,
            'ten_score_order':self.ten_score_order,
            'pace_score_order':self.pace_score_order,
            'up_score_order':self.up_score_order,
            'position_score_order':self.position_score_order,
            'expect_jokey_win_rate':self.expect_jokey_win_rate,
            'expect_jokey_rentai_rate':self.expect_jokey_rentai_rate,
            'yuso':self.yuso,
            'soho':self.soho,
            'taikei_data':self.taikei_data,
            'taikei':self.taikei,
            'senaka':self.senaka,
            'do':self.do,
            'siri':self.siri,
            'tomo':self.tomo,
            'harabukuro':self.harabukuro,
            'head':self.head,
            'neck':self.neck,
            'breast':self.breast,
            'shoulder':self.shoulder,
            'zencho':self.zencho,
            'kocho':self.kocho,
            'maehaba':self.maehaba,
            'ushirohaba':self.ushirohaba,
            'maetsunagi':self.maetsunagi,
            'ushirotsunagi':self.ushirotsunagi,
            'tail':self.tail,
            'furikata':self.furikata,
            '0':self.taikei_sogo1,
            '0':self.taikei_sogo2,
            '0':self.taikei_sogo3,
            'umatokki1':self.umatokki1,
            'umatokki2':self.umatokki2,
            'umatokki3':self.umatokki3,
            'horse_start_score':self.horse_start_score,
            'horse_latestart_rate':self.horse_latestart_rate,
            'sanko_zenso':self.sanko_zenso,
            'sanko_zenso_jockey_code':self.sanko_zenso_jockey_code,
            'mambaken_score':self.mambaken_score,
            'mambaken_shirushi':self.mambaken_shirushi,
            'kokyu_flg':self.kokyu_flg,
            'gekiso_type':self.gekiso_type,
            'rest_reason_code':self.rest_reason_code,
            'flg':self.flg,
            'turf_dart_steeple_flg':self.turf_dart_steeple_flg,
            'distance_flg':self.distance_flg,
            'class_flg':self.class_flg,
            'tenkyu_flg':self.tenkyu_flg,
            'kyosei_flg':self.kyosei_flg,
            'norikae_flg':self.norikae_flg,
            'runtimes_first_train':self.runtimes_first_train,
            'date_first_train':self.date_first_train,
            'days_after_first_train':self.days_after_first_train,
            'hobokusaki':self.hobokusaki,
            'hobokusaki_index':self.hobokusaki_index,
            'hobokusaki_rank':self.hobokusaki_rank,
            'trainer_rank':self.trainer_rank,
            'train_type':self.train_type,
            'train_course_kind':self.train_course_kind,
            'saka':self.saka,
            'wood':self.wood,
            'dart':self.dart,
            'turf':self.turf,
            'pool':self.pool,
            'steeple':self.steeple,
            'politruck':self.politruck,
            'train_distance':self.train_distance,
            'train_juten':self.train_juten,
            'train_oikiri_score':self.train_oikiri_score,
            'shiage_score':self.shiage_score,
            'train_vol_hyoka':self.train_vol_hyoka,
            'shiage_score_change':self.shiage_score_change,
            'oikiri_num':self.oikiri_num,
            'kaisu':self.kaisu,
            'train_course_code':self.train_course_code,
            'train_course_code_index':self.train_course_code_index,
            'oikiri_kind':self.oikiri_kind,
            'oikiri_state':self.oikiri_state,
            'oikiri_state_index':self.oikiri_state_index,
            'train_f':self.train_f,
            'ten_f':self.ten_f,
            'mid_f':self.mid_f,
            'end_f':self.end_f,
            'ten_f_score':self.ten_f_score,
            'mid_f_score':self.mid_f_score,
            'end_f_score':self.end_f_score,
            'oikiri_score':self.oikiri_score,
            'horse_index':self.horse_index,
            'jockey_index':self.jockey_index,
            'trainer_index':self.trainer_index,
            'zenso1_bacode':self.zenso1_bacode,
            'zenso1_year':self.zenso1_year,
            'zenso1_kai':self.zenso1_kai,
            'zenso1_day':self.zenso1_day,
            'zenso1_raceno':self.zenso1_raceno,
            'zenso1_num':self.zenso1_num,
            'zenso1_distance':self.zenso1_distance,
            'zenso1_tdscode':self.zenso1_tdscode,
            'zenso1_right_left':self.zenso1_right_left,
            'zenso1_in_out':self.zenso1_in_out,
            'zenso1_baba':self.zenso1_baba,
            'zenso1_baba_abst':self.zenso1_baba_abst,
            'zenso1_baba_detail':self.zenso1_baba_detail,
            'zenso1_shubetsu':self.zenso1_shubetsu,
            'zenso1_joken':self.zenso1_joken,
            'zenso1_kigo':self.zenso1_kigo,
            'zenso1_juryo':self.zenso1_juryo,
            'zenso1_grade':self.zenso1_grade,
            'zenso1_num_of_all_horse':self.zenso1_num_of_all_horse,
            'zenso1_order':self.zenso1_order,
            'zenso1_ijo_kbn':self.zenso1_ijo_kbn,
            'zenso1_time':self.zenso1_time,
            'zenso1_kinryo':self.zenso1_kinryo,
            'zenso1_decided_odds':self.zenso1_decided_odds,
            'zenso1_decided_pop_order':self.zenso1_decided_pop_order,
            'zenso1_natural_score':self.zenso1_natural_score,
            'zenso1_baba_sa':self.zenso1_baba_sa,
            'zenso1_pace':self.zenso1_pace,
            'zenso1_start_late':self.zenso1_start_late,
            'zenso1_position':self.zenso1_position,
            'zenso1_furi':self.zenso1_furi,
            'zenso1_mae_furi':self.zenso1_mae_furi,
            'zenso1_naka_furi':self.zenso1_naka_furi,
            'zenso1_ushiro_furi':self.zenso1_ushiro_furi,
            'zenso1_race':self.zenso1_race,
            'zenso1_course_position':self.zenso1_course_position,
            'zenso1_up_code':self.zenso1_up_code,
            'zenso1_class_code':self.zenso1_class_code,
            'zenso1_batai_code':self.zenso1_batai_code,
            'zenso1_kehai_code':self.zenso1_kehai_code,
            'zenso1_racepace':self.zenso1_racepace,
            'zenso1_umapace':self.zenso1_umapace,
            'zenso1_ten_score':self.zenso1_ten_score,
            'zenso1_up_score':self.zenso1_up_score,
            'zenso1_pace_score':self.zenso1_pace_score,
            'zenso1_racep_score':self.zenso1_racep_score,
            'zenso1_time_sa':self.zenso1_time_sa,
            'zenso1_mae3f_time':self.zenso1_mae3f_time,
            'zenso1_agari3f_time':self.zenso1_agari3f_time,
            'zenso1_corner_order1':self.zenso1_corner_order1,
            'zenso1_corner_order2':self.zenso1_corner_order2,
            'zenso1_corner_order3':self.zenso1_corner_order3,
            'zenso1_corner_order4':self.zenso1_corner_order4,
            'zenso1_mae3f_sa':self.zenso1_mae3f_sa,
            'zenso1_agari3f_sa':self.zenso1_agari3f_sa,
            'zenso1_jockey_code':self.zenso1_jockey_code,
            'zenso1_trainer_code':self.zenso1_trainer_code,
            'zenso1_weight':self.zenso1_weight,
            'zenso1_weight_increase':self.zenso1_weight_increase,
            'zenso1_tenko':self.zenso1_tenko,
            'zenso1_course':self.zenso1_course,
            'zenso1_race_leg_type':self.zenso1_race_leg_type,
            'zenso1_race_pace_flow':self.zenso1_race_pace_flow,
            'zenso1_horse_pace_flow':self.zenso1_horse_pace_flow,
            'zenso1_corner4_course_position':self.zenso1_corner4_course_position,
            'zenso1_paceupposition':self.zenso1_paceupposition,
            'zenso2_bacode':self.zenso2_bacode,
            'zenso2_year':self.zenso2_year,
            'zenso2_kai':self.zenso2_kai,
            'zenso2_day':self.zenso2_day,
            'zenso2_raceno':self.zenso2_raceno,
            'zenso2_num':self.zenso2_num,
            'zenso2_distance':self.zenso2_distance,
            'zenso2_tdscode':self.zenso2_tdscode,
            'zenso2_right_left':self.zenso2_right_left,
            'zenso2_in_out':self.zenso2_in_out,
            'zenso2_baba':self.zenso2_baba,
            'zenso2_baba_abst':self.zenso2_baba_abst,
            'zenso2_baba_detail':self.zenso2_baba_detail,
            'zenso2_shubetsu':self.zenso2_shubetsu,
            'zenso2_joken':self.zenso2_joken,
            'zenso2_kigo':self.zenso2_kigo,
            'zenso2_juryo':self.zenso2_juryo,
            'zenso2_grade':self.zenso2_grade,
            'zenso2_num_of_all_horse':self.zenso2_num_of_all_horse,
            'zenso2_order':self.zenso2_order,
            'zenso2_ijo_kbn':self.zenso2_ijo_kbn,
            'zenso2_time':self.zenso2_time,
            'zenso2_kinryo':self.zenso2_kinryo,
            'zenso2_decided_odds':self.zenso2_decided_odds,
            'zenso2_decided_pop_order':self.zenso2_decided_pop_order,
            'zenso2_natural_score':self.zenso2_natural_score,
            'zenso2_baba_sa':self.zenso2_baba_sa,
            'zenso2_pace':self.zenso2_pace,
            'zenso2_start_late':self.zenso2_start_late,
            'zenso2_position':self.zenso2_position,
            'zenso2_furi':self.zenso2_furi,
            'zenso2_mae_furi':self.zenso2_mae_furi,
            'zenso2_naka_furi':self.zenso2_naka_furi,
            'zenso2_ushiro_furi':self.zenso2_ushiro_furi,
            'zenso2_race':self.zenso2_race,
            'zenso2_course_position':self.zenso2_course_position,
            'zenso2_up_code':self.zenso2_up_code,
            'zenso2_class_code':self.zenso2_class_code,
            'zenso2_batai_code':self.zenso2_batai_code,
            'zenso2_kehai_code':self.zenso2_kehai_code,
            'zenso2_racepace':self.zenso2_racepace,
            'zenso2_umapace':self.zenso2_umapace,
            'zenso2_ten_score':self.zenso2_ten_score,
            'zenso2_up_score':self.zenso2_up_score,
            'zenso2_pace_score':self.zenso2_pace_score,
            'zenso2_racep_score':self.zenso2_racep_score,
            'zenso2_time_sa':self.zenso2_time_sa,
            'zenso2_mae3f_time':self.zenso2_mae3f_time,
            'zenso2_agari3f_time':self.zenso2_agari3f_time,
            'zenso2_corner_order1':self.zenso2_corner_order1,
            'zenso2_corner_order2':self.zenso2_corner_order2,
            'zenso2_corner_order3':self.zenso2_corner_order3,
            'zenso2_corner_order4':self.zenso2_corner_order4,
            'zenso2_mae3f_sa':self.zenso2_mae3f_sa,
            'zenso2_agari3f_sa':self.zenso2_agari3f_sa,
            'zenso2_jockey_code':self.zenso2_jockey_code,
            'zenso2_trainer_code':self.zenso2_trainer_code,
            'zenso2_weight':self.zenso2_weight,
            'zenso2_weight_increase':self.zenso2_weight_increase,
            'zenso2_tenko':self.zenso2_tenko,
            'zenso2_course':self.zenso2_course,
            'zenso2_race_leg_type':self.zenso2_race_leg_type,
            'zenso2_race_pace_flow':self.zenso2_race_pace_flow,
            'zenso2_horse_pace_flow':self.zenso2_horse_pace_flow,
            'zenso2_corner4_course_position':self.zenso2_corner4_course_position,
            'zenso2_paceupposition':self.zenso2_paceupposition,
            'zenso3_bacode':self.zenso3_bacode,
            'zenso3_year':self.zenso3_year,
            'zenso3_kai':self.zenso3_kai,
            'zenso3_day':self.zenso3_day,
            'zenso3_raceno':self.zenso3_raceno,
            'zenso3_num':self.zenso3_num,
            'zenso3_distance':self.zenso3_distance,
            'zenso3_tdscode':self.zenso3_tdscode,
            'zenso3_right_left':self.zenso3_right_left,
            'zenso3_in_out':self.zenso3_in_out,
            'zenso3_':self.zenso3_baba,
            'zenso3_baba':self.zenso3_baba_abst,
            'zenso3_':self.zenso3_baba_detail,
            'zenso3_shubetsu':self.zenso3_shubetsu,
            'zenso3_joken':self.zenso3_joken,
            'zenso3_kigo':self.zenso3_kigo,
            'zenso3_juryo':self.zenso3_juryo,
            'zenso3_grade':self.zenso3_grade,
            'zenso3_num_of_all_horse':self.zenso3_num_of_all_horse,
            'zenso3_order':self.zenso3_order,
            'zenso3_ijo_kbn':self.zenso3_ijo_kbn,
            'zenso3_time':self.zenso3_time,
            'zenso3_kinryo':self.zenso3_kinryo,
            'zenso3_decided_odds':self.zenso3_decided_odds,
            'zenso3_decided_pop_order':self.zenso3_decided_pop_order,
            'zenso3_natural_score':self.zenso3_natural_score,
            'zenso3_baba_sa':self.zenso3_baba_sa,
            'zenso3_pace':self.zenso3_pace,
            'zenso3_start_late':self.zenso3_start_late,
            'zenso3_position':self.zenso3_position,
            'zenso3_furi':self.zenso3_furi,
            'zenso3_mae_furi':self.zenso3_mae_furi,
            'zenso3_naka_furi':self.zenso3_naka_furi,
            'zenso3_ushiro_furi':self.zenso3_ushiro_furi,
            'zenso3_race':self.zenso3_race,
            'zenso3_course_position':self.zenso3_course_position,
            'zenso3_up_code':self.zenso3_up_code,
            'zenso3_class_code':self.zenso3_class_code,
            'zenso3_batai_code':self.zenso3_batai_code,
            'zenso3_kehai_code':self.zenso3_kehai_code,
            'zenso3_racepace':self.zenso3_racepace,
            'zenso3_umapace':self.zenso3_umapace,
            'zenso3_ten_score':self.zenso3_ten_score,
            'zenso3_up_score':self.zenso3_up_score,
            'zenso3_pace_score':self.zenso3_pace_score,
            'zenso3_racep_score':self.zenso3_racep_score,
            'zenso3_time_sa':self.zenso3_time_sa,
            'zenso3_mae3f_time':self.zenso3_mae3f_time,
            'zenso3_agari3f_time':self.zenso3_agari3f_time,
            'zenso3_corner_order1':self.zenso3_corner_order1,
            'zenso3_corner_order2':self.zenso3_corner_order2,
            'zenso3_corner_order3':self.zenso3_corner_order3,
            'zenso3_corner_order4':self.zenso3_corner_order4,
            'zenso3_mae3f_sa':self.zenso3_mae3f_sa,
            'zenso3_agari3f_sa':self.zenso3_agari3f_sa,
            'zenso3_jockey_code':self.zenso3_jockey_code,
            'zenso3_trainer_code':self.zenso3_trainer_code,
            'zenso3_weight':self.zenso3_weight,
            'zenso3_weight_increase':self.zenso3_weight_increase,
            'zenso3_tenko':self.zenso3_tenko,
            'zenso3_course':self.zenso3_course,
            'zenso3_race_leg_type':self.zenso3_race_leg_type,
            'zenso3_race_pace_flow':self.zenso3_race_pace_flow,
            'zenso3_horse_pace_flow':self.zenso3_horse_pace_flow,
            'zenso3_corner4_course_position':self.zenso3_corner4_course_position,
            'zenso3_paceupposition':self.zenso3_paceupposition
        }

class HorseIndex(Base):
    __tablename__ = 'horseindex'
    blood = Column(Integer,ForeignKey('racehorse.blood'),primary_key = True)
    index = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'blood':self.blood,
            'index':self.index
        }

class JockeyIndex(Base):
    __tablename__ = 'jockeyindex'
    jockey_code = Column(Integer,ForeignKey('racehorse.jockey_code'),primary_key = True)
    index = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'jockey_code':self.jockey_code,
            'index':self.index
        }

class TrainerIndex(Base):
    __tablename__ = 'trainerindex'
    trainer_code = Column(Integer,ForeignKey('racehorse.trainer_code'),primary_key = True)
    index = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'trainer_code':self.trainer_code,
            'index':self.index
        }

class OikiriStateIndex(Base):
    __tablename__ = 'oikiristateindex'
    oikiri_state = Column(Integer,ForeignKey('train_oikiri.oikiri_state'),primary_key = True)
    index = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'oikiri_state':self.oikiri_state,
            'index':self.index
        }

class TrainCourseCodeIndex(Base):
    __tablename__ = 'traincoursecodeindex'
    train_course_code = Column(String,ForeignKey('train_oikiri.train_course_code'),primary_key = True)
    index = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'train_course_code':self.train_course_code,
            'index':self.index
        }

class HobokusakiIndex(Base):
    __tablename__ = 'hobokusakiindex'
    index = Column(Integer,primary_key = True)
    hobokusaki = Column(String,ForeignKey('racehorse.hobokusaki'))
    

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'index':self.index,
            'hobokusaki':self.hobokusaki
        }

class HidumeCodeIndex(Base):
    __tablename__ = 'hidumecodeindex'
    hidume_code = Column(Integer,ForeignKey('racehorse.hidume_code'),primary_key = True)
    index = Column(Integer)    

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'hidume_code':self.hidume_code,
            'index':self.index
        }

engine = create_engine('sqlite:///jrdb.db')
Base.metadata.create_all(engine)
