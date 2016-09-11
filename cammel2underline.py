#!/usr/bin/python

import unittest

def camel_to_underline(camel_format):
	underline_format=''
	if isinstance(camel_format, str):
		for _s_ in camel_format:
			underline_format += _s_ if _s_.islower() else '_'+_s_.lower()
	return underline_format
	
class TestCameltoUnderline(unittest.TestCase):
	def test_upper_num(self):
		camel="aaaC4321dfafe"
		underline="aaa_c4321"
	def test_upper(self):
		camel = "aaaBbbCccc"
		underline = "aaa_bbb_ccc_dd"
		self.assertEqual(camel_to_underline(came),underline)
		
		
if __name__ =="__main__":
	unittest.main