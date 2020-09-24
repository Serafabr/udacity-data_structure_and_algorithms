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

## List of telephone numbers in text records. 
# Join the first column (sending numbers) with the second column (receiving number).
list_phones_texts = list(zip(*texts))[0] + list(zip(*texts))[1]

## List of telephone numbers in call records. 
# Join the first column (calling numbers) with the second column (receiving number).
list_phones_calls = list(zip(*calls))[0] + list(zip(*calls))[1]

## List of all numbers. Create a set to eliminate duplicates
set_phones = set(list_phones_calls + list_phones_texts)
num_phones = len(set_phones)

message = "There are {} different telephone numbers in the records."
print(message.format(num_phones))