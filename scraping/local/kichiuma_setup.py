from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import numpy as np

Base = declarative_base()

class HorsePillar(Base):
    __tablename__ = 'horsepillar'
    
    racehorsekey = Column(String,primary_key=True)
    racekey = Column(String)
    
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
    racehorsekey = Column(String,primary_key=True)
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
    racehorsekey = Column(String,primary_key=True)
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
    racehorsekey = Column(String,primary_key=True)
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

engine = create_engine('sqlite:///kichiuma.db')
Base.metadata.create_all(engine)
