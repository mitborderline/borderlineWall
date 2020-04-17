for i in range(1,11):
	filename = "room"+str(i)+".html"
	with open(filename, "r") as fp:
		string1 = "<head>\n\t<link rel=\"stylesheet\" href=\"../main.css\">\n</head><div class=\"room\">"
		string2 = "</div>"
		text = fp.read().replace('\n', '')
		mid = "<a href="
		textlist = text.split(mid)

		final = "\n".join([string1, textlist[0], string2, mid, mid.join(textlist[1:])])

	with open(filename, "w") as fp:
		fp.write(final)
