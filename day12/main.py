import os, sys

def getNewCoordinate(current, direction, distance):
    directions = {'N': 1, 'E': 1, 'S': -1, 'W': -1}

    if direction in ('N', 'S'):
        return [current[0] + directions[direction]*distance, current[1]]
    
    if direction in ('E', 'W'):
        return [current[0], current[1] + directions[direction]*distance]

def getNewDirection(current, direction, angle):
    angleDirectionMap = {
        'N': 0, 'E': 90, 'S': 180, 'W': 270,
        0: 'N', 90: 'E', 180: 'S', 270: 'W'
    }
    direction = -1 if direction == 'L' else 1

    currentAngle = angleDirectionMap[current]
    newAngle = abs((currentAngle + angle*direction) % 360)

    return angleDirectionMap[newAngle]

def calculateManhattanDistance(startPoint, endPoint):
    return abs(startPoint[0] - endPoint[0]) + abs(startPoint[1] - endPoint[1])

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        currentBatch = file.read().strip().split('\n')

        startCoordinate = currentCoordinate = [0,0]
        currentDirection = 'E'

        for line in currentBatch:
            instruction,distance = line[0], int(line[1:])

            if instruction in ('N', 'E', 'S', 'W'):
                currentCoordinate = getNewCoordinate(currentCoordinate, instruction, distance)
            elif instruction in ('L', 'R'):
                currentDirection = getNewDirection(currentDirection, instruction, distance)
            elif instruction == 'F':
                currentCoordinate = getNewCoordinate(currentCoordinate, currentDirection, distance)


        manhattanDistance = calculateManhattanDistance(startCoordinate, currentCoordinate)

        print(f'The calculated Manhattan distance is {manhattanDistance}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')