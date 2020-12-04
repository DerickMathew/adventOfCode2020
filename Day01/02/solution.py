def findNumbersThatAddUpTo(numbers, year):
	for i in xrange(len(numbers)):
		for j in xrange(i+1, len(numbers)):
			remainingSum = year - (numbers[i] + numbers[j])
			if remainingSum in  numbers[j+1:]:
				return [numbers[i], numbers[j],  remainingSum]

def getLinesFromInput():
	inputFile = open('../input.txt', 'r') 
	return inputFile.readlines()

def solution():
	year = 2020
	reportLines = getLinesFromInput()
	numbersInReport = map(lambda x:int(x), reportLines)
	numbersWhoAddUp  = findNumbersThatAddUpTo(numbersInReport, year)
	print reduce(lambda num1, num2: num1 * num2, numbersWhoAddUp)

solution()
