from sqlalchemy import create_engine
from database_setup import Base, BacodeMaster
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
		bacode = line[0:2]
		baname = line[3:5]
		#ここからDB操作
		new_bacode = BacodeMaster(
			bacode = bacode,
			baname = baname
		)
		session.add(new_bacode)

session.commit()
