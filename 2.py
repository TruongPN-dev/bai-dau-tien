from time import sleep
while True:
	a = int(input('Nhap so tang a: '))
	for i in range(a):
		print('  '*(a*2-1-i) + '+ '*(i+i+1))
		sleep(0.2)
	for i in range(a):
		print('  '*(a-i-1) + '+ '*(i+1) + '  '* (a*2-1) + '+ '*(i+1))
		sleep(0.2)
		if (i + 1) == a:
			for j in range(a-1):
				print('  '*(a-i) + '+ '*i + '  '*(a*2-1) + '+ '*i)
				i = i - 1
				sleep(0.2)
	for i in range(a):
		print('  '*(a+i) + '+ '*(a*2-i*2-1))
		sleep(0.2)