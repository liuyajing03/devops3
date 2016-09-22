string = "asdkljfweoriwpeoiraaswlkvmsdlkjf"

res = {}

for i in string:
	if i in res:
		res[i] += 1
	else:
		res[i] = 1

print res
