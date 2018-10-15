from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import numpy as np

Base = declarative_base()

class HorsePillar(Base):
    __tablename__ = 'horsepillar'
    
    racehorsekey = Column(String,primary_key=True)
    racekey = Column(String,ForeignKey('bangumi.racekey'))
    speed = relationship("SpeedData",uselist=False,backref="racehorse",lazy='joined')
    speedrank = relationship("SpeedRankData",uselist=False,backref="racehorse",lazy='joined')
    recommend = relationship("RecommendData",uselist=False,backref="racehorse",lazy='joined')
    result = relationship("SeisekiData",uselist=False,backref="racehorse",lazy='joined')
    #馬情報
    num = Column(Integer)
    waku = Column(Integer)
    horse = Column(String)
    father = Column(String)
    mother = Column(String)
    motherfather = Column(String)
    hair = Column(String)
    sex = Column(String)
    age = Column(Integer)
    owner = Column(String)
    producer = Column(String)
    
    seiseki_all_icchaku = Column(Integer)
    seiseki_all_nichaku = Column(Integer)
    seiseki_all_sanchaku = Column(Integer)
    seiseki_all_chakugai = Column(Integer)
    seiseki_dart_left_icchaku = Column(Integer)
    seiseki_dart_left_nichaku = Column(Integer)
    seiseki_dart_left_sanchaku = Column(Integer)
    seiseki_dart_left_chakugai = Column(Integer)
    seiseki_dart_right_icchaku = Column(Integer)
    seiseki_dart_right_nichaku = Column(Integer)
    seiseki_dart_right_sanchaku = Column(Integer)
    seiseki_dart_right_chakugai = Column(Integer)
    seiseki_this_course_icchaku = Column(Integer)
    seiseki_this_course_nichaku = Column(Integer)
    seiseki_this_course_sanchaku = Column(Integer)
    seiseki_this_course_chakugai = Column(Integer)
    
    #騎手情報
    jockey_name = Column(String)
    jockey_shozoku = Column(String)
    jockey_seiseki_icchaku = Column(Integer)
    jockey_seiseki_nichaku = Column(Integer)
    jockey_seiseki_sanchaku = Column(Integer)
    jokcey_seiseki_chakugai = Column(Integer)
    
    trainer_name = Column(String)
    trainer_shozoku = Column(String)
    
    #前走情報
    zenso1_ymd=Column(String)
    zenso1_course_name=Column(String)
    zenso1_left_right=Column(String)
    zenso1_baba=Column(String)
    zenso1_race_name=Column(String)
    zenso1_distance=Column(Integer)
    zenso1_num_of_all_horse=Column(Integer)
    zenso1_waku=Column(Integer)
    zenso1_jockey_name=Column(String)
    zenso1_kinryo=Column(Integer)
    zenso1_weight=Column(Integer)
    zenso1_order_of_arrival=Column(Integer)
    zenso1_time=Column(Integer)
    zenso1_agari_3f=Column(Integer)
    zenso1_chakusa=Column(Integer)
    zenso1_corner1=Column(Integer)
    zenso1_corner2=Column(Integer)
    zenso1_corner3=Column(Integer)
    zenso1_corner4=Column(Integer)
    zenso1_win_horse=Column(String)

    zenso2_ymd=Column(String)
    zenso2_course_name=Column(String)
    zenso2_left_right=Column(String)
    zenso2_baba=Column(String)
    zenso2_race_name=Column(String)
    zenso2_distance=Column(Integer)
    zenso2_num_of_all_horse=Column(Integer)
    zenso2_waku=Column(Integer)
    zenso2_jockey_name=Column(String)
    zenso2_kinryo=Column(Integer)
    zenso2_weight=Column(Integer)
    zenso2_order_of_arrival=Column(Integer)
    zenso2_time=Column(Integer)
    zenso2_agari_3f=Column(Integer)
    zenso2_chakusa=Column(Integer)
    zenso2_corner1=Column(Integer)
    zenso2_corner2=Column(Integer)
    zenso2_corner3=Column(Integer)
    zenso2_corner4=Column(Integer)
    zenso2_win_horse=Column(String)

    zenso3_ymd=Column(String)
    zenso3_course_name=Column(String)
    zenso3_left_right=Column(String)
    zenso3_baba=Column(String)
    zenso3_race_name=Column(String)
    zenso3_distance=Column(Integer)
    zenso3_num_of_all_horse=Column(Integer)
    zenso3_waku=Column(Integer)
    zenso3_jockey_name=Column(String)
    zenso3_kinryo=Column(Integer)
    zenso3_weight=Column(Integer)
    zenso3_order_of_arrival=Column(Integer)
    zenso3_time=Column(Integer)
    zenso3_agari_3f=Column(Integer)
    zenso3_chakusa=Column(Integer)
    zenso3_corner1=Column(Integer)
    zenso3_corner2=Column(Integer)
    zenso3_corner3=Column(Integer)
    zenso3_corner4=Column(Integer)
    zenso3_win_horse=Column(String)

    zenso4_ymd=Column(String)
    zenso4_course_name=Column(String)
    zenso4_left_right=Column(String)
    zenso4_baba=Column(String)
    zenso4_race_name=Column(String)
    zenso4_distance=Column(Integer)
    zenso4_num_of_all_horse=Column(Integer)
    zenso4_waku=Column(Integer)
    zenso4_jockey_name=Column(String)
    zenso4_kinryo=Column(Integer)
    zenso4_weight=Column(Integer)
    zenso4_order_of_arrival=Column(Integer)
    zenso4_time=Column(Integer)
    zenso4_agari_3f=Column(Integer)
    zenso4_chakusa=Column(Integer)
    zenso4_corner1=Column(Integer)
    zenso4_corner2=Column(Integer)
    zenso4_corner3=Column(Integer)
    zenso4_corner4=Column(Integer)
    zenso4_win_horse=Column(String)

    zenso5_ymd=Column(String)
    zenso5_course_name=Column(String)
    zenso5_left_right=Column(String)
    zenso5_baba=Column(String)
    zenso5_race_name=Column(String)
    zenso5_distance=Column(Integer)
    zenso5_num_of_all_horse=Column(Integer)
    zenso5_waku=Column(Integer)
    zenso5_jockey_name=Column(String)
    zenso5_kinryo=Column(Integer)
    zenso5_weight=Column(Integer)
    zenso5_order_of_arrival=Column(Integer)
    zenso5_time=Column(Integer)
    zenso5_agari_3f=Column(Integer)
    zenso5_chakusa=Column(Integer)
    zenso5_corner1=Column(Integer)
    zenso5_corner2=Column(Integer)
    zenso5_corner3=Column(Integer)
    zenso5_corner4=Column(Integer)
    zenso5_win_horse=Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racehorsekey':self.racehorsekey,
            'racekey':self.rackey,
            'num':self.num ,
            'waku':self.waku,
            'horse':self.horse ,
            'father':self.father ,
            'mother':self.mother ,
            'motherfather':self.motherfather ,
            'hair':self.hair ,
            'sex':self.sex ,
            'age':self.age ,
            'owner':self.owner ,
            'producer':self.producer ,
            'seiseki_all_icchaku':self.seiseki_all_icchaku ,
            'seiseki_all_nichaku':self.seiseki_all_nichaku ,
            'seiseki_all_sanchaku':self.seiseki_all_sanchaku ,
            'seiseki_all_chakugai':self.seiseki_all_chakugai ,
            'seiseki_dart_left_icchaku':self.seiseki_dart_left_icchaku ,
            'seiseki_dart_left_nichaku':self.seiseki_dart_left_nichaku ,
            'seiseki_dart_left_sanchaku':self.seiseki_dart_left_sanchaku ,
            'seiseki_dart_left_chakugai':self.seiseki_dart_left_chakugai ,
            'seiseki_dart_right_icchaku':self.seiseki_dart_right_icchaku ,
            'seiseki_dart_right_nichaku':self.seiseki_dart_right_nichaku ,
            'seiseki_dart_right_sanchaku':self.seiseki_dart_right_sanchaku ,
            'seiseki_dart_right_chakugai':self.seiseki_dart_right_chakugai ,
            'seiseki_this_course_icchaku':self.seiseki_this_course_icchaku ,
            'seiseki_this_course_nichaku':self.seiseki_this_course_nichaku ,
            'seiseki_this_course_sanchaku':self.seiseki_this_course_sanchaku ,
            'seiseki_this_course_chakugai':self.seiseki_this_course_chakugai ,
            'jockey_name':self.jockey_name ,
            'jockey_shozoku':self.jockey_shozoku ,
            'jockey_seiseki_icchaku':self.jockey_seiseki_icchaku ,
            'jockey_seiseki_nichaku':self.jockey_seiseki_nichaku ,
            'jockey_seiseki_sanchaku':self.jockey_seiseki_sanchaku ,
            'jokcey_seiseki_chakugai':self.jokcey_seiseki_chakugai ,
            'trainer_name':self.trainer_name ,
            'trainer_shozoku':self.trainer_shozoku ,
            'zenso1_ymd':self.zenso1_ymd,
            'zenso1_course_name':self.zenso1_course_name,
            'zenso1_left_right':self.zenso1_left_right,
            'zenso1_baba':self.zenso1_baba,
            'zenso1_race_name':self.zenso1_race_name,
            'zenso1_distance':self.zenso1_distance,
            'zenso1_num_of_all_horse':self.zenso1_num_of_all_horse,
            'zenso1_waku':self.zenso1_waku,
            'zenso1_jockey_name':self.zenso1_jockey_name,
            'zenso1_kinryo':self.zenso1_kinryo,
            'zenso1_weight':self.zenso1_weight,
            'zenso1_order_of_arrival':self.zenso1_order_of_arrival,
            'zenso1_time':self.zenso1_time,
            'zenso1_agari_3f':self.zenso1_agari_3f,
            'zenso1_chakusa':self.zenso1_chakusa,
            'zenso1_corner1':self.zenso1_corner1,
            'zenso1_corner2':self.zenso1_corner2,
            'zenso1_corner3':self.zenso1_corner3,
            'zenso1_corner4':self.zenso1_corner4,
            'zenso1_win_horse':self.zenso1_win_horse,
            'zenso2_ymd':self.zenso2_ymd,
            'zenso2_course_name':self.zenso2_course_name,
            'zenso2_left_right':self.zenso2_left_right,
            'zenso2_baba':self.zenso2_baba,
            'zenso2_race_name':self.zenso2_race_name,
            'zenso2_distance':self.zenso2_distance,
            'zenso2_num_of_all_horse':self.zenso2_num_of_all_horse,
            'zenso2_waku':self.zenso2_waku,
            'zenso2_jockey_name':self.zenso2_jockey_name,
            'zenso2_kinryo':self.zenso2_kinryo,
            'zenso2_weight':self.zenso2_weight,
            'zenso2_order_of_arrival':self.zenso2_order_of_arrival,
            'zenso2_time':self.zenso2_time,
            'zenso2_agari_3f':self.zenso2_agari_3f,
            'zenso2_chakusa':self.zenso2_chakusa,
            'zenso2_corner1':self.zenso2_corner1,
            'zenso2_corner2':self.zenso2_corner2,
            'zenso2_corner3':self.zenso2_corner3,
            'zenso2_corner4':self.zenso2_corner4,
            'zenso2_win_horse':self.zenso2_win_horse,
            'zenso3_ymd':self.zenso3_ymd,
            'zenso3_course_name':self.zenso3_course_name,
            'zenso3_left_right':self.zenso3_left_right,
            'zenso3_baba':self.zenso3_baba,
            'zenso3_race_name':self.zenso3_race_name,
            'zenso3_distance':self.zenso3_distance,
            'zenso3_num_of_all_horse':self.zenso3_num_of_all_horse,
            'zenso3_waku':self.zenso3_waku,
            'zenso3_jockey_name':self.zenso3_jockey_name,
            'zenso3_kinryo':self.zenso3_kinryo,
            'zenso3_weight':self.zenso3_weight,
            'zenso3_order_of_arrival':self.zenso3_order_of_arrival,
            'zenso3_time':self.zenso3_time,
            'zenso3_agari_3f':self.zenso3_agari_3f,
            'zenso3_chakusa':self.zenso3_chakusa,
            'zenso3_corner1':self.zenso3_corner1,
            'zenso3_corner2':self.zenso3_corner2,
            'zenso3_corner3':self.zenso3_corner3,
            'zenso3_corner4':self.zenso3_corner4,
            'zenso3_win_horse':self.zenso3_win_horse,
            'zenso4_ymd':self.zenso4_ymd,
            'zenso4_course_name':self.zenso4_course_name,
            'zenso4_left_right':self.zenso4_left_right,
            'zenso4_baba':self.zenso4_baba,
            'zenso4_race_name':self.zenso4_race_name,
            'zenso4_distance':self.zenso4_distance,
            'zenso4_num_of_all_horse':self.zenso4_num_of_all_horse,
            'zenso4_waku':self.zenso4_waku,
            'zenso4_jockey_name':self.zenso4_jockey_name,
            'zenso4_kinryo':self.zenso4_kinryo,
            'zenso4_weight':self.zenso4_weight,
            'zenso4_order_of_arrival':self.zenso4_order_of_arrival,
            'zenso4_time':self.zenso4_time,
            'zenso4_agari_3f':self.zenso4_agari_3f,
            'zenso4_chakusa':self.zenso4_chakusa,
            'zenso4_corner1':self.zenso4_corner1,
            'zenso4_corner2':self.zenso4_corner2,
            'zenso4_corner3':self.zenso4_corner3,
            'zenso4_corner4':self.zenso4_corner4,
            'zenso4_win_horse':self.zenso4_win_horse,
            'zenso5_ymd':self.zenso5_ymd,
            'zenso5_course_name':self.zenso5_course_name,
            'zenso5_left_right':self.zenso5_left_right,
            'zenso5_baba':self.zenso5_baba,
            'zenso5_race_name':self.zenso5_race_name,
            'zenso5_distance':self.zenso5_distance,
            'zenso5_num_of_all_horse':self.zenso5_num_of_all_horse,
            'zenso5_waku':self.zenso5_waku,
            'zenso5_jockey_name':self.zenso5_jockey_name,
            'zenso5_kinryo':self.zenso5_kinryo,
            'zenso5_weight':self.zenso5_weight,
            'zenso5_order_of_arrival':self.zenso5_order_of_arrival,
            'zenso5_time':self.zenso5_time,
            'zenso5_agari_3f':self.zenso5_agari_3f,
            'zenso5_chakusa':self.zenso5_chakusa,
            'zenso5_corner1':self.zenso5_corner1,
            'zenso5_corner2':self.zenso5_corner2,
            'zenso5_corner3':self.zenso5_corner3,
            'zenso5_corner4':self.zenso5_corner4,
            'zenso5_win_horse':self.zenso5_win_horse
        }


class BangumiData(Base):
    __tablename__ = 'bangumi'
    racekey = Column(String,primary_key=True)
    racehorses = relationship("HorsePillar",backref="race",lazy='subquery')
    returninfo = relationship("Returninfo",uselist=False,backref="race",lazy='subquery')
    #レース情報
    ymd = Column(String)
    course_code = Column(Integer)
    course_name = Column(String)
    race_num = Column(String)
    race_name = Column(String)
    left_right = Column(String)
    distance = Column(Integer)
    start_time = Column(String)
    prize1 = Column(Integer)
    prize2 = Column(Integer)
    prize3 = Column(Integer)
    prize4 = Column(Integer)
    prize5 = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racekey':self.rackey,
            'ymd':self.ymd ,
            'course_code':self.course_code,
            'course_name':self.course_name ,
            'race_num':self.race_num ,
            'race_name':self.race_name ,
            'left_right':self.left_right ,
            'distance':self.distance ,
            'start_time':self.start_time ,
            'prize1':self.prize1 ,
            'prize2':self.prize2 ,
            'prize3':self.prize3 ,
            'prize4':self.prize4 ,
            'prize5':self.prize5
        }

class SpeedData(Base):
    __tablename__ = 'speed'
    racehorsekey = Column(String,ForeignKey('horsepillar.racehorsekey'),primary_key=True)
    sp_mod = Column(Integer)
    sp_mod_mark = Column(String)
    sp_mean = Column(Integer)
    sp_mean_mark = Column(String)
    sp_max = Column(Integer)
    sp_max_mark = Column(String)
    zenso1_speed_score = Column(Integer)
    zenso1_senko_score = Column(Integer)
    zenso1_agari_score = Column(Integer)
    zenso2_speed_score = Column(Integer)
    zenso2_senko_score = Column(Integer)
    zenso2_agari_score = Column(Integer)
    zenso3_speed_score = Column(Integer)
    zenso3_senko_score = Column(Integer)
    zenso3_agari_score = Column(Integer)
    zenso4_speed_score = Column(Integer)
    zenso4_senko_score = Column(Integer)
    zenso4_agari_score = Column(Integer)
    zenso5_speed_score = Column(Integer)
    zenso5_senko_score = Column(Integer)
    zenso5_agari_score = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racehorsekey':self.racehorsekey,
            'sp_mod':self.sp_mod,
            'sp_mod_mark':self.sp_mod_mark,
            'sp_mean':self.sp_mean,
            'sp_mean_mark':self.sp_mean_mark,
            'sp_max':self.sp_max,
            'sp_max_mark':self.sp_max_mark,
            'zenso1_speed_score':self.zenso1_speed_score,
            'zenso1_senko_score':self.zenso1_senko_score,
            'zenso1_agari_score':self.zenso1_agari_score,
            'zenso2_speed_score':self.zenso2_speed_score,
            'zenso2_senko_score':self.zenso2_senko_score,
            'zenso2_agari_score':self.zenso2_agari_score,
            'zenso3_speed_score':self.zenso3_speed_score,
            'zenso3_senko_score':self.zenso3_senko_score,
            'zenso3_agari_score':self.zenso3_agari_score,
            'zenso4_speed_score':self.zenso4_speed_score,
            'zenso4_senko_score':self.zenso4_senko_score,
            'zenso4_agari_score':self.zenso4_agari_score,
            'zenso5_speed_score':self.zenso5_speed_score,
            'zenso5_senko_score':self.zenso5_senko_score,
            'zenso5_agari_score':self.zenso5_agari_score
        }

class SpeedRankData(Base):
    __tablename__ = 'speedrank'
    racehorsekey = Column(String,ForeignKey('horsepillar.racehorsekey'),primary_key=True)
    zenso_rank = Column(String)
    kakoso_rank = Column(String)
    zenso1_sp = Column(Integer)
    zenso2_sp = Column(Integer)
    zenso3_sp = Column(Integer)
    zenso4_sp = Column(Integer)
    zenso5_sp = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racehorsekey':self.racehorsekey,
            'zenso_rank':zenso_rank,
            'kakoso_rank':self.kakoso_rank,
            'zenso1_sp':self.zenso1_sp,
            'zenso2_sp':self.zenso2_sp,
            'zenso3_sp':self.zenso3_sp,
            'zenso4_sp':self.zenso4_sp,
            'zenso5_sp':self.zenso5_sp
        }

class RecommendData(Base):
    __tablename__ = 'recommend'
    racehorsekey = Column(String,ForeignKey('horsepillar.racehorsekey'),primary_key=True)
    hyoka = Column(String)
    sp = Column(Integer)
    senko_score = Column(Integer)
    sp_credit = Column(Integer)
    sp_credit_mark = Column(String)
    sp_mod = Column(Integer)
    sp_mod_mark = Column(String)
    sp_max = Column(Integer)
    sp_max_mark = Column(String)
    last_leg_power = Column(Integer)
    last_leg_power_mark = Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racehorsekey':self.racehorsekey,
            'hyoka':self.hyoka,
            'sp':self.sp,
            'senko_score':self.senko_score,
            'sp_credit':self.sp_credit,
            'sp_credit_mark':self.sp_credit_mark,
            'sp_mod':self.sp_mod,
            'sp_mod_mark':self.sp_mod_mark,
            'last_leg_power':self.last_leg_power,
            'last_leg_power_mark':self.last_leg_power_mark
        }

class SeisekiData(Base):
    __tablename__ = 'seiseki'
    racehorsekey = Column(String,ForeignKey('horsepillar.racehorsekey'),primary_key=True)
    num = Column(Integer)
    waku = Column(Integer)
    lineage_login_code = Column(Integer) 
    order_of_arrival = Column(Integer)
    kinryo = Column(Integer)
    jockey_license_no = Column(Integer)
    jockey_name = Column(String)
    trainer_license_no = Column(Integer)
    trainer_name = Column(String)
    weight = Column(Integer)
    weight_increase = Column(Integer)
    time_m = Column(Integer)
    time_s = Column(Integer)
    chakusa = Column(String)
    agari_3f = Column(Integer)
    pop_order = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racehorsekey':self.racehorsekey,
            'num':self.num,
            'waku':self.waku,
            'lineage_login_code':self.lineage_login_code,
            'order_of_arrival':self.order_of_arrival,
            'kinryo':self.kinryo,
            'jockey_license_no':self.jockey_license_no,
            'jockey_name':self.jockey_name,
            'trainer_name':self.trainer_name,
            'weight':self.weight,
            'time_m':self.time_m,
            'time_s':self.time_s,
            'chakusa':self.chakusa,
            'agari_3f':self.agari_3f,
            'pop_order':self.pop_order
        }

class Returninfo(Base):
    __tablename__ = 'returninfo'
    racekey = Column(String,ForeignKey('bangumi.racekey'),primary_key=True)
    win1_num = Column(Integer)
    win1_ret = Column(Integer)
    win1_pop = Column(Integer)
    win2_num = Column(Integer)
    win2_ret = Column(Integer)
    win2_pop = Column(Integer)
    win3_num = Column(Integer)
    win3_ret = Column(Integer)
    win3_pop = Column(Integer)

    place1_num = Column(Integer)
    place1_ret = Column(Integer)
    place1_pop = Column(Integer)
    place2_num = Column(Integer)
    place2_ret = Column(Integer)
    place2_pop = Column(Integer)
    place3_num = Column(Integer)
    place3_ret = Column(Integer)
    place3_pop = Column(Integer)
    place4_num = Column(Integer)
    place4_ret = Column(Integer)
    place4_pop = Column(Integer)
    place5_num = Column(Integer)
    place5_ret = Column(Integer)
    place5_pop = Column(Integer)
    place6_num = Column(Integer)
    place6_ret = Column(Integer)
    place6_pop = Column(Integer)

    wakuren1_num1 = Column(Integer)
    wakuren1_num2 = Column(Integer)
    wakuren1_ret = Column(Integer)
    wakuren1_pop = Column(Integer)
    wakuren2_num1 = Column(Integer)
    wakuren2_num2 = Column(Integer)
    wakuren2_ret = Column(Integer)
    wakuren2_pop = Column(Integer)
    wakuren3_num1 = Column(Integer)
    wakuren3_num2 = Column(Integer)
    wakuren3_ret = Column(Integer)
    wakuren3_pop = Column(Integer)

    umaren1_num1 = Column(Integer)
    umaren1_num2 = Column(Integer)
    umaren1_ret = Column(Integer)
    umaren1_pop = Column(Integer)
    umaren2_num1 = Column(Integer)
    umaren2_num2 = Column(Integer)
    umaren2_ret = Column(Integer)
    umaren2_pop = Column(Integer)
    umaren3_num1 = Column(Integer)
    umaren3_num2 = Column(Integer)
    umaren3_ret = Column(Integer)
    umaren3_pop = Column(Integer)

    wide1_num1 = Column(Integer)
    wide1_num2 = Column(Integer)
    wide1_ret = Column(Integer)
    wide1_pop = Column(Integer)
    wide2_num1 = Column(Integer)
    wide2_num2 = Column(Integer)
    wide2_ret = Column(Integer)
    wide2_pop = Column(Integer)
    wide3_num1 = Column(Integer)
    wide3_num2 = Column(Integer)
    wide3_ret = Column(Integer)
    wide3_pop = Column(Integer)
    wide4_num1 = Column(Integer)
    wide4_num2 = Column(Integer)
    wide4_ret = Column(Integer)
    wide4_pop = Column(Integer)
    wide5_num1 = Column(Integer)
    wide5_num2 = Column(Integer)
    wide5_ret = Column(Integer)
    wide5_pop = Column(Integer)
    wide6_num1 = Column(Integer)
    wide6_num2 = Column(Integer)
    wide6_ret = Column(Integer)
    wide6_pop = Column(Integer)
    wide7_num1 = Column(Integer)
    wide7_num2 = Column(Integer)
    wide7_ret = Column(Integer)
    wide7_pop = Column(Integer)

    wakutan1_num1 = Column(Integer)
    wakutan1_num2 = Column(Integer)
    wakutan1_ret = Column(Integer)
    wakutan1_pop = Column(Integer)
    wakutan2_num1 = Column(Integer)
    wakutan2_num2 = Column(Integer)
    wakutan2_ret = Column(Integer)
    wakutan2_pop = Column(Integer)
    wakutan3_num1 = Column(Integer)
    wakutan3_num2 = Column(Integer)
    wakutan3_ret = Column(Integer)
    wakutan3_pop = Column(Integer)

    umatan1_num1 = Column(Integer)
    umatan1_num2 = Column(Integer)
    umatan1_ret = Column(Integer)
    umatan1_pop = Column(Integer)
    umatan2_num1 = Column(Integer)
    umatan2_num2 = Column(Integer)
    umatan2_ret = Column(Integer)
    umatan2_pop = Column(Integer)
    umatan3_num1 = Column(Integer)
    umatan3_num2 = Column(Integer)
    umatan3_ret = Column(Integer)
    umatan3_pop = Column(Integer)

    sanrenpuku1_num1 = Column(Integer)
    sanrenpuku1_num2 = Column(Integer)
    sanrenpuku1_num3 = Column(Integer)
    sanrenpuku1_ret = Column(Integer)
    sanrenpuku1_pop = Column(Integer)
    sanrenpuku2_num1 = Column(Integer)
    sanrenpuku2_num2 = Column(Integer)
    sanrenpuku2_num3 = Column(Integer)
    sanrenpuku2_ret = Column(Integer)
    sanrenpuku2_pop = Column(Integer)
    sanrenpuku3_num1 = Column(Integer)
    sanrenpuku3_num2 = Column(Integer)
    sanrenpuku3_num3 = Column(Integer)
    sanrenpuku3_ret = Column(Integer)
    sanrenpuku3_pop = Column(Integer)

    sanrentan1_num1 = Column(Integer)
    sanrentan1_num2 = Column(Integer)
    sanrentan1_num3 = Column(Integer)
    sanrentan1_ret = Column(Integer)
    sanrentan1_pop = Column(Integer)
    sanrentan2_num1 = Column(Integer)
    sanrentan2_num2 = Column(Integer)
    sanrentan2_num3 = Column(Integer)
    sanrentan2_ret = Column(Integer)
    sanrentan2_pop = Column(Integer)
    sanrentan3_num1 = Column(Integer)
    sanrentan3_num2 = Column(Integer)
    sanrentan3_num3 = Column(Integer)
    sanrentan3_ret = Column(Integer)
    sanrentan3_pop = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'racekey':self.racekey,
            'win1_ret':self.win1_num,
            'win1_ret':self.win1_ret,
            'win1_pop':self.win1_pop,
            'win2_num':self.win2_num,
            'win2_ret':self.win2_ret,
            'win2_pop':self.win2_pop,
            'win3_num':self.win3_num,
            'win3_ret':self.win3_ret,
            'win3_pop':self.win3_pop,
            'place1_num':self.place1_num,
            'place1_ret':self.place1_ret,
            'place1_pop':self.place1_pop,
            'place2_num':self.place2_num,
            'place2_ret':self.place2_ret,
            'place2_pop':self.place2_pop,
            'place3_num':self.place3_num,
            'place3_ret':self.place3_ret,
            'place3_pop':self.place3_pop,
            'place4_num':self.place4_num,
            'place4_ret':self.place4_ret,
            'place4_pop':self.place4_pop,
            'place5_num':self.place5_num,
            'place5_ret':self.place5_ret,
            'place5_pop':self.place5_pop,
            'place6_num':self.place6_num,
            'place6_ret':self.place6_ret,
            'place6_pop':self.place6_pop,
            'wakuren1_num1':self.wakuren1_num1,
            'wakuren1_num2':self.wakuren1_num2,
            'wakuren1_ret':self.wakuren1_ret,
            'wakuren1_pop':self.wakuren1_pop,
            'wakuren2_num1':self.wakuren2_num1,
            'wakuren2_num2':self.wakuren2_num2,
            'wakuren2_ret':self.wakuren2_ret,
            'wakuren2_pop':self.wakuren2_pop,
            'wakuren3_num1':self.wakuren3_num1,
            'wakuren3_num2':self.wakuren3_num2,
            'wakuren3_ret':self.wakuren3_ret,
            'wakuren3_pop':self.wakuren3_pop,
            'umaren1_num1':self.umaren1_num1,
            'umaren1_num2':self.umaren1_num2,
            'umaren1_ret':self.umaren1_ret,
            'umaren1_pop':self.umaren1_pop,
            'umaren2_num1':self.umaren2_num1,
            'umaren2_num2':self.umaren2_num2,
            'umaren2_ret':self.umaren2_ret,
            'umaren2_pop':self.umaren2_pop,
            'umaren3_num1':self.umaren3_num1,
            'umaren3_num2':self.umaren3_num2,
            'umaren3_ret':self.umaren3_ret,
            'umaren3_pop':self.umaren3_pop,
            'wide1_num1':self.wide1_num1,
            'wide1_num2':self.wide1_num2,
            'wide1_ret':self.wide1_ret,
            'wide1_pop':self.wide1_pop,
            'wide2_num1':self.wide2_num1,
            'wide2_num2':self.wide2_num2,
            'wide2_ret':self.wide2_ret,
            'wide2_pop':self.wide2_pop,
            'wide3_num1':self.wide3_num1,
            'wide3_num2':self.wide3_num2,
            'wide3_ret':self.wide3_ret,
            'wide3_pop':self.wide3_pop,
            'wide4_num1':self.wide4_num1,
            'wide4_num2':self.wide4_num2,
            'wide4_ret':self.wide4_ret,
            'wide4_pop':self.wide4_pop,
            'wide5_num1':self.wide5_num1,
            'wide5_num2':self.wide5_num2,
            'wide5_ret':self.wide5_ret,
            'wide5_pop':self.wide5_pop,
            'wide6_num1':self.wide6_num1,
            'wide6_num2':self.wide6_num2,
            'wide6_ret':self.wide6_ret,
            'wide6_pop':self.wide6_pop,
            'wide7_num1':self.wide7_num1,
            'wide7_num2':self.wide7_num2,
            'wide7_ret':self.wide7_ret,
            'wide7_pop':self.wide7_pop,
            'wakutan1_num1':self.wakutan1_num1,
            'wakutan1_num2':self.wakutan1_num2,
            'wakutan1_ret':self.wakutan1_ret,
            'wakutan1_pop':self.wakutan1_pop,
            'wakutan2_num1':self.wakutan2_num1,
            'wakutan2_num2':self.wakutan2_num2,
            'wakutan2_ret':self.wakutan2_ret,
            'wakutan2_pop':self.wakutan2_pop,
            'wakutan3_num1':self.wakutan3_num1,
            'wakutan3_num2':self.wakutan3_num2,
            'wakutan3_ret':self.wakutan3_ret,
            'wakutan3_pop':self.wakutan3_pop,
            'umatan1_num1':self.umatan1_num1,
            'umatan1_num2':self.umatan1_num2,
            'umatan1_ret':self.umatan1_ret,
            'umatan1_pop':self.umatan1_pop,
            'umatan2_num1':self.umatan2_num1,
            'umatan2_num2':self.umatan2_num2,
            'umatan2_ret':self.umatan2_ret,
            'umatan2_pop':self.umatan2_pop,
            'umatan3_num1':self.umatan3_num1,
            'umatan3_num2':self.umatan3_num2,
            'umatan3_ret':self.umatan3_ret,
            'umatan3_pop':self.umatan3_pop,
            'sanrenpuku1_num1':self.sanrenpuku1_num1,
            'sanrenpuku1_num2':self.sanrenpuku1_num2,
            'sanrenpuku1_num3':self.sanrenpuku1_num3,
            'sanrenpuku1_ret':self.sanrenpuku1_ret,
            'sanrenpuku1_pop':self.sanrenpuku1_pop,
            'sanrenpuku2_num1':self.sanrenpuku2_num1,
            'sanrenpuku2_num2':self.sanrenpuku2_num2,
            'sanrenpuku2_num3':self.sanrenpuku2_num3,
            'sanrenpuku2_ret':self.sanrenpuku2_ret,
            'sanrenpuku2_pop':self.sanrenpuku2_pop,
            'sanrenpuku3_num1':self.sanrenpuku3_num1,
            'sanrenpuku3_num2':self.sanrenpuku3_num2,
            'sanrenpuku3_num3':self.sanrenpuku3_num3,
            'sanrenpuku3_ret':self.sanrenpuku3_ret,
            'sanrenpuku3_pop':self.sanrenpuku3_pop,
            'sanrentan1_num1':self.sanrentan1_num1,
            'sanrentan1_num2':self.sanrentan1_num2,
            'sanrentan1_num3':self.sanrentan1_num3,
            'sanrentan1_ret':self.sanrentan1_ret,
            'sanrentan1_pop':self.sanrentan1_pop,
            'sanrentan2_num1':self.sanrentan2_num1,
            'sanrentan2_num2':self.sanrentan2_num2,
            'sanrentan2_num3':self.sanrentan2_num3,
            'sanrentan2_ret':self.sanrentan2_ret,
            'sanrentan2_pop':self.sanrentan2_pop,
            'sanrentan3_num1':self.sanrentan3_num1,
            'sanrentan3_num2':self.sanrentan3_num2,
            'sanrentan3_num3':self.sanrentan3_num3,
            'sanrentan3_ret':self.sanrentan3_ret,
            'sanrentan3_pop':self.sanrentan3_pop
        }

engine = create_engine('sqlite:///kichiuma.db')
Base.metadata.create_all(engine)
