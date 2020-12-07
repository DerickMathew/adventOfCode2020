def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def getGroups(answers):
	groups = []
	stringOfYeses = set()
	reset = True
	for answer in answers:
		if len(answer) == 0:
			groups.append(stringOfYeses)
			stringOfYeses = set()
			reset = True
		else:
			if reset:
				stringOfYeses = set(list(answer))
			else:
				newString = set()
				for char in set(list(answer)):
					if char in stringOfYeses:
						newString.add(char)
				stringOfYeses = newString
			reset = False
	if len(stringOfYeses) > 0:
		groups.append(stringOfYeses)
	return groups

def solution():
	answers = getLines()
	groups = getGroups(answers)
	print sum(map(lambda group: len(set(list(group))), groups))

solution()
