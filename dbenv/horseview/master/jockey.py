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


class JockeyData(baseobj):
    __tablename__ = "jockey"
    jockey_code = colobj(intobj, primary_key=True)
    delete_flg = colobj(intobj)
    delete_ymd = colobj(intobj)
    jockey_name = colobj(strobj)
    jockey_name_kana = colobj(strobj)
    jockey_name_short = colobj(strobj)
    shozoku_code = colobj(intobj)
    shozoku_region = colobj(strobj)
    birthday = colobj(intobj)
    get_licence_year = colobj(intobj)
    minarai_kbn = colobj(intobj)
    trainer_code = colobj(intobj)
    jockey_comment = colobj(strobj)
    comment_ymd = colobj(intobj)
    this_leading = colobj(intobj)
    this_flat_seiseki_1st = colobj(intobj)
    this_flat_seiseki_2nd = colobj(intobj)
    this_flat_seiseki_3rd = colobj(intobj)
    this_flat_seiseki_out = colobj(intobj)
    this_steeple_seiseki_1st = colobj(intobj)
    this_steeple_seiseki_2nd = colobj(intobj)
    this_steeple_seiseki_3rd = colobj(intobj)
    this_steeple_seiseki_out = colobj(intobj)
    this_tokubetsu_win = colobj(intobj)
    this_jusho_win = colobj(intobj)
    last_leading = colobj(intobj)
    last_flat_seiseki_1st = colobj(intobj)
    last_flat_seiseki_2nd = colobj(intobj)
    last_flat_seiseki_3rd = colobj(intobj)
    last_flat_seiseki_out = colobj(intobj)
    last_steeple_seiseki_1st = colobj(intobj)
    last_steeple_seiseki_2nd = colobj(intobj)
    last_steeple_seiseki_3rd = colobj(intobj)
    last_steeple_seiseki_out = colobj(intobj)
    last_tokubetsu_win = colobj(intobj)
    last_jusho_win = colobj(intobj)
    total_flat_seiseki_1st = colobj(intobj)
    total_flat_seiseki_2nd = colobj(intobj)
    total_flat_seiseki_3rd = colobj(intobj)
    total_flat_seiseki_out = colobj(intobj)
    total_steeple_seiseki_1st = colobj(intobj)
    total_steeple_seiseki_2nd = colobj(intobj)
    total_steeple_seiseki_3rd = colobj(intobj)
    total_steeple_seiseki_out = colobj(intobj)
    data_ymd = colobj(intobj)
    jockey_index = colobj(intobj)
