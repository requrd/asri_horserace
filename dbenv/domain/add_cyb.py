from sqlalchemy import create_engine
from database_setup import Base, TrainAnalysisData
from sqlalchemy.orm import sessionmaker
import sys
import codecs

file = sys.argv[1]
print(file)

##ここからDB操作
engine = create_engine('sqlite:///jrdb.db')
Base.metadata.bind=engine
Session = sessionmaker(bind=engine)
session = Session()

#ここからファイル操作
with codecs.open(file, "r", "shift_jisx0213") as f:
	for line in f:
		line = line.encode("Shift-jis")
		racehorsekey=line[0:10].decode("Shift-jis")
		racekey=line[0:8].decode("Shift-jis")
		num=line[8:10].decode("Shift-jis")
		train_type=line[10:12].decode("Shift-jis")
		train_course_kind=line[12:13].decode("Shift-jis")
		saka=line[13:15].decode("Shift-jis")
		wood=line[15:17].decode("Shift-jis")
		dart=line[17:19].decode("Shift-jis")
		turf=line[19:21].decode("Shift-jis")
		pool=line[21:23].decode("Shift-jis")
		steeple=line[23:25].decode("Shift-jis")
		politruck=line[25:27].decode("Shift-jis")
		train_distance=line[27:28].decode("Shift-jis")
		train_juten=line[28:29].decode("Shift-jis")
		oikiri_score=line[29:32].decode("Shift-jis")
		
		if oikiri_score == '   ':
			oikiri_score = 0
		
		shiage_score=line[32:35].decode("Shift-jis")
		
		if shiage_score == '   ':
			shiage_score = 0
		
		train_vol_hyoka=line[35:36].decode("Shift-jis")
		shiage_score_change=line[36:37].decode("Shift-jis")
		train_comment=line[37:77].decode("Shift-jis")
		comment_date=line[77:85].decode("Shift-jis")
		train_hyoka=line[85:86].decode("Shift-jis")

		#ここからDB操作
		new_train = TrainAnalysisData(
			racehorsekey=racehorsekey,
			racekey=racekey,
			num=num,
			train_type=train_type,
			train_course_kind=train_course_kind,
			saka=saka,
			wood=wood,
			dart=dart,
			turf=turf,
			pool=pool,
			steeple=steeple,
			politruck=politruck,
			train_distance=train_distance,
			train_juten=train_juten,
			oikiri_score=oikiri_score,
			shiage_score=shiage_score,
			train_vol_hyoka=train_vol_hyoka,
			shiage_score_change=shiage_score_change,
			train_comment=train_comment,
			comment_date=comment_date,
			train_hyoka=train_hyoka
		)
		session.add(new_train)

session.commit()
