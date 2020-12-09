def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

NOOP = 'nop'
ACCUMULATOR = 'acc'
JUMP = 'jmp'
EXECUTED_INSTRUCTIONS = 'executedInstructions'

def executeInstructions(instructions, position, accumulator, executedInstructions):
	if position >= len(instructions):
		return {ACCUMULATOR : accumulator}
	if position in executedInstructions:
		return {EXECUTED_INSTRUCTIONS: executedInstructions}
	executedInstructions.append(position)
	(instruction, number) = instructions[position].split(' ')
	if instruction == NOOP or instruction == ACCUMULATOR:
		position += 1
	if instruction == ACCUMULATOR:
		accumulator += int(number)
	if instruction == JUMP:
		position += int(number)
	return executeInstructions(instructions, position, accumulator, executedInstructions)

def getAccumulatorWhenFixed(instructions, corruptableInstructionPositions):
	for instructionPosition in corruptableInstructionPositions:
		(instruction, number) = instructions[instructionPosition].split(' ')
		newInstructions = instructions[:]
		if instruction == JUMP:
			newInstructions[instructionPosition] = NOOP + ' ' + number
			result = executeInstructions(newInstructions, 0, 0, [])
			if result.has_key(ACCUMULATOR):
				return result[ACCUMULATOR]
		elif instruction == NOOP and int(number) != 0:
			newInstructions[instructionPosition] = JUMP + ' ' + number
			result = executeInstructions(newInstructions, 0, 0, [])
			if result.has_key(ACCUMULATOR):
				return result[ACCUMULATOR]

def solution():
	instructions = getLines()
	result = executeInstructions(instructions, 0, 0, [])
	if result.has_key(EXECUTED_INSTRUCTIONS):
		corruptableInstructionPositions = result[EXECUTED_INSTRUCTIONS]
		print getAccumulatorWhenFixed(instructions, corruptableInstructionPositions)


solution()
