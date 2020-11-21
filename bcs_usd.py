def bcsSpbBase(dollar, a):
	tot = 0.0007 * dollar + 0.004 * a
	if (tot < 1):
		tot = 1
	#tot += 0.004 * a
	spb = 0.004 * a + 0.0001 * dollar
	return tot + spb

dollar = input()
a = input()
print("Spb Base USA", bcsSpbBase(dollar, a))
fx = input()
print("In RUB", bcsSpbBase(dollar, a) * fx)
