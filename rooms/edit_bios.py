# script for editing all the bios
# TODO: rooms 19 and 20 have some undecodable character --> copy the file content over from another room
num_rooms = 24

new = 'src=\"../headshots/headshot'
old = 'src=\"rooms/headshots/headshots/headshot'
# old = '"../main.css"'
# new = '"../../main.css"'

for i in range(20,num_rooms+1):
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


