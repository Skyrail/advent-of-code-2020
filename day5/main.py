import os, sys  
from math import ceil

def parseSeatFromPass(boardingPass):

    boardingPass = boardingPass.replace('F', '0').replace('B','1').replace('L','0').replace('R', '1')

    rowCode,columnCode = boardingPass[:-3], boardingPass[-3:]

    row,column = int(rowCode, 2), int(columnCode, 2)

    return row,column

def calculateSeatId(row,column):
    return row*8 + column

def getAvailableSeatId(seatIds):
    possibleIds = set(range(min(seatIds),max(seatIds)))
    availableIds = list(possibleIds.difference(seatIds))

    return availableIds[0]


if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        batch = list(file.read().strip().split('\n'))

        seats = [parseSeatFromPass(boardingPass) for boardingPass in batch]

        seatIds = [calculateSeatId(row,column) for row,column in seats]

        availableId = getAvailableSeatId(seatIds)

        print(f'Max seat ID is {max(seatIds)}')
        print(f'Available seat ID is {availableId}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')