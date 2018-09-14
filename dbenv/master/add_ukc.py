from sqlalchemy import create_engine
from database_setup import Base, HorsebaseData
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
		blood=line[0:8]
		horse=line[8:26]
		sex=line[26:27]
		hair=line[27:29]
		umakigo=line[29:31]
		father=line[31:49]
		mother=line[49:67]
		mother_father=line[67:85]
		birthday=line[85:93]
		father_birthyear=line[93:97]
		mother_birthyear=line[97:101]
		mother_father_birthyear=line[101:105]
		owner=line[105:125]
		owner_kai_code=line[125:127]
		producer=line[127:147]
		locality=line[147:151]
		delete_flg=line[151:152]
		data_ymd=line[152:160]
		father_phylogeny=line[160:164]
		mother_phylogeny=line[164:168]
		horse_index=line[284:290]
		jockey_index=0
		exist_flg = 0
		
		hs = session.query(HorsebaseData).filter(HorsebaseData.blood==blood).first()
		
		if hs is not None:
			hs.horse = horse
			hs.sex=sex
			hs.hair=hair
			hs.umakigo=umakigo
			hs.father=father
			hs.mother=mother
			hs.mother_father=mother_father
			hs.birthday=birthday
			hs.father_birthyear=father_birthyear
			hs.mother_birthyear=mother_birthyear
			hs.mother_father_birthyear=mother_father_birthyear
			hs.owner=owner
			hs.owner_kai_code=owner_kai_code
			hs.producer=producer
			hs.locality=locality
			hs.delete_flg=delete_flg
			hs.data_ymd=data_ymd
			hs.father_phylogeny=father_phylogeny
			hs.mother_phylogeny=mother_phylogeny
			hs.horse_index=horse_index
			session.add(hs)
			exist_flg = 1

		#ここからDB操作
		new_horse = HorsebaseData(
			blood=blood,
			horse=horse,
			sex=sex,
			hair=hair,
			umakigo=umakigo,
			father=father,
			mother=mother,
			mother_father=mother_father,
			birthday=birthday,
			father_birthyear=father_birthyear,
			mother_birthyear=mother_birthyear,
			mother_father_birthyear=mother_father_birthyear,
			owner=owner,
			owner_kai_code=owner_kai_code,
			producer=producer,
			locality=locality,
			delete_flg=delete_flg,
			data_ymd=data_ymd,
			father_phylogeny=father_phylogeny,
			mother_phylogeny=mother_phylogeny,
			horse_index=horse_index
		)
		if exist_flg == 0:
			session.add(new_horse)
session.commit()
