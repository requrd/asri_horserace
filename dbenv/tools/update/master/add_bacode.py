from horseview.horsemodel import sesobj,BacodeMaster
import sys

file = sys.argv[1]
print(file)

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
		sesobj.add(new_bacode)

sesobj.commit()
