"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def find_telemarketers(data1: list, data2: list):
    
    caller = set()
    responder = set()
    texter = set()
    reciever = set()
    
    for call in data1:
        caller.add(call[0])
        responder.add(call[1])
    for call in data2:
        texter.add(call[0])
        reciever.add(call[1])
    
    prob_telemarketers = []
    RespTextRecieves = set().union(responder, texter, reciever)
    for contact in caller:
        if contact not in RespTextRecieves:
            prob_telemarketers.append(contact)
    
    return sorted(prob_telemarketers)

prob_telemarketers = find_telemarketers(calls, texts)
print("These numbers could be telemarketers:")
for prob_telemarketer in prob_telemarketers:
    print(prob_telemarketer)


