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
    TASK 2: Which telephone number spent the longest time on the phone
    during the period? Don't forget that time spent answering a call is
    also time spent on the phone.
    Print a message:
    "<telephone number> spent the longest time, <total time> seconds, on the phone during
    September 2016.".
    """



import collections

def count_time(data: list) -> dict:
    number2time = collections.defaultdict(int)
    for conversation in data:
        for phone_number in [conversation[0], conversation[1]]:
            number2time[phone_number] += int(conversation[3])
    return number2time


def get_max_number() -> (int, int):
    number2time = count_time(calls)
    
    #max_key = max(number2time, key = number2time.get)
    #return max_key, number2time[max_key]
    
    # if max version not allowed, self implemented:
    max_val = 0
    max_val_num = ""
    for key, val in number2time.items():
        if val > max_val:
            max_val = val
            max_val_num = key
    
    return max_val_num, max_val

max_val_num, max_val = get_max_number()

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
                                                                                          max_val_num, max_val))


