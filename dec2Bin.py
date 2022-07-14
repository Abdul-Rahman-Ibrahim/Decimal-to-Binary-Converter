def int2Bin(n):
	if not '.' in str(n):
		if n == 0:
			return 0
		elif n == 1:
			return 1
		ans = []
		while n//2 != 0:
			ans.append(str(n%2))
			n = n//2
		ans.append(str(1))
		ans.reverse()
		return int(''.join(ans))
	else:
		n = str(n)
		if not (n[0]==str(0) or n[0]=='.'):
			i = n.index('.')
			n1, n2 = n[:i], n[i:]
			ans1, ans2 = int2Bin(int(n1)), int2Bin(float(n2))
			ans = float(str(ans1)+'.'+str(ans2))
			return ans
		else:
		 	prec = 0
		 	ans = []
		 	n = float(n)
		 	while n != 0:
		 		n *= 2
		 		if n >= 1:
		 			ans.append(str(1))
		 		else:
		 			ans.append(str(0))
		 		n = n % 1
		 		prec += 1
		 	return (''.join(ans))

x = 0.03
print(int2Bin(x))
