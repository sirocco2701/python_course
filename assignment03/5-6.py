a = int (input ())
b = int (input ())

for i in range (1, a + 1):
	if i <= b:
		if a % i == 0 and b % i == 0:
			bmm = i

kmm = (a * b)/bmm
print ("kmm",kmm)
print("bmm",bmm)