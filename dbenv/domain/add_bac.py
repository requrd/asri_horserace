from sqlalchemy import create_engine
from database_setup import Base, BangumiData
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
		racekey=line[0:8]
		kaisaikey=line[0:6]
		ymd=line[8:16]
		start_time=line[16:20]
		distance=line[20:24]
		tdscode=line[24:25]
		right_left=line[25:26]
		in_out=line[26:27]
		shubetsu=line[27:29]
		joken=line[29:31]
		kigo=line[31:34]
		horse_kind_joken = line[31:32]
		horse_sex_joken = line[32:33]
		inter_race_joken = line[33:34]
		juryo=line[34:35]
		grade=line[35:36]
		race_name=line[36:61]
		
		#ズレ対策
		after_line = line[61:]
		s = after_line
		n_start = s.find('第')
		n_end = s.find('回') - n_start
		if n_start < 0:
			kai = "　"
		else :
			if n_end < 0:
				n_end = 4
			kai = after_line[n_start:n_start+n_end+1]
			n_start = n_start + n_end
			s = after_line[n_start:]
			after_line = s
		
		w_start1 = s.find("0")
		w_start2 = s.find("1")
		if w_start1 > w_start2:
			n_start = w_start2
		else :
			n_start = w_start1
		
		ns = n_start
		num_of_all_horse = after_line[ns:ns+2]
		course=after_line[ns+2:ns+3]
		kaisai_kbn=after_line[ns+3:ns+4]
		race_name_short=after_line[ns+4:ns+8]
		race_name_9char=after_line[ns+8:ns+17]
		
		#レース名（短縮）ズレ対応
		import re
		regex = r' '
		pattern = re.compile(regex)
		matchObj = pattern.findall(race_name_9char)
		
		#if isinstance(matchObj,type(None)) == False:
		w_end = len(matchObj)
		if w_end >0:
			print("スペース位置:",w_end)
			ns = ns + w_end
			print("異常ファイル")
			race_name_9char=after_line[ns+8:ns+17]
		
		data_kbn=after_line[ns+17:ns+18]
		money1st=after_line[ns+18:ns+23]
		money2nd=after_line[ns+23:ns+28]
		money3rd=after_line[ns+28:ns+33]
		money4th=after_line[ns+33:ns+38]
		money5th=after_line[ns+38:ns+43]
		sannyu_money1st=after_line[ns+43:ns+48]
		sannyu_money2nd=after_line[ns+48:ns+53]
		sellflg_tansho=after_line[ns+53:ns+54]
		sellflg_fukusho=after_line[ns+54:ns+55]
		sellflg_wakuren=after_line[ns+55:ns+56]
		sellflg_umaren=after_line[ns+56:ns+57]
		sellflg_umatan=after_line[ns+57:ns+58]
		sellflg_wide=after_line[ns+58:ns+59]
		sellflg_sanrenpuku=after_line[ns+59:ns+60]
		sellflg_sanrentan=after_line[ns+60:ns+61]
		yobi=after_line[ns+61:ns+69]
		win5flg=after_line[ns+69:ns+70]

		#ここからDB操作
		new_bangumi = BangumiData(
			racekey=racekey,
			kaisaikey=kaisaikey,
			ymd=ymd,
			start_time=start_time,
			distance=distance,
			tdscode=tdscode,
			right_left=right_left,
			in_out=in_out,
			shubetsu=shubetsu,
			joken=joken,
			kigo=kigo,
			horse_kind_joken = horse_kind_joken,
			horse_sex_joken = horse_sex_joken,
			inter_race_joken = inter_race_joken,
			juryo=juryo,
			grade=grade,
			race_name=race_name,
			kai=kai,
			num_of_all_horse=num_of_all_horse,
			course=course,
			kaisai_kbn=kaisai_kbn,
			race_name_short=race_name_short,
			race_name_9char=race_name_9char,
			data_kbn=data_kbn,
			money1st=money1st,
			money2nd=money2nd,
			money3rd=money3rd,
			money4th=money4th,
			money5th=money5th,
			sannyu_money1st=sannyu_money1st,
			sannyu_money2nd=sannyu_money2nd,
			sellflg_tansho=sellflg_tansho,
			sellflg_fukusho=sellflg_fukusho,
			sellflg_wakuren=sellflg_wakuren,
			sellflg_umaren=sellflg_umaren,
			sellflg_umatan=sellflg_umatan,
			sellflg_wide=sellflg_wide,
			sellflg_sanrenpuku=sellflg_sanrenpuku,
			sellflg_sanrentan=sellflg_sanrentan,
			yobi=yobi,
			win5flg=win5flg
		)
		session.add(new_bangumi)

session.commit()
