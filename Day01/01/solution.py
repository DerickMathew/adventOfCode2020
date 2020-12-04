def findNumbersThatAddUpTo(numbers, year):
	for i in xrange(len(numbers)):
		difference = year - numbers[i]
		if difference in  numbers[i+1:]:
			return [numbers[i], difference]

def getLinesFromInput():
	inputFile = open('../input.txt', 'r') 
	return inputFile.readlines()

def solution():
	year = 2020
	reportLines = getLinesFromInput()
	numbersInReport = map(lambda x:int(x), reportLines)
	numbersWhoAddUp  = findNumbersThatAddUpTo(numbersInReport, year)
	print numbersWhoAddUp[0] * numbersWhoAddUp[1]

solution()
