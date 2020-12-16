import os, sys, re
from functools import reduce
from collections import defaultdict

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

def parseRules(ruleText):
    rules = dict()
    lines = ruleText.split('\n')
    ruleRegex = r'([a-z\s]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)'

    for rule in lines:
        result = re.match(ruleRegex, rule)
        field = result.group(1)
        minX,maxX,minY,maxY = [int(x) for x in result.group(2,3,4,5)]
        rules[field] = set(range(minX,maxX+1)) | set(range(minY,maxY+1))
    
    return rules

def isValid(value, rules):
    
    allRules = reduce(lambda x,y: x.union(y), rules.values())

    if value in allRules:
        return True

    return False

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        blocks = file.read().strip().split('\n\n')

        rules,myTicket,otherTickets = blocks

        rules = parseRules(rules)
        myTicket = myTicket.split('\n')[1].split(',')
        otherTickets = [ticket.split(',') for ticket in otherTickets.split('\n')[1:]]

        validTickets = list()

        for ticket in otherTickets:
            isValidTicket = True
            for value in ticket:
                if isValid(int(value), rules) is False:
                    isValidTicket = False
            if isValidTicket:
                validTickets.append(ticket)

        validFields = defaultdict(set)

        for field,rule in rules.items():
            for i in range(len(validTickets[0])):
                if all(int(ticket[i]) in rules[field] for ticket in validTickets):
                    validFields[field].add(i)

        while all([len(L) == 1 for L in validFields.values()]) == False:
            for field,indicies in validFields.items():
                if len(indicies) == 1:
                    for f,i in validFields.items():
                        if field == f:
                            continue
                        validFields[f] = i - indicies

        result = 1

        for field,index in validFields.items():
            if 'departure' in field:
                result *= int(myTicket[list(index)[0]])

        print(f'The result is {result}')
        

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')