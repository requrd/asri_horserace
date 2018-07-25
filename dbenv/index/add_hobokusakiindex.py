from sqlalchemy import create_engine
from database_setup import Base, HobokusakiIndex
from sqlalchemy.orm import sessionmaker
import sys
import pandas as pd
import csv
import numpy as np


file = sys.argv[1]
print(file)

##ここからDB操作
engine = create_engine('sqlite:///jrdb.db')
Base.metadata.bind=engine
Session = sessionmaker(bind=engine)
session = Session()

#ここからファイル操作
df = csv.reader(open(file, 'r'))
data = [ v for v in df]
mat = np.array(data)

for i in range(len(mat)):
	index = mat[i,0]
	hobokusaki = mat[i,1]
	new_hobokusaki = HobokusakiIndex(index = index,hobokusaki = hobokusaki)
	session.add(new_hobokusaki)

session.commit()
