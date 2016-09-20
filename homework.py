#! /usr/bin/env python2.7
# -*- coding:utf8 -*-
__author__ = 'samsing'
import  unittest
def getChar(str1):
    dict_num_char = {}
    dict_char_num = {i:str1.count(i) for i in str1}
    for _char,_num in dict_char_num.items():
        if dict_num_char.get(_num):
            dict_num_char[_num].append(_char)
        else:
            dict_num_char[_num] = [_char]
    dict_char_k = sorted(dict_num_char.items(), key=lambda asd:asd[0], reverse=True)
    print dict_char_k[0][1].sort()
    return((dict_char_k[0][0], ' | '.join(dict_char_k[0][1])))

class TestGetChar(unittest.TestCase):
    def test_getChar(self):
        testStr = "hellowoorld"
        self.assertEquals(getChar(testStr), (3,'l | o'))

if __name__ == "__main__":
    unittest.main()
