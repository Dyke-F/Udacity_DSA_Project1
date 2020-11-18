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
    TASK 1:
    How many different telephone numbers are there in the records?
    Print a message:
    "There are <count> different telephone numbers in the records."
    """

def count_nums(data1: list, data2: list) -> (set, int):
    """ Returns the total number of different telephone numbers in the dataset """
    
    count_num = set()
    for item in [data1, data2]:
        for idx in range(2):
            count_num.update([row[idx] for row in item])

return count_num, len(count_num)


count_num, count_length = count_nums(texts, calls)
print("There are {} different telephone numbers in the records.".format(count_length))
