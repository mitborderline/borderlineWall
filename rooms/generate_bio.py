# script for generating a roomX.html popup bio

###### EDIT THESE PARAMETERS
room_num = 31

# name = "Gloria Lin"
description = "Hello! I'm Emily. I'm a class of 2023 in 6-3 with a love for developing electric race cars (check out fsae.mit.edu) and helping to advance medicine and healthcare (UROPed for designing and developing medical device). Born in Chengdu, China, but now I'm calling San Francisco Bay Area my home. My room in tunnel 66 preserves a little bit of everything from different dorm rooms (because rona) I lived in since freshmen year (MacGregor, Maseeh, McCormick, and Simmons) and my home. Feel free to stalk me at yxshi.io."
headshot = True
# Username Only for socials
instagram = "emilyshi1003"
facebook = "yongxin.shi.1"
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

