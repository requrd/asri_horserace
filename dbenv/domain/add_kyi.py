﻿from sqlalchemy import create_engine
from database_setup import Base, RacehorseData
from sqlalchemy.orm import sessionmaker
import sys

file = sys.argv[1]
print(file)

##ここからDB操作
engine = create_engine('sqlite:///jrdb.db')
Base.metadata.bind=engine
Session = sessionmaker(bind=engine)
session = Session()

#ここからファイル操作
with open(file, 'r') as f:
	for line in f:
		line = line.replace(" ","0")
		racehorsekey = line[0:10]
		racekey = line[0:8]
		bacode = line[0:2]
		year = line[2:4]
		kai = line[4:5]
		day = line[5:6]
		race = line[6:8]
		num=line[8:10]
		blood=line[10:18]
		horse=line[18:36]
		idm=line[36:41].replace("0-","-")
		jockey_score=line[41:46].replace("0-","-")
		info_score=line[46:51].replace("0-","-")
		yobi1=line[51:56]
		yobi2=line[56:61]
		yobi3=line[61:66]
		sogo_score=line[66:71].replace("0-","-")
		leg_type=line[71:72]
		distance_adjust=line[72:73]
		up_degree=line[73:74]
		routin=line[74:77]
		cri_odds=line[77:82]
		cri_popular_order=line[82:84]
		cri_fukusho_odds=line[84:89]
		cri_fukusho_popluar_order=line[89:91]
		specific_info_1=line[91:94]
		specific_info_2=line[94:97]
		specific_info_3=line[97:100]
		specific_info_4=line[100:103]
		specific_info_5=line[103:106]
		sogo_info_1=line[106:109]
		sogo_info_2=line[109:112]
		sogo_info_3=line[112:115]
		sogo_info_4=line[115:118]
		sogo_info_5=line[118:121]
		pop_score=line[121:126].replace("0-","-")
		train_score=line[126:131].replace("0-","-")
		trainer_score=line[131:136].replace("0-","-")
		train_code=line[136:137]
		trainer_hyoka_code=line[137:138]
		jockey_rate_rentai=line[138:142]
		gekiso_score=line[142:145].replace("0-","-")
		hidume_code=line[145:147]
		#蹄コード分割
		if hidume_code == 0:
			hidume_shape = 0
			hidume_size = 0
		else :
			hidume_shape = (hidume_code-1) / 4 + 1
			hidume_size = hidume_code % 4
			if hidume_size == 0:
				hidume_size = 4

		omotekisei_code=line[147:148]
		class_code=line[148:150]
		yobi4=line[150:152]
		brinkers=line[152:153]
		jockey_name=line[153:159]
		kinryo=line[159:162]
		minarai=line[162:163]
		trainer_name=line[163:169]
		trainer_shozoku=line[169:171]
		
		#ズレチェック（F.フーラハ問題）
		import re
		regex = r'0'
		pattern = re.compile(regex)
		matchObj = pattern.findall(trainer_shozoku)
		w_end = len(matchObj)
		if w_end >0:
			print("スペース位置:",w_end)
			print("異常ファイル")
			line = line[w_end:]
			trainer_shozoku=line[169:171]
		
		zenso_seiseki_key_1=line[171:187]
		zenso_seiseki_key_2=line[187:203]
		zenso_seiseki_key_3=line[203:219]
		zenso_seiseki_key_4=line[219:235]
		zenso_seiseki_key_5=line[235:251]
		zenso_racekey_1=line[251:259]
		zenso_racekey_2=line[259:267]
		zenso_racekey_3=line[267:275]
		zenso_racekey_4=line[275:283]
		zenso_racekey_5=line[283:291]
		waku=line[291:292]
		yobi5=line[292:294]
		sogo_shirushi=line[294:295]
		idm_shiruishi=line[295:296]
		info_shirushi=line[296:297]
		jockey_shirushi=line[297:298]
		trainer_shirushi=line[298:299]
		train_shirushi=line[299:300]
		gekiso_shirushi=line[300:301]
		turf_adjust_code=line[301:302]
		dart_adjust_code=line[302:303]
		jockey_code=line[303:308]
		trainer_code=line[308:313]
		yobi6=line[313:314]
		kakutoku_money=line[314:320]
		shukaku_money=line[320:325]
		joken=line[325:326]
		ten_score=line[326:331].replace("0-","-")
		pace_score=line[331:336].replace("0-","-")
		up_score=line[336:341].replace("0-","-")
		position_score=line[341:346].replace("0-","-")
		pace_predict=line[346:347]
		dochu_order=line[347:349]
		dochu_sa=line[349:351]
		dochu_in_out=line[351:352]
		last_order=line[352:354]
		last_sa=line[354:356]
		last_in_out=line[356:357]
		order=line[357:359]
		sa=line[359:361]
		in_out=line[361:362]
		tenkai=line[362:363]
		distance_adjust2=line[363:364]
		commit_weight=line[364:367]
		commit_weight_increase=line[367:370]
		torikeshi=line[370:371]
		sex=line[371:372]
		owner_name=line[372:392]
		banushikai_code=line[392:394]
		umakigo_code=line[394:396]
		gekiso_order=line[396:398]
		ls_score_order=line[398:400]
		ten_score_order=line[400:402]
		pace_score_order=line[402:404]
		up_score_order=line[404:406]
		position_score_order=line[406:408]
		expect_jokey_win_rate=line[408:412]
		expect_jokey_rentai_rate=line[412:416]
		yuso=line[416:417]
		soho=line[417:425]
		taikei_data=line[425:449]
		taikei = line[425]
		senaka = line[426]
		do = line[427]
		siri = line[428]
		tomo = line[429]
		harabukuro = line[430]
		head = line[431]
		neck = line[432]
		breast = line[433]
		shoulder = line[434]
		zencho = line[435]
		kocho = line[436]
		maehaba = line[437]
		ushirohaba = line[438]
		maetsunagi = line[439]
		ushirotsunagi = line[440]
		#尻尾は、上げるか下げるかのため、修正なし
		tail = line[441]
		furikata = line[442]
		taikei_sogo1=line[449:452]
		taikei_sogo2=line[452:455]
		taikei_sogo3=line[455:458]
		umatokki1=line[458:461]
		umatokki2=line[461:464]
		umatokki3=line[464:467]
		horse_start_score=line[467:471].replace("0-","-")
		horse_latestart_rate=line[471:475]
		sanko_zenso=line[475:477]
		sanko_zenso_jockey_code=line[477:482]
		mambaken_score=line[482:485].replace("0-","-")
		mambaken_shirushi=line[485:486]
		kokyu_flg=line[486:487]
		gekiso_type=line[487:489]
		rest_reason_code=line[489:491]
		flg=line[491:507]
		turf_dart_steeple_flg=line[491]
		distance_flg=line[492]
		class_flg=line[493]
		tenkyu_flg=line[494]
		kyosei_flg=line[495]
		norikae_flg=line[496]
		runtimes_first_train=line[507:509]
		date_first_train=line[509:517]
		days_after_first_train=line[517:520]
		
		#放牧先以降は、encodeが必要
		w_gaikyu = line[520:].encode('sjis')
		hobokusaki = w_gaikyu[0:50].decode('sjis')
		hobokusaki_rank = w_gaikyu[50:51].decode('sjis')
		trainer_rank = w_gaikyu[51:52].decode('sjis')
		
		#ここからDB操作
		new_racehorse = RacehorseData(
			racehorsekey = racehorsekey,
			racekey = racekey,
			bacode = bacode,
			year = year,
			kai = kai,
			day = day,
			race = race,
			num=num,
			blood=blood,
			horse=horse,
			idm=idm,
			jockey_score=jockey_score,
			info_score=info_score,
			yobi1=yobi1,
			yobi2=yobi2,
			yobi3=yobi3,
			sogo_score=sogo_score,
			leg_type=leg_type,
			distance_adjust=distance_adjust,
			up_degree=up_degree,
			routin=routin,
			cri_odds=cri_odds,
			cri_popular_order=cri_popular_order,
			cri_fukusho_odds=cri_fukusho_odds,
			cri_fukusho_popluar_order=cri_fukusho_popluar_order,
			specific_info_1=specific_info_1,
			specific_info_2=specific_info_2,
			specific_info_3=specific_info_3,
			specific_info_4=specific_info_4,
			specific_info_5=specific_info_5,
			sogo_info_1=sogo_info_1,
			sogo_info_2=sogo_info_2,
			sogo_info_3=sogo_info_3,
			sogo_info_4=sogo_info_4,
			sogo_info_5=sogo_info_5,
			pop_score=pop_score,
			train_score=train_score,
			trainer_score=trainer_score,
			train_code=train_code,
			trainer_hyoka_code=trainer_hyoka_code,
			jockey_rate_rentai=jockey_rate_rentai,
			gekiso_score=gekiso_score,
			hidume_code=hidume_code,
			hidume_shape=hidume_shape,
			hidume_size=hidume_size,
			omotekisei_code=omotekisei_code,
			class_code=class_code,
			yobi4=yobi4,
			brinkers=brinkers,
			jockey_name=jockey_name,
			kinryo=kinryo,
			minarai=minarai,
			trainer_name=trainer_name,
			trainer_shozoku=trainer_shozoku,
			zenso_seiseki_key_1=zenso_seiseki_key_1,
			zenso_seiseki_key_2=zenso_seiseki_key_2,
			zenso_seiseki_key_3=zenso_seiseki_key_3,
			zenso_seiseki_key_4=zenso_seiseki_key_4,
			zenso_seiseki_key_5=zenso_seiseki_key_5,
			zenso_racekey_1=zenso_racekey_1,
			zenso_racekey_2=zenso_racekey_2,
			zenso_racekey_3=zenso_racekey_3,
			zenso_racekey_4=zenso_racekey_4,
			zenso_racekey_5=zenso_racekey_5,
			waku=waku,
			yobi5=yobi5,
			sogo_shirushi=sogo_shirushi,
			idm_shiruishi=idm_shiruishi,
			info_shirushi=info_shirushi,
			jockey_shirushi=jockey_shirushi,
			trainer_shirushi=trainer_shirushi,
			train_shirushi=train_shirushi,
			gekiso_shirushi=gekiso_shirushi,
			turf_adjust_code=turf_adjust_code,
			dart_adjust_code=dart_adjust_code,
			jockey_code=jockey_code,
			trainer_code=trainer_code,
			yobi6=yobi6,
			kakutoku_money=kakutoku_money,
			shukaku_money=shukaku_money,
			joken=joken,
			ten_score=ten_score,
			pace_score=pace_score,
			up_score=up_score,
			position_score=position_score,
			pace_predict=pace_predict,
			dochu_order=dochu_order,
			dochu_sa=dochu_sa,
			dochu_in_out=dochu_in_out,
			last_order=last_order,
			last_sa=last_sa,
			last_in_out=last_in_out,
			order=order,
			sa=sa,
			in_out=in_out,
			tenkai=tenkai,
			distance_adjust2=distance_adjust2,
			commit_weight=commit_weight,
			commit_weight_increase=commit_weight_increase,
			torikeshi=torikeshi,
			sex=sex,
			owner_name=owner_name,
			banushikai_code=banushikai_code,
			umakigo_code=umakigo_code,
			gekiso_order=gekiso_order,
			ls_score_order=ls_score_order,
			ten_score_order=ten_score_order,
			pace_score_order=pace_score_order,
			up_score_order=up_score_order,
			position_score_order=position_score_order,
			expect_jokey_win_rate=expect_jokey_win_rate,
			expect_jokey_rentai_rate=expect_jokey_rentai_rate,
			yuso=yuso,
			soho=soho,
			taikei_data=taikei_data,
			taikei = taikei,
			senaka = senaka,
			do = do,
			siri = siri,
			tomo = tomo,
			harabukuro = harabukuro,
			head = head,
			neck = neck,
			breast = breast,
			shoulder = shoulder,
			zencho = zencho,
			kocho = kocho,
			maehaba = maehaba,
			ushirohaba = ushirohaba,
			maetsunagi = maetsunagi,
			ushirotsunagi = ushirotsunagi,
			tail = tail,
			furikata = furikata,
			taikei_sogo1=taikei_sogo1,
			taikei_sogo2=taikei_sogo2,
			taikei_sogo3=taikei_sogo3,
			umatokki1=umatokki1,
			umatokki2=umatokki2,
			umatokki3=umatokki3,
			horse_start_score=horse_start_score,
			horse_latestart_rate=horse_latestart_rate,
			sanko_zenso=sanko_zenso,
			sanko_zenso_jockey_code=sanko_zenso_jockey_code,
			mambaken_score=mambaken_score,
			mambaken_shirushi=mambaken_shirushi,
			kokyu_flg=kokyu_flg,
			gekiso_type=gekiso_type,
			rest_reason_code=rest_reason_code,
			flg=flg,
			turf_dart_steeple_flg=turf_dart_steeple_flg,
			distance_flg=distance_flg,
			class_flg=class_flg,
			tenkyu_flg=tenkyu_flg,
			kyosei_flg=kyosei_flg,
			norikae_flg=norikae_flg,
			runtimes_first_train=runtimes_first_train,
			date_first_train=date_first_train,
			days_after_first_train=days_after_first_train,
			hobokusaki=hobokusaki.replace("0",""),
			hobokusaki_rank=hobokusaki_rank,
			trainer_rank=trainer_rank
		)
		session.add(new_racehorse)

session.commit()
