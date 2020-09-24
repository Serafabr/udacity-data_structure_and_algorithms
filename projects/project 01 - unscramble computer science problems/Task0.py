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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_text_message = "First record of texts, {} texts {} at time {}"
last_call_message = "Last record of calls, {} calls {} at time {}, lasting {} seconds"

# Accessing the first record of texts
print(first_text_message.format(texts[0][0], texts[0][1], texts[0][2]))

# Accessing the last record of calls
print(last_call_message.format(calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3]))