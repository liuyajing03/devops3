x = "xxcicrbnclsuiycbfeej1938e47rrceicboof7o845yfyljcns;sjcp98qeoqyf43bbfljnlfcuhehrfuh"

def codeCount(char_in):
	b = {}
	for i,ch in enumerate(char_in):
		if ch not in b:
			b[ch] = 1
		else:
			b[ch] += 1
	c = sorted(b.iteritems(), key = lambda asd:asd[1], reverse = True)
	i = 0
	for res in c:
		if i <=9:
			print c[i]
			i += 1
		else:
			break

codeCount(x)
