import unittest, pdb

x = "xxcicrbnclsuiycbfeej1938e47rrceicboof7o845yfyljcns;sjcp98qeoqyf43bbfljnlfcuhehrfuh"

def codeCount(char_in):
	a = []
	b = {}
	for i,ch in enumerate(char_in):
		y = 0
		for strx in a:
			if ch == strx:
				break
			else:
				y = y + 1
				continue
		if y == len(a):
			a.append(ch)

	for strx in a:
		b[strx] = 0
		for i,ch in enumerate(char_in):
			if ch == strx:
				b[strx] = b[strx] + 1
			else:
				continue
	
	c = sorted(b.iteritems(), key = lambda asd:asd[1], reverse = True)
	i = 0
	e = []
	for res in c:
		i += 1
		if i<= 10:
			e.append(res)
	return dict(e)

class TestCameltoUnderline(unittest.TestCase):
    def test(self):
        char_in = "aaaaccc4444444"
        res = {'4': 7, 'a': 4, 'c': 3}
        self.assertEqual(codeCount(char_in), res)
		
if __name__ == "__main__":
    unittest.main()

