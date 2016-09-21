#!/usr/bin/python
# coding=utf-8

import unittest
from collections import Counter

# Counter 是一个简单的计数器类，可以统计字符出现的个数
# 方法 most_common() 可以返回出现频率最高的字符或单词

s1 = "fdjaoijfineaatghiwo1i853524adwionfdasdfjlkaj;jgisoajfdaf"
s2 = u"aabbbccccddddd或或或或或或"

def charCount(string):
    c = Counter(string)
    return c.most_common(10)

class TestCharCount(unittest.TestCase):
    def test(self):
	res1 = [('a', 8), ('f', 6), ('i', 6), ('j', 6), ('d', 5),
		 ('o', 4), ('5', 2), ('g', 2), ('n', 2), ('s', 2)]
	res2 = [(u'或', 6), (u'd', 5), (u'c', 4), (u'b', 3), (u'a', 2)]
        self.assertEqual(charCount(s1), res1)
        self.assertEqual(charCount(s2), res2)
        self.assertEqual(u'或', u'\u6216')

if __name__ == "__main__":
    print charCount(s1)
    print charCount(s2)
    unittest.main()
    
    
