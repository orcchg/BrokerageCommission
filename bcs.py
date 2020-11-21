print("Input your portfolio size")
size = input()

def profD(v):
     profQ=0.0531
     if (v >= 100000):
             profQ=0.0413
     if (v >= 300000):
             profQ=0.0354
     if (v >= 1000000):
             profQ=0.0295
     if (v >= 5000000):
             profQ=0.0236
     if (v >= 15000000):
             profQ=0.0177
     tot = profQ * v * 0.01
     if (tot < 35.4):
     	tot = 35.4
     return tot

def profM(v, d):
	tot = profD(v) * d
	if (tot < 177):
		tot = 177
	return 177 + tot

def investorD(v):
	tot = v * 0.001
	return tot

def investorM(v, d):
	return investorD(v) * d

def investorProD(v):
	q = 0.3
	if (size >= 900000):
		q = 0.035
	if (size >= 2500000):
		q = 0.03
	if (size >= 5000000):
		q = 0.025
	if (size >= 10000000):
		q = 0.02
	if (size >= 30000000):
		q = 0.015
	tot = v * q * 0.01
	return tot

def investorProM(v, d):
	return investorProD(v) * d + 299

def traderD(v):
	trQ=0.05
	if (v >= 1000000):
		trQ=0.04
	if (v >= 5000000):
		trQ=0.03
	if (v >= 15000000):
		trQ=0.025
	if (v >= 50000000):
		trQ=0.02
	if (v >= 100000000):
		trQ=0.015
	return v * trQ * 0.01

def traderM(v, d):
	return 199 + traderD(v) * d

def traderProD(v):
	trQ=0.045
	if (v >= 1000000):
		trQ=0.04
	if (v >= 5000000):
		trQ=0.03
	if (v >= 15000000):
		trQ=0.025
	if (v >= 50000000):
		trQ=0.02
	if (v >= 100000000):
		trQ=0.015
	return v * trQ * 0.01

def traderProM(v, d):
	return 299 + traderProD(v) * d

def tinkoffInvestor(v, d):
	return v * 0.003 * d

def tinkoffTraderD(v):
	q = 0.05
	tot = 0
	if (v >= 200000):
		tot = 100 + (v - 200000) * 0.025 * 0.01
	else:
		tot = v * q * 0.01
	return tot

def tinkoffTraderM(v, d):
	tot = tinkoffTraderD(v) * d
	if (size < 2000000):
		tot += 290
	return tot

def tinkoffPremierD(v):
	return v * 0.025 * 0.01

def tinkoffPremierM(v, d):
	tot = 990
	if (size >= 3000000):
		tot = 0
	return tinkoffPremierD(v) * d + tot

v = input()
d = input()
prof = profM(v, d)
investor = investorM(v, d)
investorPro = investorProM(v, d)
trader = traderM(v, d)
traderPro = traderProM(v, d)
tcsInvestor = tinkoffInvestor(v, d)
tcsTrader = tinkoffTraderM(v, d)
tcsPremier = tinkoffPremierM(v, d)

print(profD(v))
print("Professional", prof)
print("Investor    ", investor)
print("Investor Pro", investorPro)
print("Trader      ", trader)
print("Trader Pro  ", traderPro)
print("TCS Investor", tcsInvestor)
print("TCS Trader  ", tcsTrader)
print("TCS Premier ", tcsPremier)

