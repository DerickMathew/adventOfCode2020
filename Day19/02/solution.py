from time import time

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def getRule(rawRule):
	[number, rule] = rawRule.split(':')
	if 'a' in rule:
		return (int(number), 'a')
	if 'b' in rule:
		return (int(number), 'b')
	rule = map(lambda group: map(lambda n: int(n), group.strip().split(' ')), rule.split('|'))
	return (int(number), rule)

def getRulesAndMessages(lines):
	isRule = True
	rules = {}
	messages = []
	for line in lines:
		if line == '':
			isRule = False
		elif isRule:
			(number, rule) = getRule(line)
			rules[number] = rule
		else:
			messages.append(line)
	return (rules, messages)

def expandRule(rule, rules):
	if rule == 'a' or rule == 'b':
		return [rule]
	if isinstance(rule, int):
		return expandRules(rules[rule], rules)
	expandedOutcomes = []
	for orRule in rule:
		innerOutcomes = ['']
		for innerRule in orRule:
			newInnerOutcomes = []
			for outcome in expandRule(rules[innerRule], rules):
				for expandingOutcome in innerOutcomes:
					newInnerOutcomes.append(''.join([expandingOutcome, outcome]))
			innerOutcomes = newInnerOutcomes
		expandedOutcomes.extend(innerOutcomes)
	return expandedOutcomes

def isValidMiddle(message, possible42s, possible31s):
	if len(message) == 0:
		return True
	if len(message) >= 16 and message[:8] in possible42s and message[-8:] in possible31s:
		return isValidMiddle(message[8:-8], possible42s, possible31s)
	if message[:8] in possible42s:
		return isValidMiddle(message[8:], possible42s, possible31s)
	return False

def matchesFormat(message, possible42s, possible31s):
	# Since we know all 42's and 31's have lengths of exaclty 8 characters
	if len(message) < 24 or len(message) % 8 != 0:
		return False
	messageStart1 = message[:8]
	messageStart2 = message[8:16]
	messageMiddle = message[16:-8]
	messageEnd = message[-8:]
	if messageStart1 in possible42s: # satisfies 8
		if messageStart2 in possible42s and messageEnd in possible31s: # satisfies 11
			return isValidMiddle(messageMiddle, possible42s, possible31s)
	return False

def solution():
	lines = getLines()
	start = time()
	(rules, messages) = getRulesAndMessages(lines)
	possible42s = expandRule(rules[42], rules)
	possible31s = expandRule(rules[31], rules)
	# print '\nWe know all 42`s and 31`s have lengths of exaclty 8 characters'
	# lengthOf42s = set(map(lambda possibility: len(possibility), possible42s))
	# lengthOf31s = set(map(lambda possibility: len(possibility), possible31s))
	# print 'len of 42`s = ' + str(lengthOf42s) + ',\tlen of 31`s = ' + str(lengthOf31s) 
	# intersected = set(possible31s).intersection(set(possible42s))
	# print '\nThe intersection of 42`s and 31`s = ' + str(intersected)
	# print '\n\n' 
	print len(filter(lambda message: matchesFormat(message, possible42s, possible31s), messages))
	end = time()
	print end - start

solution()
