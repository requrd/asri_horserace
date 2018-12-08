from horseview.horsemodel import sesobj,SeisekiData
import sys,codecs

file = sys.argv[1]
print(file)

#ここからファイル操作
with codecs.open(file, "r", "shift_jisx0213") as f:
	for line in f:
		#line = line.replace(" ","0")
		racehorsekey=line[0:10]
		racekey=line[0:8]
		raceseisekikey=line[10:26]
		bacode=line[0:2]
		year=line[2:4]
		kai=line[4:5]
		day=line[5:6]
		raceno=line[6:8]
		num=line[8:10]
		blood=line[10:18]
		ymd=line[18:26]
		horse=line[26:44]
		distance=line[44:48]
		tdscode=line[48:49]
		right_left=line[49:50]
		in_out=line[50:51]
		baba=line[51:53]
		baba_abst=line[51:52]
		baba_detail=line[52:53]
		shubetsu=line[53:55]
		joken=line[55:57]
		kigo=line[57:60]
		juryo=line[60:61]
		grade=line[61:62].replace(" ","0")
		racename=line[62:87]
		num_of_all_horse=line[87:89]
		racename_ryaku=line[89:93]
		
		#レース名のズレ修正
		latter_half_line = line[93:]
		
		s1 = latter_half_line.find('0')
		s2 = latter_half_line.find('1')
		
		if s1 < s2 :
			s = s1
		else:
			s = s2
		
		latter_half_line = latter_half_line[s:]
		latter_half_line = latter_half_line.replace(" ","0")
		order_of_arrival=latter_half_line[0:2]
		ijo_kbn=latter_half_line[2:3]
		time=latter_half_line[3:7]
		kinryo=latter_half_line[7:10]
		jockey_name=latter_half_line[10:16]
		trainer_name=latter_half_line[16:22]
		decided_odds=latter_half_line[22:28]
		decided_pop_order=latter_half_line[28:30]
		idm=latter_half_line[30:33].replace("0-","-")
		natural_score=latter_half_line[33:36].replace("0-","-")
		baba_sa=latter_half_line[36:39].replace("0-","-")
		pace=latter_half_line[39:42].replace("0-","-")
		start_late=latter_half_line[42:45].replace("0-","-")
		position=latter_half_line[45:48].replace("0-","-")
		furi=latter_half_line[48:51].replace("0-","-")
		mae_furi=latter_half_line[51:54].replace("0-","-")
		naka_furi=latter_half_line[54:57].replace("0-","-")
		ushiro_furi=latter_half_line[57:60].replace("0-","-")
		race=latter_half_line[60:63].replace("0-","-")
		course_position=latter_half_line[63:64]
		up_code=latter_half_line[64:65]
		class_code=latter_half_line[65:67]
		batai_code=latter_half_line[67:68]
		kehai_code=latter_half_line[68:69]
		racepace=latter_half_line[69:70]
		umapace=latter_half_line[70:71]
		ten_score=latter_half_line[71:76].replace("0-","-")
		up_score=latter_half_line[76:81].replace("0-","-")
		pace_score=latter_half_line[81:86].replace("0-","-")
		racep_score=latter_half_line[86:91].replace("0-","-")
		win_horse_name=latter_half_line[91:97]
		time_sa=latter_half_line[97:100].replace("0-","-")
		mae3f_time=latter_half_line[100:103]
		agari3f_time=latter_half_line[103:106]
		
		#SEC読み込み用
		latter_half_line = latter_half_line.replace("　　　　　　000","000000000000000")
		#ここまで
		
		biko=latter_half_line[106:130]
		yobi=latter_half_line[130:132]
		decided_place_odds=latter_half_line[132:138]
		juji_win_odds=latter_half_line[138:144]
		juji_place_odds=latter_half_line[144:150]
		corner_order1=latter_half_line[150:152]
		corner_order2=latter_half_line[152:154]
		corner_order3=latter_half_line[154:156]
		corner_order4=latter_half_line[156:158]
		mae3f_sa=latter_half_line[158:161].replace("0-","-")
		agari3f_sa=latter_half_line[161:164].replace("0-","-")
		jockey_code=latter_half_line[164:169]
		trainer_code=latter_half_line[169:174]
		weight=latter_half_line[174:177]
		weight_increase=latter_half_line[177:180]
		tenko=latter_half_line[180:181]
		course=latter_half_line[181:182]
		race_leg_type=latter_half_line[182:183]
		win_ret=latter_half_line[183:190]
		place_ret=latter_half_line[190:197]
		this_money=latter_half_line[197:202]
		earned_money=latter_half_line[202:207]
		race_pace_flow=latter_half_line[207:209]
		horse_pace_flow=latter_half_line[209:211]
		corner4_course_position=latter_half_line[211:212]

		#ここからDB操作
		new_seiseki = SeisekiData(
			racehorsekey = racehorsekey,
			racekey = racekey,
			bacode=bacode,
			year=year,
			kai=kai,
			day=day,
			raceno=raceno,
			num=num,
			raceseisekikey=raceseisekikey,
			blood=blood,
			ymd=ymd,
			horse=horse,
			distance=distance,
			tdscode=tdscode,
			right_left=right_left,
			in_out=in_out,
			baba=baba,
			baba_abst=baba_abst,
			baba_detail=baba_detail,
			shubetsu=shubetsu,
			joken=joken,
			kigo=kigo,
			juryo=juryo,
			grade=grade,
			racename=racename,
			num_of_all_horse=num_of_all_horse,
			racename_ryaku=racename_ryaku,
			order_of_arrival=order_of_arrival,
			ijo_kbn=ijo_kbn,
			time=time,
			kinryo=kinryo,
			jockey_name=jockey_name,
			trainer_name=trainer_name,
			decided_odds=decided_odds,
			decided_pop_order=decided_pop_order,
			idm=idm,
			natural_score=natural_score,
			baba_sa=baba_sa,
			pace=pace,
			start_late=start_late,
			position=position,
			furi=furi,
			mae_furi=mae_furi,
			naka_furi=naka_furi,
			ushiro_furi=ushiro_furi,
			race=race,
			course_position=course_position,
			up_code=up_code,
			class_code=class_code,
			batai_code=batai_code,
			kehai_code=kehai_code,
			racepace=racepace,
			umapace=umapace,
			ten_score=ten_score,
			up_score=up_score,
			pace_score=pace_score,
			racep_score=racep_score,
			win_horse_name=win_horse_name,
			time_sa=time_sa,
			mae3f_time=mae3f_time,
			agari3f_time=agari3f_time,
			biko=biko,
			yobi=yobi,
			decided_place_odds=decided_place_odds,
			juji_win_odds=juji_win_odds,
			juji_place_odds=juji_place_odds,
			corner_order1=corner_order1,
			corner_order2=corner_order2,
			corner_order3=corner_order3,
			corner_order4=corner_order4,
			mae3f_sa=mae3f_sa,
			agari3f_sa=agari3f_sa,
			jockey_code=jockey_code,
			trainer_code=trainer_code,
			weight=weight,
			weight_increase=weight_increase,
			tenko=tenko,
			course=course,
			race_leg_type=race_leg_type,
			win_ret=win_ret,
			place_ret=place_ret,
			this_money=this_money,
			earned_money=earned_money,
			race_pace_flow=race_pace_flow,
			horse_pace_flow=horse_pace_flow,
			corner4_course_position=corner4_course_position
		)
		sesobj.add(new_seiseki)

sesobj.commit()
