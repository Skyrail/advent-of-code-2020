import os, sys  
from math import ceil

def parseSeatFromPass(boardingPass):
    rowCode,columnCode,row,column = boardingPass[:-3], boardingPass[-3:], [0,127], [0,7]

    for r in rowCode:
        if r == 'F':
            row = [row[0],row[1] - ceil((row[1]-row[0])/2)]
        elif r == 'B':
            row = [row[0] + ceil((row[1]-row[0])/2), row[1]]
    else:
        row = row[0] if r == 'F' else row[1]

    for c in columnCode:
        if c == 'L':
            column = [column[0],column[1] - ceil((column[1]-column[0])/2)]
        elif c == 'R':
            column = [column[0] + ceil((column[1]-column[0])/2), column[1]]
    else:
        column = column[0] if c == 'L' else column[1]

    return row,column

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        batch = list(file.read().strip().split('\n'))

        seats = [parseSeatFromPass(boardingPass) for boardingPass in batch]

        maximumSeatId = max(list(map(lambda seat: seat[0]*8+seat[1], seats)))
        
        print(f'Maximum seat ID is {maximumSeatId}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')