import unittest

def lower_to_upper(string):
	return string.upper()

def upper_to_lower(string):
	return string.lower()

class Test(unittest.TestCase):
	def test_upper(self):
		param = '51reboot'
		res = '51REBOOT'
		self.assertEqual(lower_to_upper(param),res)


if __name__ == '__main__':
	unittest.main()


