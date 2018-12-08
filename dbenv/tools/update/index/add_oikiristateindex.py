﻿from horseview.horsemodel import sesobj,OikiriStateIndex
import sys,pandas as pd,csv,numpy as np

file = sys.argv[1]
print(file)

#ここからファイル操作
df = csv.reader(open(file, 'r'))
data = [ v for v in df]
mat = np.array(data)

for i in range(len(mat)):
	index = mat[i,0]
	oikiri_state = mat[i,1]
	new_oikiri_state = OikiriStateIndex(index = index,oikiri_state = oikiri_state)
	sesobj.add(new_oikiri_state)

sesobj.commit()
