# script for generating a roomX.html popup bio

###### EDIT THESE PARAMETERS
room_num = 33

# name = "Gloria Lin"
description = "Hihi~ My name is Yiming Chen, and I am a freshman living in China who's interested in 18C (Math+CS), 2 (Mechanical Engineering), and French! I'm involved with Borderline (as co-publicity chair<3), the UA, the MIT Chinese Music Ensemble, and the figure skating club (though I'm an absolute beginner lol). In my free time, I love drawing, painting, playing a traditional Chinese zither called Guzheng, eating fruit, and jogging at a local park while listening to audiobooks. I also love making new friends, so please give me a poke if you wanna chat~ :)"
headshot = True
# Username Only for socials
instagram = "artyiming"
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

