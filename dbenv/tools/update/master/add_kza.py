from horseview.horsemodel import sesobj, JockeyData
import sys

file = sys.argv[1]
print(file)

# ここからファイル操作
with open(file, "r") as f:
    for line in f:
        jockey_code = line[0:5]
        delete_flg = line[5:6]
        delete_ymd = line[6:14]
        jockey_name = line[14:20]
        jockey_name_kana = line[20:35]
        jockey_name_short = line[35:38]
        shozoku_code = line[38:39]
        shozoku_region = line[39:41]
        birthday = line[41:49]
        get_licence_year = line[49:53]
        minarai_kbn = line[53:54]
        trainer_code = line[54:59]
        jockey_comment = line[59:79]
        comment_ymd = line[79:87]
        this_leading = line[87:90]
        this_flat_seiseki_1st = line[90:93]
        this_flat_seiseki_2nd = line[93:96]
        this_flat_seiseki_3rd = line[96:99]
        this_flat_seiseki_out = line[99:102]
        this_steeple_seiseki_1st = line[102:105]
        this_steeple_seiseki_2nd = line[105:108]
        this_steeple_seiseki_3rd = line[108:111]
        this_steeple_seiseki_out = line[111:114]
        this_tokubetsu_win = line[114:117]
        this_jusho_win = line[117:120]
        last_leading = line[120:123]
        last_flat_seiseki_1st = line[123:126]
        last_flat_seiseki_2nd = line[126:129]
        last_flat_seiseki_3rd = line[129:132]
        last_flat_seiseki_out = line[132:135]
        last_steeple_seiseki_1st = line[135:138]
        last_steeple_seiseki_2nd = line[138:141]
        last_steeple_seiseki_3rd = line[141:144]
        last_steeple_seiseki_out = line[144:147]
        last_tokubetsu_win = line[147:150]
        last_jusho_win = line[150:153]
        total_flat_seiseki_1st = line[153:158]
        total_flat_seiseki_2nd = line[158:163]
        total_flat_seiseki_3rd = line[163:168]
        total_flat_seiseki_out = line[168:173]
        total_steeple_seiseki_1st = line[173:178]
        total_steeple_seiseki_2nd = line[178:183]
        total_steeple_seiseki_3rd = line[183:188]
        total_steeple_seiseki_out = line[188:193]
        data_ymd = line[239:247]
        jockey_index = 0

        # ここからDB操作
        new_jockey = JockeyData(
            jockey_code=jockey_code,
            delete_flg=delete_flg,
            delete_ymd=delete_ymd,
            jockey_name=jockey_name,
            jockey_name_kana=jockey_name_kana,
            jockey_name_short=jockey_name_short,
            shozoku_code=shozoku_code,
            shozoku_region=shozoku_region,
            birthday=birthday,
            get_licence_year=get_licence_year,
            minarai_kbn=minarai_kbn,
            trainer_code=trainer_code,
            jockey_comment=jockey_comment,
            comment_ymd=comment_ymd,
            this_leading=this_leading,
            this_flat_seiseki_1st=this_flat_seiseki_1st,
            this_flat_seiseki_2nd=this_flat_seiseki_2nd,
            this_flat_seiseki_3rd=this_flat_seiseki_3rd,
            this_flat_seiseki_out=this_flat_seiseki_out,
            this_steeple_seiseki_1st=this_steeple_seiseki_1st,
            this_steeple_seiseki_2nd=this_steeple_seiseki_2nd,
            this_steeple_seiseki_3rd=this_steeple_seiseki_3rd,
            this_steeple_seiseki_out=this_steeple_seiseki_out,
            this_tokubetsu_win=this_tokubetsu_win,
            this_jusho_win=this_jusho_win,
            last_leading=last_leading,
            last_flat_seiseki_1st=last_flat_seiseki_1st,
            last_flat_seiseki_2nd=last_flat_seiseki_2nd,
            last_flat_seiseki_3rd=last_flat_seiseki_3rd,
            last_flat_seiseki_out=last_flat_seiseki_out,
            last_steeple_seiseki_1st=last_steeple_seiseki_1st,
            last_steeple_seiseki_2nd=last_steeple_seiseki_2nd,
            last_steeple_seiseki_3rd=last_steeple_seiseki_3rd,
            last_steeple_seiseki_out=last_steeple_seiseki_out,
            last_tokubetsu_win=last_tokubetsu_win,
            last_jusho_win=last_jusho_win,
            total_flat_seiseki_1st=total_flat_seiseki_1st,
            total_flat_seiseki_2nd=total_flat_seiseki_2nd,
            total_flat_seiseki_3rd=total_flat_seiseki_3rd,
            total_flat_seiseki_out=total_flat_seiseki_out,
            total_steeple_seiseki_1st=total_steeple_seiseki_1st,
            total_steeple_seiseki_2nd=total_steeple_seiseki_2nd,
            total_steeple_seiseki_3rd=total_steeple_seiseki_3rd,
            total_steeple_seiseki_out=total_steeple_seiseki_out,
            data_ymd=data_ymd,
            jockey_index=jockey_index,
        )
        sesobj.add(new_jockey)

sesobj.commit()
