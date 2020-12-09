def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def executeInstructions(instructions, position, accumulator, executedInstructions):
	if position in executedInstructions:
		return accumulator
	executedInstructions.append(position)
	(instruction, number) = instructions[position].split(' ')
	number = int(number)
	if instruction == 'nop':
		return executeInstructions(instructions, position + 1, accumulator, executedInstructions)
	if instruction == 'acc':
		return executeInstructions(instructions, position + 1, accumulator + number, executedInstructions)
	# instruction == 'jmp':
	return executeInstructions(instructions, position + number, accumulator, executedInstructions)

def solution():
	instructions = getLines()
	print executeInstructions(instructions, 0, 0, [])

solution()
