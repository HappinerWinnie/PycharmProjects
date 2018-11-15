
for num in range(1,1001):
	perfectFactor = 0
	for n in range(1,num):
		if num % n == 0:
			perfectFactor += n
	if perfectFactor == num:
		print("%d是完数且小于1000." % perfectFactor)