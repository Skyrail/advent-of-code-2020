import os, sys
import math

def getNewCoordinate(current, waypoint, distance):
    return [current[0] + waypoint[0]*distance, current[1] + waypoint[1]*distance]

def getNewWaypoint(current, instruction, distance):
    if instruction in ('L', 'R'):
        return rotateWaypoint(current, instruction, distance)
    if instruction in ('N', 'E', 'S', 'W'):
        return moveWaypoint(current, instruction, distance)

def rotateWaypoint(current, direction, angle):
    x,y = current[0], current[1]

    angle = math.radians(angle) if direction == 'R' else math.radians(angle * -1)

    x1 = round(x * math.cos(angle) + y * math.sin(angle))
    y1 = round(-x * math.sin(angle) + y * math.cos(angle))

    return [x1,y1]

def moveWaypoint(current, direction, distance):
    directionMap = {'N': 1, 'S': -1, 'E': 1, 'W': -1}

    if direction in ('N', 'S'):
        return [current[0], current[1] + directionMap[direction]*distance]
    if direction in ('E', 'W'):
        return [current[0] + directionMap[direction]*distance, current[1]]

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
        currentWaypoint = [10,1]

        for line in currentBatch:
            instruction,distance = line[0], int(line[1:])

            if instruction in ('N', 'E', 'S', 'W', 'L', 'R'):
                currentWaypoint = getNewWaypoint(currentWaypoint, instruction, distance)
            elif instruction == 'F':
                currentCoordinate = getNewCoordinate(currentCoordinate, currentWaypoint, distance)

        manhattanDistance = calculateManhattanDistance(startCoordinate, currentCoordinate)

        print(f'The calculated Manhattan distance is {manhattanDistance}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')