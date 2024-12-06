a = 0
dem = 0
while a <= 100:
	if a % 2 !=0:
		if a != 99 and dem != 2:
			print(str(a) + ", ", end="")
			dem += 1
		else:
			print(a)
			dem = 0
	a += 1