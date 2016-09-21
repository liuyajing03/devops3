# coding=utf-8
import unittest, pdb

x = "哈哈哈哈哈哈哈哈xxcicrbnclsuiycbfeej1938e47rrceicboof7o845yfyljcns;sjcp98qeoqyf43bbfljnlfcuhehrfuh"

def codeCount(char_in):
	char = unicode(char_in,"utf-8")
	b = {}
	for i,ch in enumerate(char):
		if ch not in b:
			b[ch] = 1
		else:
			b[ch] += 1
	c = sorted(b.iteritems(), key = lambda asd:asd[1], reverse = True)
	i = 0
	d = []
	for res in c:
		if i <=9:
			d.append(c[i])
			i += 1
		else:
			break
	return d


class TestCameltoUnderline(unittest.TestCase):
	def test(self):
		char_in = "aaaaccc4444444你"
		res = [(u'4', 7), (u'a', 4), (u'c', 3),(u'你', 1)]
		self.assertEqual(codeCount(char_in), res)

if __name__ == "__main__":
	unittest.main()

