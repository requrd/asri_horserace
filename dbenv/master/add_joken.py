from sqlalchemy import create_engine
from database_setup import Base, JokenMaster,JokenGroupMaster,JuryoMaster,LegtypeMaster,DistanceadjustMaster,ShubetsuMaster, IjokbnMaster,TenkoMaster,RestreasoncodeMaster
from sqlalchemy.orm import sessionmaker

##ここからDB操作
engine = create_engine('sqlite:///jrdb.db')
Base.metadata.bind=engine
Session = sessionmaker(bind=engine)
session = Session()

#数が少ないため、直接追加
session.add(JokenMaster(joken = '01', joken_group = 1,joken_name = "400万下"))
session.add(JokenMaster(joken = '05', joken_group = 1,joken_name = "500万下"))
session.add(JokenMaster(joken = '08', joken_group = 2,joken_name = "800万下"))
session.add(JokenMaster(joken = '09', joken_group = 2,joken_name = "900万下"))
session.add(JokenMaster(joken = '10', joken_group = 2,joken_name = "1000万下"))
session.add(JokenMaster(joken = '15', joken_group = 3,joken_name = "1500万下"))
session.add(JokenMaster(joken = '16', joken_group = 3,joken_name = "1600万下"))
session.add(JokenMaster(joken = 'A1', joken_group = 0,joken_name = "新馬"))
session.add(JokenMaster(joken = 'A2', joken_group = 0,joken_name = "未出走"))
session.add(JokenMaster(joken = 'A3', joken_group = 0,joken_name = "未勝利"))
session.add(JokenMaster(joken = 'OP', joken_group = 9,joken_name = "オープン"))

session.add(JokenGroupMaster(joken_group = 1,joken_group_name = "1勝クラス"))
session.add(JokenGroupMaster(joken_group = 2,joken_group_name = "2勝クラス"))
session.add(JokenGroupMaster(joken_group = 3,joken_group_name = "準オープンクラス"))
session.add(JokenGroupMaster(joken_group = 0,joken_group_name = "未勝利クラス"))
session.add(JokenGroupMaster(joken_group = 9,joken_group_name = "オープンクラス"))

session.add(JuryoMaster(juryo = 1, juryo_name = "ハンデ"))
session.add(JuryoMaster(juryo = 2, juryo_name = "別定"))
session.add(JuryoMaster(juryo = 3, juryo_name = "馬齢"))
session.add(JuryoMaster(juryo = 4, juryo_name = "定量"))

session.add(LegtypeMaster(leg_type = 1, race_leg_type = '1',leg_type_name = "逃げ"))
session.add(LegtypeMaster(leg_type = 2, race_leg_type = '2',leg_type_name = "先行"))
session.add(LegtypeMaster(leg_type = 3, race_leg_type = '3',leg_type_name = "差し"))
session.add(LegtypeMaster(leg_type = 4, race_leg_type = '4',leg_type_name = "追込"))
session.add(LegtypeMaster(leg_type = 5, race_leg_type = '5',leg_type_name = "好意差し"))
session.add(LegtypeMaster(leg_type = 6, race_leg_type = '6',leg_type_name = "自在"))

session.add(DistanceadjustMaster(distance_adjust = 1, distance_name = "短距離"))
session.add(DistanceadjustMaster(distance_adjust = 2, distance_name = "中距離"))
session.add(DistanceadjustMaster(distance_adjust = 3, distance_name = "長距離"))
session.add(DistanceadjustMaster(distance_adjust = 5, distance_name = "哩（マイル）"))
session.add(DistanceadjustMaster(distance_adjust = 6, distance_name = "万能"))

session.add(ShubetsuMaster(shubetsu = 11, shubetsu_name = "２歳"))
session.add(ShubetsuMaster(shubetsu = 12, shubetsu_name = "３歳"))
session.add(ShubetsuMaster(shubetsu = 13, shubetsu_name = "３歳以上"))
session.add(ShubetsuMaster(shubetsu = 14, shubetsu_name = "４歳以上"))
session.add(ShubetsuMaster(shubetsu = 20, shubetsu_name = "障害"))
session.add(ShubetsuMaster(shubetsu = 99, shubetsu_name = "その他"))

session.add(IjokbnMaster(ijo_kbn = 0, ijo_kbn_name = "異常なし"))
session.add(IjokbnMaster(ijo_kbn = 1, ijo_kbn_name = "取消"))
session.add(IjokbnMaster(ijo_kbn = 2, ijo_kbn_name = "除外"))
session.add(IjokbnMaster(ijo_kbn = 3, ijo_kbn_name = "中止"))
session.add(IjokbnMaster(ijo_kbn = 4, ijo_kbn_name = "失格"))
session.add(IjokbnMaster(ijo_kbn = 5, ijo_kbn_name = "降着"))
session.add(IjokbnMaster(ijo_kbn = 6, ijo_kbn_name = "再騎乗"))

session.add(TenkoMaster(tenko = 1, tenko_name = "晴"))
session.add(TenkoMaster(tenko = 2, tenko_name = "曇"))
session.add(TenkoMaster(tenko = 3, tenko_name = "小雨"))
session.add(TenkoMaster(tenko = 4, tenko_name = "雨"))
session.add(TenkoMaster(tenko = 5, tenko_name = "小雪"))
session.add(TenkoMaster(tenko = 6, tenko_name = "雪"))

session.add(RestreasoncodeMaster(rest_reason_code = 1, rest_reason_name = "放牧"))
session.add(RestreasoncodeMaster(rest_reason_code = 2, rest_reason_name = "放牧(故障、骨折等)"))
session.add(RestreasoncodeMaster(rest_reason_code = 3, rest_reason_name = "放牧(不安、ソエ等)"))
session.add(RestreasoncodeMaster(rest_reason_code = 4, rest_reason_name = "放牧(病気)"))
session.add(RestreasoncodeMaster(rest_reason_code = 5, rest_reason_name = "放牧(再審査)"))
session.add(RestreasoncodeMaster(rest_reason_code = 6, rest_reason_name = "放牧(出走停止)"))
session.add(RestreasoncodeMaster(rest_reason_code = 7, rest_reason_name = "放牧(手術）"))
session.add(RestreasoncodeMaster(rest_reason_code = 11, rest_reason_name = "調整"))
session.add(RestreasoncodeMaster(rest_reason_code = 12, rest_reason_name = "調整(故障、骨折等)"))
session.add(RestreasoncodeMaster(rest_reason_code = 13, rest_reason_name = "調整(不安、ソエ等)"))
session.add(RestreasoncodeMaster(rest_reason_code = 14, rest_reason_name = "調整(病気)"))

session.commit()
