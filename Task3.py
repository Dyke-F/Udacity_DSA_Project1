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
    TASK 3:
    (080) is the area code for fixed line telephones in Bangalore.
    Fixed line numbers include parentheses, so Bangalore numbers
    have the form (080)xxxxxxx.)
    
    Part A: Find all of the area codes and mobile prefixes called by people
    in Bangalore.
    - Fixed lines start with an area code enclosed in brackets. The area
    codes vary in length but always begin with 0.
    - Mobile numbers have no parentheses, but have a space in the middle
    of the number to help readability. The prefix of a mobile number
    is its first four digits, and they always start with 7, 8 or 9.
    - Telemarketers' numbers have no parentheses or space, but they start
    with the area code 140.
    
    Print the answer as part of a message:
    "The numbers called by people in Bangalore have codes:"
    <list of codes>
    The list of codes should be print out one per line in lexicographic order with no duplicates.
    
    Part B: What percentage of calls from fixed lines in Bangalore are made
    to fixed lines also in Bangalore? In other words, of all the calls made
    from a number starting with "(080)", what percentage of these calls
    were made to a number also starting with "(080)"?
    
    Print the answer as a part of a message::
    "<percentage> percent of calls from fixed lines in Bangalore are calls
    to other fixed lines in Bangalore."
    The percentage should have 2 decimal digits
    """


def count_calls(data: list):
    
    bangalore_out_calls_set = set()
    bangalore_out_calls_list = []
    
    for idx, call in enumerate(data):
        
        #if call[0].find("(080)", 0, 5) == 0:
        idx = 0
        prefix = "(080)"
        for char in prefix:
            if char == call[0][idx]:
                idx+=1
        if idx == len(prefix):
            
            
            responder = call[1]
            if responder[0] in ["7", "8", "9"] and " " in responder:
                bangalore_out_calls_set.add(responder[:4])
                bangalore_out_calls_list.append(responder[:4])
            if responder[:3] == "140":
                bangalore_out_calls_set.add(responder[:3])
                bangalore_out_calls_list.append(responder[:3])
            if responder[:2] == "(0" and ")" in responder:
                end_idx = responder.index(")")
                bangalore_out_calls_set.add(responder[:end_idx+1])
                bangalore_out_calls_list.append(responder[:end_idx+1])



return len(bangalore_out_calls_set), sorted(bangalore_out_calls_set), bangalore_out_calls_list



_, call_set, call_list = count_calls(calls)
print("The numbers called by people in Bangalore have codes:")
for code in call_set:
    print(code)
print()




def count_percentage(calls):
    
    call_len, call_set, call_list = count_calls(calls)
    total_num_calls = len(call_list)
    bangalore2bangalore = 0
    for call_code in call_list:
        if call_code == "(080)":
            bangalore2bangalore += 1
    
    return round((bangalore2bangalore / total_num_calls * 100), 3)



print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(count_percentage(calls)))
