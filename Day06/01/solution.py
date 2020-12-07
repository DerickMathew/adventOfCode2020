def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def getGroups(answers):
	groups = []
	stringOfYeses = ''
	for answer in answers:
		if len(answer) == 0:
			groups.append(stringOfYeses)
			stringOfYeses = ''
		else:
			stringOfYeses = stringOfYeses + answer
	if len(stringOfYeses) > 0:
		groups.append(stringOfYeses)
	return groups

def solution():
	answers = getLines()
	groups = getGroups(answers)
	print sum(map(lambda group: len(set(list(group))), groups))

solution()
