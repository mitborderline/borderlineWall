# script for generating a roomX.html popup bio

###### EDIT THESE PARAMETERS
room_num = 26
# name = "Gloria Lin"
description = "I'm Philena Liu, a current frosh ('24) living in MacGregor G Entry! I'm thinking of majoring in 18C (or maybe 18 or 6), and I'm involved in Borderline (as the co-pub chair woohoo <33) and HMMT. I bought a bunch of tapestry and pillows online (shown in the drawing), and I have super bad posture so I STRUGGLED to move the shelves around so that I could place my monitor higher up. Let's hope my neck doesn't hurt this semester *crosses fingers*. More about me: I like to play badminton (top right shelf!), draw, do css and struggle with css, whistle, watch kdramas/anime/webtoons, and listen to kpop in my free time ;))"
headshot = True
# Username Only for socials
instagram = "liup1134"
facebook = "philenaliu"
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

