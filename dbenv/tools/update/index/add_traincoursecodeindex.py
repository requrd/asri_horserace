﻿from horseview.horsemodel import sesobj,TrainCourseCodeIndex
import sys,pandas as pd,csv,numpy as np

file = sys.argv[1]
print(file)

#ここからファイル操作
df = csv.reader(open(file, 'r'))
data = [ v for v in df]
mat = np.array(data)

for i in range(len(mat)):
	index = mat[i,0]
	train_course_code = mat[i,1]
	new_train_course = TrainCourseCodeIndex(index = index,train_course_code = train_course_code)
	sesobj.add(new_train_course)

sesobj.commit()
