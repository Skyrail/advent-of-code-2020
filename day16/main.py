import os, sys, re

if len(sys.argv) != 2:
    raise ValueError('Please supply the input to be processed')

inputPath = sys.argv[1]

def parseRules(ruleText):
    rules = dict()
    lines = ruleText.split('\n')
    ruleRegex = r'([a-z\s]+): ([0-9-]+) or ([0-9-]+)'

    for rule in lines:
        result = re.match(ruleRegex, rule)
        field = result.group(1)
        rules[field] = [r.split('-') for r in result.group(2,3)]
    
    return rules

def isValid(value, rules):
    for limits in rules.values():
        for limit in limits:
            if int(limit[0]) <= int(value) <= int(limit[1]):
                return True

    return False

if os.path.isfile(inputPath):
    try:
        file = open(inputPath)
        
        blocks = file.read().strip().split('\n\n')

        # Input segments:
        # - everything up until 'your ticket:' is the validation
        # - from 'your ticket:' to 'nearby tickets:' is your ticket numbers
        # - from 'nearby tickets:' is the other tickets

        rules,myTicket,otherTickets = blocks

        rules = parseRules(rules)
        myTicket = myTicket.split('\n')[1].split(',')
        otherTickets = [ticket.split(',') for ticket in otherTickets.split('\n')[1:]]

        invalidValues = list()

        for ticket in otherTickets:
            for value in ticket:
                if isValid(value, rules) is False:
                    invalidValues.append(int(value))

        print(f'Ticket scanning error rate is: {sum(invalidValues)}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        file.close()
else:
    print(f'Unable to locate file {inputPath}')