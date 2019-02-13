from horseview.horsemodel import sesobj, KaisaiData
import sys, codecs

file = sys.argv[1]
print(file)

# ここからファイル操作
with codecs.open(file, "r", "shift_jisx0213") as f:
    for line in f:
        line = line.replace(" ", "0")
        kaisaikey = line[0:6]
        ymd = line[6:14]
        kaisai_kbn = line[14:15]
        day_of_week = line[15:16]
        course_name = line[16:18]
        tenko = line[18:19]
        turf_baba = line[19:21]
        turf_baba_abst = line[19:20]
        turf_baba_detail = line[20:21]
        turf_baba_in = line[21:22]
        turf_baba_center = line[22:23]
        turf_baba_out = line[23:24]
        turf_baba_sa = line[24:27]
        turf_baba_straight_saiuchi = line[27:29]
        turf_baba_straight_in = line[29:31]
        turf_baba_straight_center = line[31:33]
        turf_baba_straight_out = line[33:35]
        turf_baba_straight_oosoto = line[35:37]
        dart_baba = line[37:39]
        dart_baba_abst = line[37:38]
        dart_baba_detail = line[38:39]
        dart_baba_in = line[39:40]
        dart_baba_center = line[40:41]
        dart_baba_out = line[41:42]
        dart_baba_sa = line[42:45]
        data_kbn = line[45:46]
        renzoku_day = line[46:48]
        turf_kind = line[48:49]
        turf_length = line[49:53]
        tennatsu = line[53:54]
        stopfreeze = line[54:55]
        precipitation = line[55:60]

        # ここからDB操作
        new_kaisai = KaisaiData(
            kaisaikey=kaisaikey,
            ymd=ymd,
            kaisai_kbn=kaisai_kbn,
            day_of_week=day_of_week,
            course_name=course_name,
            tenko=tenko,
            turf_baba=turf_baba,
            turf_baba_abst=turf_baba_abst,
            turf_baba_detail=turf_baba_detail,
            turf_baba_in=turf_baba_in,
            turf_baba_center=turf_baba_center,
            turf_baba_out=turf_baba_out,
            turf_baba_sa=turf_baba_sa,
            turf_baba_straight_saiuchi=turf_baba_straight_saiuchi,
            turf_baba_straight_in=turf_baba_straight_in,
            turf_baba_straight_center=turf_baba_straight_center,
            turf_baba_straight_out=turf_baba_straight_out,
            turf_baba_straight_oosoto=turf_baba_straight_oosoto,
            dart_baba=dart_baba,
            dart_baba_abst=dart_baba_abst,
            dart_baba_detail=dart_baba_detail,
            dart_baba_in=dart_baba_in,
            dart_baba_center=dart_baba_center,
            dart_baba_out=dart_baba_out,
            dart_baba_sa=dart_baba_sa,
            data_kbn=data_kbn,
            renzoku_day=renzoku_day,
            turf_kind=turf_kind,
            turf_length=turf_length,
            tennatsu=tennatsu,
            stopfreeze=stopfreeze,
            precipitation=precipitation,
        )
        sesobj.add(new_kaisai)

sesobj.commit()
