def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def satisfiesAnyRule(number, rules):
	for key in rules:
		if rules[key]['range1Start'] <= number <= rules[key]['range1End']:
			return True
		if rules[key]['range2Start'] <= number <= rules[key]['range2End']:
			return True
	return False

def isValidTicket(ticket, rules):
	for number in ticket:
		if not satisfiesAnyRule(number, rules):
			return False
	return True

def allNumbersFollowRule(numbers, rule):
	for number in numbers:
		if not (rule['range1Start'] <= number <= rule['range1End']):
			if not (rule['range2Start'] <= number <= rule['range2End']):
				return False
	return True

def getPossibleRules(numbers, rules):
	ruleNames = []
	for ruleName in rules:
		if allNumbersFollowRule(numbers, rules[ruleName]):
			ruleNames.append(ruleName)
	return ruleNames

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
	myTicket = map(lambda n: int(n), lines[22].split(','))
	nearbyTickets = map(lambda ticket: map(lambda n: int(n), ticket.split(',')), lines[25:])
	validTickets = []
	validTickets.append(myTicket)
	errorRate = 0
	for ticket in nearbyTickets:
		if isValidTicket(ticket, rules):
			validTickets.append(ticket)
	possibilities = {}
	keys = []
	for i in xrange(len(myTicket)):
		value = map(lambda ticket: ticket[i], validTickets)
		possibilities[i] = getPossibleRules(value, rules)
		keys.append('')
	for i in xrange(len(myTicket)):
		possibilityKey = filter(lambda key: len(possibilities[key]) == 1, possibilities.keys())[0]
		keys[possibilityKey] = possibilities[possibilityKey][0]
		for key in possibilities.keys():
			possibilities[key] = filter(lambda value: value != keys[possibilityKey] , possibilities[key])
	departureValuesMultiplied = 1
	for index in xrange(len(keys)):
		print str(keys[index]) + '\t' + str(myTicket[index])
		departureValuesMultiplied *= 1 if not('departure' in keys[index]) else myTicket[index]
	print departureValuesMultiplied
	

solution()
