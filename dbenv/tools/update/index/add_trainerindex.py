﻿from horseview.horsemodel import sesobj,TrainerIndex
import sys,pandas as pd,csv,numpy as np

file = sys.argv[1]
print(file)

#ここからファイル操作
df = csv.reader(open(file, 'r'))
data = [ v for v in df]
mat = np.array(data)

for i in range(len(mat)):
	index = mat[i,0]
	trainer_code = mat[i,1]
	new_trainer = TrainerIndex(index = index,trainer_code = trainer_code)
	sesobj.add(new_trainer)

sesobj.commit()
