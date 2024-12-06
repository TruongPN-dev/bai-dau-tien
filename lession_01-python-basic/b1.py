a = 0
dem = 0
while a <= 100:
	if a % 2 != 0:
		if a != 99:
			if dem % 3 == 0:
				print()
				dem = 0
			print(a, end="")
			if dem == 0 or dem == 1:
				print(", ", end="")
			dem += 1
		else:
			print(a, end="")
	a += 1