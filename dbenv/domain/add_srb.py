from sqlalchemy import create_engine
from database_setup import Base, SeisekiRaceData
from sqlalchemy.orm import sessionmaker
import sys,codecs

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
		furlongtime1=line[8:11]
		furlongtime2=line[11:14]
		furlongtime3=line[14:17]
		furlongtime4=line[17:20]
		furlongtime5=line[20:23]
		furlongtime6=line[23:26]
		furlongtime7=line[26:29]
		furlongtime8=line[29:32]
		furlongtime9=line[32:35]
		furlongtime10=line[35:38]
		furlongtime11=line[38:41]
		furlongtime12=line[41:44]
		furlongtime13=line[44:47]
		furlongtime14=line[47:50]
		furlongtime15=line[50:53]
		furlongtime16=line[53:56]
		furlongtime17=line[56:59]
		furlongtime18=line[59:62]
		corner1=line[62:126]
		corner2=line[126:190]
		corner3=line[190:254]
		corner4=line[254:318]
		paceupposition=line[318:320]
		truckbias1_in=line[320:321]
		truckbias1_center=line[321:322]
		truckbias1_out=line[322:323]
		truckbias2_in=line[323:326]
		truckbias2_center=line[326:327]
		truckbias2_out=line[327:328]
		truckbias_muko_in=line[326:329]
		truckbias_muko_center=line[329:330]
		truckbias_muko_out=line[330:331]
		truckbias3_in=line[329:332]
		truckbias3_center=line[332:333]
		truckbias3_out=line[333:334]
		truckbias4_saiuchi=line[332:333]
		truckbias4_in=line[333:334]
		truckbias4_center=line[334:335]
		truckbias4_out=line[333:334]
		truckbias4_oosoto=line[334:335]
		truckbias_straight_saiuchi=line[337:338]
		truckbias_straight_in=line[338:339]
		truckbias_straight_center=line[339:340]
		truckbias_straight_out=line[340:341]
		truckbias_straight_oosoto=line[341:342]
		comment=line[342:842]

		#ここからDB操作
		new_seisekirace = SeisekiRaceData(
			racekey=racekey,
			furlongtime1=furlongtime1,
			furlongtime2=furlongtime2,
			furlongtime3=furlongtime3,
			furlongtime4=furlongtime4,
			furlongtime5=furlongtime5,
			furlongtime6=furlongtime6,
			furlongtime7=furlongtime7,
			furlongtime8=furlongtime8,
			furlongtime9=furlongtime9,
			furlongtime10=furlongtime10,
			furlongtime11=furlongtime11,
			furlongtime12=furlongtime12,
			furlongtime13=furlongtime13,
			furlongtime14=furlongtime14,
			furlongtime15=furlongtime15,
			furlongtime16=furlongtime16,
			furlongtime17=furlongtime17,
			furlongtime18=furlongtime18,
			corner1=corner1,
			corner2=corner2,
			corner3=corner3,
			corner4=corner4,
			paceupposition=paceupposition,
			truckbias1_in=truckbias1_in,
			truckbias1_center=truckbias1_center,
			truckbias1_out=truckbias1_out,
			truckbias2_in=truckbias2_in,
			truckbias2_center=truckbias2_center,
			truckbias2_out=truckbias2_out,
			truckbias_muko_in=truckbias_muko_in,
			truckbias_muko_center=truckbias_muko_center,
			truckbias_muko_out=truckbias_muko_out,
			truckbias3_in=truckbias3_in,
			truckbias3_center=truckbias3_center,
			truckbias3_out=truckbias3_out,
			truckbias4_saiuchi=truckbias4_saiuchi,
			truckbias4_in=truckbias4_in,
			truckbias4_center=truckbias4_center,
			truckbias4_out=truckbias4_out,
			truckbias4_oosoto=truckbias4_oosoto,
			truckbias_straight_saiuchi=truckbias_straight_saiuchi,
			truckbias_straight_in=truckbias_straight_in,
			truckbias_straight_center=truckbias_straight_center,
			truckbias_straight_out=truckbias_straight_out,
			truckbias_straight_oosoto=truckbias_straight_oosoto,
			comment=comment
		)
		session.add(new_seisekirace)

session.commit()
