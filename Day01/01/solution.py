YEAR = 2020

def getExpense(expenseReport, year):
	for i in xrange(len(expenseReport)):
		for j in xrange(i+1, len(expenseReport)):
			if (expenseReport[i] + expenseReport[j]) == year:
				return (expenseReport[i] * expenseReport[j])

def solution():
	inputFile = open('../input.txt', 'r') 
	reportLines = inputFile.readlines()
	expenseReport = []
	for n in reportLines:
		expenseReport.append(int(n))
	print (getExpense(expenseReport, YEAR))

solution()
