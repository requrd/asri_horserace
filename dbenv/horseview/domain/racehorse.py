from ..sessioncontroll import (
    baseobj,
    strobj,
    baseobj,
    intobj,
    colobj,
    relobj,
    fkyobj,
    bkrobj,
)


class RacehorseData(baseobj):
    __tablename__ = "racehorse"
    racehorsekey = colobj(strobj, fkyobj("seiseki.racehorsekey"), primary_key=True)
    # 親に対して
    racekey = colobj(strobj, fkyobj("bangumi.racekey"))
    # 1:1
    trainanalysis = relobj(
        "TrainAnalysisData", uselist=False, backref=bkrobj("racehorse"), innerjoin=True
    )
    trainoikiri = relobj(
        "TrainOikiriData", uselist=False, backref=bkrobj("racehorse"), innerjoin=True
    )
    horse_base = relobj(
        "HorsebaseData", uselist=False, backref=bkrobj("racehorse"), innerjoin=True
    )
    result = relobj(
        "SeisekiData", uselist=False, foreign_keys=[racehorsekey], innerjoin=False
    )
    predict = relobj(
        "PredictData", uselist=False, backref=bkrobj("racehorse"), innerjoin=False
    )
    # インデックスに対して
    horseidx = relobj("HorseIndex", uselist=False, backref=bkrobj("racehorse"))
    jockeyidx = relobj("JockeyIndex", uselist=False, backref=bkrobj("racehorse"))
    traineridx = relobj("TrainerIndex", uselist=False, backref=bkrobj("racehorse"))
    hobokusakiidx = relobj(
        "HobokusakiIndex", uselist=False, backref=bkrobj("racehorse")
    )
    bacode = colobj(intobj)

    year = colobj(intobj)
    kai = colobj(intobj)
    day = colobj(intobj)
    race = colobj(intobj)
    num = colobj(intobj)
    blood = colobj(intobj)
    horse = colobj(strobj)
    idm = colobj(intobj)
    jockey_score = colobj(intobj)
    info_score = colobj(intobj)
    yobi1 = colobj(strobj)
    yobi2 = colobj(strobj)
    yobi3 = colobj(strobj)
    sogo_score = colobj(intobj)
    leg_type = colobj(intobj)
    distance_adjust = colobj(intobj)
    up_degree = colobj(intobj)
    routin = colobj(intobj)
    cri_odds = colobj(intobj)
    cri_popular_order = colobj(intobj)
    cri_fukusho_odds = colobj(intobj)
    cri_fukusho_popluar_order = colobj(intobj)
    specific_info_1 = colobj(intobj)
    specific_info_2 = colobj(intobj)
    specific_info_3 = colobj(intobj)
    specific_info_4 = colobj(intobj)
    specific_info_5 = colobj(intobj)
    sogo_info_1 = colobj(intobj)
    sogo_info_2 = colobj(intobj)
    sogo_info_3 = colobj(intobj)
    sogo_info_4 = colobj(intobj)
    sogo_info_5 = colobj(intobj)
    pop_score = colobj(intobj)
    train_score = colobj(intobj)
    trainer_score = colobj(intobj)
    train_code = colobj(intobj)
    trainer_hyoka_code = colobj(intobj)
    jockey_rate_rentai = colobj(intobj)
    gekiso_score = colobj(intobj)
    hidume_code = colobj(intobj)
    hidume_shape = colobj(intobj)
    hidume_size = colobj(intobj)
    omotekisei_code = colobj(intobj)
    class_code = colobj(intobj)
    yobi4 = colobj(strobj)
    brinkers = colobj(strobj)
    jockey_name = colobj(strobj)
    kinryo = colobj(intobj)
    minarai = colobj(intobj)
    trainer_name = colobj(strobj)
    trainer_shozoku = colobj(strobj)
    zenso_seiseki_key_1 = colobj(strobj, fkyobj("seiseki.raceseisekikey"))
    zenso_seiseki_key_2 = colobj(strobj, fkyobj("seiseki.raceseisekikey"))
    zenso_seiseki_key_3 = colobj(strobj, fkyobj("seiseki.raceseisekikey"))
    zenso_seiseki_key_4 = colobj(strobj, fkyobj("seiseki.raceseisekikey"))
    zenso_seiseki_key_5 = colobj(strobj, fkyobj("seiseki.raceseisekikey"))

    zenso1 = relobj(
        "SeisekiData",
        uselist=False,
        foreign_keys=[zenso_seiseki_key_1],
        innerjoin=False,
    )
    zenso2 = relobj(
        "SeisekiData",
        uselist=False,
        foreign_keys=[zenso_seiseki_key_2],
        innerjoin=False,
    )
    zenso3 = relobj(
        "SeisekiData",
        uselist=False,
        foreign_keys=[zenso_seiseki_key_3],
        innerjoin=False,
    )
    zenso4 = relobj(
        "SeisekiData",
        uselist=False,
        foreign_keys=[zenso_seiseki_key_4],
        innerjoin=False,
    )
    zenso5 = relobj(
        "SeisekiData",
        uselist=False,
        foreign_keys=[zenso_seiseki_key_5],
        innerjoin=False,
    )

    zenso_racekey_1 = colobj(strobj)
    zenso_racekey_2 = colobj(strobj)
    zenso_racekey_3 = colobj(strobj)
    zenso_racekey_4 = colobj(strobj)
    zenso_racekey_5 = colobj(strobj)
    waku = colobj(intobj)
    yobi5 = colobj(strobj)
    sogo_shirushi = colobj(intobj)
    idm_shiruishi = colobj(intobj)
    info_shirushi = colobj(intobj)
    jockey_shirushi = colobj(intobj)
    trainer_shirushi = colobj(intobj)
    train_shirushi = colobj(intobj)
    gekiso_shirushi = colobj(intobj)
    turf_adjust_code = colobj(intobj)
    dart_adjust_code = colobj(intobj)
    jockey_code = colobj(intobj)
    trainer_code = colobj(intobj)
    yobi6 = colobj(strobj)
    kakutoku_money = colobj(intobj)
    shukaku_money = colobj(intobj)
    joken = colobj(intobj)
    ten_score = colobj(intobj)
    pace_score = colobj(intobj)
    up_score = colobj(intobj)
    position_score = colobj(intobj)
    pace_predict = colobj(strobj)
    dochu_order = colobj(intobj)
    dochu_sa = colobj(intobj)
    dochu_in_out = colobj(intobj)
    last_order = colobj(intobj)
    last_sa = colobj(intobj)
    last_in_out = colobj(intobj)
    order = colobj(intobj)
    sa = colobj(intobj)
    in_out = colobj(intobj)
    tenkai = colobj(strobj)
    distance_adjust2 = colobj(intobj)
    commit_weight = colobj(intobj)
    commit_weight_increase = colobj(intobj)
    torikeshi = colobj(intobj)
    sex = colobj(intobj)
    owner_name = colobj(strobj)
    banushikai_code = colobj(intobj)
    umakigo_code = colobj(intobj)
    gekiso_order = colobj(intobj)
    ls_score_order = colobj(intobj)
    ten_score_order = colobj(intobj)
    pace_score_order = colobj(intobj)
    up_score_order = colobj(intobj)
    position_score_order = colobj(intobj)
    expect_jokey_win_rate = colobj(intobj)
    expect_jokey_rentai_rate = colobj(intobj)
    yuso = colobj(strobj)
    soho = colobj(intobj)
    taikei_data = colobj(strobj)
    taikei = colobj(intobj)
    senaka = colobj(intobj)
    do = colobj(intobj)
    siri = colobj(intobj)
    tomo = colobj(intobj)
    harabukuro = colobj(intobj)
    head = colobj(intobj)
    neck = colobj(intobj)
    breast = colobj(intobj)
    shoulder = colobj(intobj)
    zencho = colobj(intobj)
    kocho = colobj(intobj)
    maehaba = colobj(intobj)
    ushirohaba = colobj(intobj)
    maetsunagi = colobj(intobj)
    ushirotsunagi = colobj(intobj)
    tail = colobj(intobj)
    furikata = colobj(intobj)
    taikei_sogo1 = colobj(intobj)
    taikei_sogo2 = colobj(intobj)
    taikei_sogo3 = colobj(intobj)
    umatokki1 = colobj(intobj)
    umatokki2 = colobj(intobj)
    umatokki3 = colobj(intobj)
    horse_start_score = colobj(intobj)
    horse_latestart_rate = colobj(intobj)
    sanko_zenso = colobj(intobj)
    sanko_zenso_jockey_code = colobj(strobj)
    mambaken_score = colobj(intobj)
    mambaken_shirushi = colobj(intobj)
    kokyu_flg = colobj(intobj)
    gekiso_type = colobj(strobj)
    rest_reason_code = colobj(intobj)
    flg = colobj(strobj)
    turf_dart_steeple_flg = colobj(intobj)
    distance_flg = colobj(intobj)
    class_flg = colobj(intobj)
    tenkyu_flg = colobj(intobj)
    kyosei_flg = colobj(intobj)
    norikae_flg = colobj(intobj)
    runtimes_first_train = colobj(intobj)
    date_first_train = colobj(intobj)
    days_after_first_train = colobj(intobj)
    hobokusaki = colobj(strobj)
    hobokusaki_rank = colobj(strobj)
    trainer_rank = colobj(intobj)
