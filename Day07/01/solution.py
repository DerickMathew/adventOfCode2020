import re 

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def getBags(lines):
	bags = {}
	for line in lines:
		[outerBag, rawInnerBags] = line.split('contain')
		outerBag = re.search('^[a-zA-Z ]* bag', outerBag).group(0)
		outerBag = outerBag[:-4]
		bags[outerBag] = set()
		innerBagsWithcount = rawInnerBags.split(',')
		for innerBagWithcount in innerBagsWithcount:
			innerBag = re.search('[0-9]* [a-zA-Z ]* bag', innerBagWithcount).group(0)
			innerBag = re.search('[[a-zA-Z][a-zA-Z ]+', innerBag[:-4]).group(0)
			bags[outerBag].add(innerBag)
	return bags

def getBagsWith(bags, description):
	return filter(lambda key: description in bags[key], bags.keys())

def solution():
	lines = getLines()
	bags = getBags(lines)
	visitedBags = []
	bagsToVisit = set(getBagsWith(bags, 'shiny gold'))
	while len(bagsToVisit) > 0:
		currentBag = bagsToVisit.pop()
		if currentBag not in visitedBags:
			visitedBags.append(currentBag)
			newBags = getBagsWith(bags, currentBag)
			for bag in newBags:
				bagsToVisit.add(bag)
	print len(visitedBags)
	

solution()
