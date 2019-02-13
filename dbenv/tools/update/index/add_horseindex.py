﻿from horseview.horsemodel import sesobj, HorseIndex
import sys, pandas as pd, csv, numpy as np

file = sys.argv[1]
print(file)

# ここからファイル操作
df = csv.reader(open(file, "r"))
data = [v for v in df]
mat = np.array(data)

for i in range(len(mat)):
    index = mat[i, 0]
    blood = mat[i, 1]
    new_horse = HorseIndex(blood=blood, index=index)
    sesobj.add(new_horse)

sesobj.commit()
