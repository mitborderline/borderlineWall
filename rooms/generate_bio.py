# script for generating a roomX.html popup bio

###### EDIT THESE PARAMETERS
room_num = 16

# name = "Gloria Lin"
description = "Hello everyone! I'm Jessica Pan, a 2024 in Computer Science and Molecular Biology (6-7) with a minor in 4b (Art and Design). I'm originally from Chicago, but I'm currently living in McCormick 3E and am excited to meet everyone! I'm also a part of ESP (the educational studies program, which runs Spark, Splash, and other events you might have heard of!), Lean on Me, and a couple of other clubs. I look forward to meeting you all, in whatever form that takes :D "
headshot = False
# Username Only for socials
instagram = ""
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

