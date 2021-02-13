# script for generating a roomX.html popup bio

###### EDIT THESE PARAMETERS
room_num = 25
# name = "Gloria Lin"
description = "Hi! I'm Mindren, a '22 from Chicago doubling in 6-3 and 20. I'm living in Next this semester but lived in MacGregor my first two years here. My MacG single isn't nearly this large, but this is otherwise what my room looks like (featuring my exceptional window view of Simmons, the very conspicuous tennis bubble, and the infamous wind tunnel). Outside of classes, I'm involved with DDR@MIT, Bridge Club, Men's Ultimate, and Camp Kesem -- you might even spot some relevant paraphernalia in my room ;)  "
headshot = True
# Username Only for socials
instagram = "nerd.nim"
facebook = "nerdnim"
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

