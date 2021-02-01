# script for editing all the bios
num_rooms = 24

old = 'src=\"headshot'
new = 'src=\"headshots/headshot'

for i in range(1,num_rooms+1):
	filename = "bios/room"+str(i)+".html"
	bio_file = open(filename)

	string_list = bio_file.readlines()
	for i in range(len(string_list)):
		line = string_list[i]
		# print(line)
		if old in line and new not in line:
			string_list[i] = line.replace(old,new)
			print(string_list[i])

	bio_file = open(filename, "w")
	new_file_content = "".join(string_list)
	bio_file.write(new_file_content)
	bio_file.close()


