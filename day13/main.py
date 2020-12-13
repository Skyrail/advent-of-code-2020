import os, sys

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        currentBatch = file.read().strip().split('\n')

        startTimestamp,busIds = currentBatch

        timestamp = startTimestamp = int(startTimestamp)
        
        busIds = [int(x) for x in busIds.split(',') if x != 'x']
        earliestBusId = 0

        while True:
            for id in busIds:
                if timestamp % id == 0:
                    earliestTimestamp,earliestBusId = timestamp,id
                    break

            if earliestBusId != 0:
                break

            timestamp += 1
                 
        print(f'Earliest timestamp is {timestamp} with bus ID {earliestBusId} which gives {(earliestTimestamp - startTimestamp) * earliestBusId}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')