def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)


def isValid(number, rules):
	for key in rules:
		if rules[key]['range1Start'] <= number <= rules[key]['range1End']:
			return True
		if rules[key]['range2Start'] <= number <= rules[key]['range2End']:
			return True
	return False

def getRules(lines):
	rules = {}
	for rule in lines [:20]:
		[ruleName, ruleBreakDown] = rule.split(': ')
		[range1, range2] = ruleBreakDown.split(' or ')
		[range1Start, range1End] = [int(n) for n in range1.split('-')]
		[range2Start, range2End] = [int(n) for n in range2.split('-')]
		rules[ruleName] = {'range1Start': range1Start,'range1End': range1End,'range2Start': range2Start,'range2End': range2End}
	return rules

def solution():
	lines = getLines()
	rules = getRules(lines)
	myTicket = lines[22]
	nearbyTickets = map(lambda ticket: map(lambda n: int(n), ticket.split(',')), lines[25:])
	invalidNumbers = []
	errorRate = 0
	for ticket in nearbyTickets:
		for number in ticket:
			errorRate += number if not isValid(number, rules) else 0
	print errorRate

solution()
