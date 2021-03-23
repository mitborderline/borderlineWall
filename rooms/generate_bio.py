# script for generating a roomX.html popup bio

###### EDIT THESE PARAMETERS
room_num = 27

# name = "Gloria Lin"
description = "Hi I’m Yijun! I’m a 2024, prospective Course 10 (ChemE), Borderline Animation Co-Chair, and DAAMIT Publicity Chair. I love figure drawing, sketchbooks, STICKERS, and art in general! If you’re a 2025, I look forward to meeting you soon, and if you’re a current student, I’ll see you around!"
headshot = True
# Username Only for socials
instagram = "y.yang.art"
facebook = ""
############################

filename = './bios/room' + str(room_num) + '.html'
bio_file = open(filename, "x")

head = "<head>\n\t<link rel=\"stylesheet\" href=\"../../main.css\">\n</head><div class=\"room\"> \n"
headshot_str = "<img class=\"headshot\" src=\"../headshots/headshot" + str(room_num)+ ".jpg\" alt=\"headshot\" align=\"right\">" if headshot else ""
description_str = "\n <p>" + description + "</p>\n</div> \n"
social_media = ""
if len(instagram) > 0 or len(facebook) > 0:
	fb_str = ""
	ig_str = ""
	if len(facebook) > 0:
		fb_str = '<a href="https://www.facebook.com/'+ facebook + '" target="_fb"><img class="icon" alt="Facebook" src="https://image.flaticon.com/icons/svg/124/124010.svg"></a>'
	if len(instagram) > 0:
		ig_str = '<a href="https://www.instagram.com/'+ instagram + '/" target="_ig"><img class="icon"alt="Instagram" src="https://image.flaticon.com/icons/svg/174/174855.svg"></a>'
	social_media += '\n <div class="row"> \n' + fb_str + "\n" + ig_str + "\n</div>"

new_file_content = "".join([head, headshot_str, description_str, social_media])
bio_file.write(new_file_content)
bio_file.close()

