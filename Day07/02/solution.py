import re 

countedBags = {}

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
			countResult = re.search('[0-9]+', innerBagWithcount)
			bagCount = 0 if not countResult else int(countResult.group(0))
			if bagCount > 0:
				innerBag = re.search('[[a-zA-Z][a-zA-Z ]+', innerBag[:-4]).group(0)
				bags[outerBag].add((innerBag, bagCount))
	return bags

def getInnerBagCount(bags, description):
	count = 0 
	if description in countedBags.keys():
		return countedBags[description]
	for bag in bags[description]:
		(innerDescription, bagCount) = bag
		count += bagCount * (1 + getInnerBagCount(bags, innerDescription))
	countedBags[description] = count
	return count

def solution():
	lines = getLines()
	bags = getBags(lines)
	print getInnerBagCount(bags, 'shiny gold')

solution()
