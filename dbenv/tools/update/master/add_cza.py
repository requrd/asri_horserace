from horseview.horsemodel import sesobj,TrainerData
import sys,re

file = sys.argv[1]
print(file)

#ここからファイル操作
with open(file, 'r') as f:
	for line in f:
		trainer_code=line[0:5]
		delete_flg=line[5:6]
		delete_ymd=line[6:14]
		trainer_name=line[14:20]
		
		#各種スペースズレ対応
		regex = r' '
		pattern = re.compile(regex)

		#名前ズレ対応
		matchObj = pattern.findall(trainer_name)
		w_end = len(matchObj)
		if w_end >0:
			print("スペース位置:",w_end)
			print("異常ファイル")
			line = line[w_end:]
		
		trainer_kana=line[20:35]
		#カナズレ対応
		matchObj = pattern.findall(trainer_kana)
		w_end = len(matchObj)
		if w_end >0:
			print("スペース位置:",w_end)
			print("異常ファイル")
			line = line[w_end:]
		
		trainer_name_short=line[35:38]
		matchObj = pattern.findall(trainer_name_short)
		w_end = len(matchObj)
		if w_end >0:
			print("スペース位置:",w_end)
			print("異常ファイル")
			line = line[w_end:]

		shozoku_code=line[38:39]
		shozoku_region=line[39:41]
		birthday=line[41:49]
		
		#国籍ズレ対応
		matchObj = pattern.findall(birthday)
		w_end = len(matchObj)
		if w_end >0:
			print("スペース位置:",w_end)
			print("異常ファイル")
			line = line[w_end:]
		
		get_licence_year=line[49:53]
		trainer_comment=line[53:73]
		
		#コメントズレ対策
		if trainer_comment[0] != "　":
			comment_ymd=line[73:81]
			slide = comment_ymd.find("2")
			if slide > 0:
				line = line[slide:]
		
		comment_ymd=line[73:81]
		this_leading=line[81:84]
		this_seiseki_flat_1st=line[84:87]
		this_seiseki_flat_2nd=line[87:90]
		this_seiseki_flat_3rd=line[90:93]
		this_seiseki_flat_out=line[93:96]
		this_seiseki_steeple_1st=line[96:99]
		this_seiseki_steeple_2nd=line[99:102]
		this_seiseki_steeple_3rd=line[102:105]
		this_seiseki_steeple_out=line[105:108]
		this_tokubetsu_win=line[108:111]
		this_jusho_win=line[111:114]
		last_leading=line[114:117]
		last_seiseki_flat_1st=line[117:120]
		last_seiseki_flat_2nd=line[120:123]
		last_seiseki_flat_3rd=line[123:126]
		last_seiseki_flat_out=line[126:129]
		last_seiseki_steeple_1st=line[129:132]
		last_seiseki_steeple_2nd=line[132:135]
		last_seiseki_steeple_3rd=line[135:138]
		last_seiseki_steeple_out=line[138:141]
		last_tokubetsu_win=line[141:144]
		last_jusho_win=line[144:147]
		total_seiseki_flat_1st=line[147:152]
		total_seiseki_flat_2nd=line[152:157]
		total_seiseki_flat_3rd=line[157:162]
		total_seiseki_flat_out=line[162:167]
		total_seiseki_steeple_1st=line[167:172]
		total_seiseki_steeple_2nd=line[172:177]
		total_seiseki_steeple_3rd=line[177:182]
		total_seiseki_steeple_out=line[182:187]
		data_ymd=line[187:195]
		trainer_index = 0
		
		#ここからDB操作
		new_trainer = TrainerData(
			trainer_code=trainer_code,
			delete_flg=delete_flg,
			delete_ymd=delete_ymd,
			trainer_name=trainer_name,
			trainer_kana=trainer_kana,
			trainer_name_short=trainer_name_short,
			shozoku_code=shozoku_code,
			shozoku_region=shozoku_region,
			birthday=birthday,
			get_licence_year=get_licence_year,
			trainer_comment=trainer_comment,
			comment_ymd=comment_ymd,
			this_leading=this_leading,
			this_seiseki_flat_1st=this_seiseki_flat_1st,
			this_seiseki_flat_2nd=this_seiseki_flat_2nd,
			this_seiseki_flat_3rd=this_seiseki_flat_3rd,
			this_seiseki_flat_out=this_seiseki_flat_out,
			this_seiseki_steeple_1st=this_seiseki_steeple_1st,
			this_seiseki_steeple_2nd=this_seiseki_steeple_2nd,
			this_seiseki_steeple_3rd=this_seiseki_steeple_3rd,
			this_seiseki_steeple_out=this_seiseki_steeple_out,
			this_tokubetsu_win=this_tokubetsu_win,
			this_jusho_win=this_jusho_win,
			last_leading=last_leading,
			last_seiseki_flat_1st=last_seiseki_flat_1st,
			last_seiseki_flat_2nd=last_seiseki_flat_2nd,
			last_seiseki_flat_3rd=last_seiseki_flat_3rd,
			last_seiseki_flat_out=last_seiseki_flat_out,
			last_seiseki_steeple_1st=last_seiseki_steeple_1st,
			last_seiseki_steeple_2nd=last_seiseki_steeple_2nd,
			last_seiseki_steeple_3rd=last_seiseki_steeple_3rd,
			last_seiseki_steeple_out=last_seiseki_steeple_out,
			last_tokubetsu_win=last_tokubetsu_win,
			last_jusho_win=last_jusho_win,
			total_seiseki_flat_1st=total_seiseki_flat_1st,
			total_seiseki_flat_2nd=total_seiseki_flat_2nd,
			total_seiseki_flat_3rd=total_seiseki_flat_3rd,
			total_seiseki_flat_out=total_seiseki_flat_out,
			total_seiseki_steeple_1st=total_seiseki_steeple_1st,
			total_seiseki_steeple_2nd=total_seiseki_steeple_2nd,
			total_seiseki_steeple_3rd=total_seiseki_steeple_3rd,
			total_seiseki_steeple_out=total_seiseki_steeple_out,
			data_ymd=data_ymd,
			trainer_index=trainer_index
		)
		sesobj.add(new_trainer)

sesobj.commit()
