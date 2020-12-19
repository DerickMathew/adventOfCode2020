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

# This solution is slow but generic
# check out the solution to part 2 to see a faster implementation (I2)
# (I2) is fast only with AoC input that comes in neat uniform lengths
# and non overlapping strings
def solution():
	lines = getLines()
	start = time()
	(rules, messages) = getRulesAndMessages(lines)
	possibleMessages =  expandRule(rules[0], rules)
	print len(filter(lambda message: message in possibleMessages, messages))
	end = time()
	print end - start

solution()
