# script for generating a roomX.html popup bio

###### EDIT THESE PARAMETERS
room_num = 30

# name = "Gloria Lin"
description = "Hi, I'm Jocelyn Shen, and I'm a junior majoring in course 6-3 and minoring in 14. This was my room in McCormick 7W last year, where I would enjoy the sunset with friends and drink tea (friends not depicted because...social distancing?). On campus, I was a part of SWE (Society of Women Engineers) exec board, and I UROPed in the Media Lab's Personal Robotics group, which is where I'll be doing graduate school next year! Aside from that, in my free time I like to <a href=\"http://jocelynshen.com/#artwork\" target=\"js_\">write and draw</a>! Looking forward to meeting everyone soon :) "
headshot = True
# Username Only for socials
instagram = "jocie_shen"
facebook = "jocelyn.shen.3"
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

