import os
import sys
from pathlib import Path

def Create(path, strs):
	
	#file open
	file_list  = open("{0}/{1}/list.txt".format(path, strs), "w")
	file_label = open("{0}/{1}/label.txt".format(path, strs), "w")
	
	#The path object genetate
	p = Path("{0}/{1}".format(path, strs))
	
	class_no = []
	class_name = []
	for i in p.glob("**/*"):
		# A directory or file judges
		if os.path.isfile(i):
			
			# windows path convert to string
			file_name = str(i)
			c = 0
			for j in class_no:
				if(j in str(i)):
					temp = strs + "\\"
					file_list.write("{0} {1}\n".format(file_name.replace(str(temp), "").replace(str(path), ""), c))
					break
				c += 1
			
		else: 
			class_no.append(str(i))
			class_name.append(str(i).replace("{0}{1}".format(path, strs),"").replace(strs,"").replace("\\", ""))
	
	c = 0
	for i in class_name:
		file_label.write("{0} {1}\n".format(c, i))
		c += 1

	print(class_name)

if __name__ == '__main__':
	args = sys.argv
	
	if len(args) < 2:
		print("  python build_database.py [data_folder]\n")
		exit(0)
	
	path = args[1]
	Create(path, "train")
	Create(path, "test")