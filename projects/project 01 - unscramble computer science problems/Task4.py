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

# Set with all the callers from calls list
set_callers = set(list(zip(*calls))[0])
# Set with all other telephone numbers
set_others_phone = set(list(zip(*calls))[1] + list(zip(*texts))[0] + list(zip(*texts))[1])

# Save all callers that is not on the other lists here.
possibles_telemarketers = set()
for caller in set_callers:
    if caller not in set_others_phone:
        possibles_telemarketers.add(caller)

# Answer to Task4.py
print("These numbers could be telemarketers:")
possibles_telemarketers = sorted(possibles_telemarketers)
for phone in possibles_telemarketers:
  print(phone)