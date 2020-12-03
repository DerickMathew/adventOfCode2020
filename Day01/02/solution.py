YEAR = 2020

def getThirdExpense(expenseReport, year):
	product = 0
	for i in xrange(len(expenseReport)):
		for j in xrange(i+1, len(expenseReport)):
			for k in xrange(j+1, len(expenseReport)):
				sumOfExpenses = expenseReport[i] + expenseReport[j] + expenseReport[k]
				if sumOfExpenses == year:
					return expenseReport[i] * expenseReport[j] * expenseReport[k]

def solution():
	inputFile = open('../input.txt', 'r') 
	reportLines = inputFile.readlines()
	expenseReport = []
	for n in reportLines:
		expenseReport.append(int(n))
	print (getThirdExpense(expenseReport, YEAR))

solution()