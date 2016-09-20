#!/usr/bin/python

def read_file(filename):  
	file_object = open(filename)
	try:
		text = file_object.read( )
		return text
	finally:
		 file_object.close( )

def dealdate(txt):
	date=txt.replace(',',' ').replace('.',' ')
	
	print len(date.split())



	

 
if __name__ == '__main__':
	txt = read_file("dome.txt")
	dealdate(txt)