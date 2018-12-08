from horseview.horsemodel import sesobj,TrainOikiriData
import sys,codecs

file = sys.argv[1]
print(file)

#ここからファイル操作
with codecs.open(file, "r", "shift_jisx0213") as f:
	for line in f:
		line = line.replace(" ","0")
		racehorsekey=line[0:10]
		racekey=line[0:8]
		num=line[8:10]
		day_of_week=line[10:11]
		train_date=line[11:19]
		kaisu=line[19:20]
		train_course_code=line[20:22]
		oikiri_kind=line[22:23]
		oikiri_state=line[23:25]
		rider=line[25:26]
		train_f=line[26:27]
		ten_f=line[27:30]
		mid_f=line[30:33]
		end_f=line[33:36]
		ten_f_score=line[36:39]
		mid_f_score=line[39:42]
		end_f_score=line[42:45]
		oikiri_score=line[45:48]
		awase_result=line[48:49]
		aite_oikiri_kind=line[49:50]
		aite_age=line[50:52]
		aite_class=line[52:54]

		#ここからDB操作
		new_oikiri = TrainOikiriData(
			racehorsekey=racehorsekey,
			racekey=racekey,
			num=num,
			day_of_week=day_of_week,
			train_date=train_date,
			kaisu=kaisu,
			train_course_code=train_course_code,
			oikiri_kind=oikiri_kind,
			oikiri_state=oikiri_state,
			rider=rider,
			train_f=train_f,
			ten_f=ten_f,
			mid_f=mid_f,
			end_f=end_f,
			ten_f_score=ten_f_score,
			mid_f_score=mid_f_score,
			end_f_score=end_f_score,
			oikiri_score=oikiri_score,
			awase_result=awase_result,
			aite_oikiri_kind=aite_oikiri_kind,
			aite_age=aite_age,
			aite_class=aite_class
		)
		sesobj.add(new_oikiri)

sesobj.commit()
