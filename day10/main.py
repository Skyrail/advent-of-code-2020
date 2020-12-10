import os, sys
from functools import reduce

def buildGraph(values):
    graph = dict()

    for value in values:
        for difference in range(1,4):
            if value + difference in values:
                if value in graph:
                    graph[value].append(value + difference)
                else:
                    graph[value] = [value + difference]
    
    return graph

def countPathways(graph, start, end, calculated={}):
    pathways = 0

    if start in calculated:
        return calculated[start]

    if start == end:
        pathways += 1
    else:
        nodes = graph[start]
        for node in nodes:
            pathways += countPathways(graph, node, end)
    
    calculated[start] = pathways
    return pathways

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        batch = sorted(list(map(int,file.read().strip().split('\n'))))

        differences, index = [], 0
        # The source supplies 0 jolts, the sink uses +3 the max adapter joltage
        batch.insert(0, 0)
        batch.append(max(batch)+3)

        # Part one
        while index < (len(batch) - 1):                
            differences.append(batch[index+1] - batch[index])
            index += 1
        
        print(f'The differences that count: {differences.count(1)*differences.count(3)}')

        # Part two
        graph = buildGraph(batch)

        print(f'Number of pathways: {countPathways(graph, 0, max(batch))}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')